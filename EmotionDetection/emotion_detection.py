def emotion_detector(text_to_analyze):
    import requests
    import json
    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = {"raw_document": {"text": text_to_analyze}}
    
    try:
        response = requests.post(url, headers=headers, json=data)
        
        # Handle blank entries by checking status_code
        if response.status_code == 400:
            return {
                "anger": None,
                "disgust": None,
                "fear": None,
                "joy": None,
                "sadness": None,
                "dominant_emotion": None
            }
        
        # Raise an exception for other HTTP errors
        response.raise_for_status()
        
        # Parse the JSON response
        response_data = response.json()
        
        # Extract emotions from the nested structure
        if (
            'emotionPredictions' in response_data and 
            len(response_data['emotionPredictions']) > 0 and
            'emotion' in response_data['emotionPredictions'][0]
        ):
            # Get the emotion scores from the correct location
            emotion_data = response_data['emotionPredictions'][0]['emotion']
            
            # Create emotions dictionary with the values
            emotions = {
                "anger": emotion_data.get("anger", 0),
                "disgust": emotion_data.get("disgust", 0),
                "fear": emotion_data.get("fear", 0),
                "joy": emotion_data.get("joy", 0),
                "sadness": emotion_data.get("sadness", 0)
            }
            
            # Find and add the dominant emotion
            dominant_emotion = max(emotions, key=emotions.get)
            emotions["dominant_emotion"] = dominant_emotion
            
            return emotions
        else:
            # Handle unexpected API response structure
            return {"error": "Unexpected API response structure"}
            
    except requests.exceptions.RequestException as e:
        # Handle API request failures
        return {"error": f"API request failed: {str(e)}"}
    except (json.JSONDecodeError, KeyError, TypeError) as e:
        # Handle errors in processing the response
        return {"error": f"Error processing response: {str(e)}"}