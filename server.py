from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector
import os

# Get the absolute path to the directory containing this file (server.py)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
# Define template and static folder paths relative to this directory
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'static')

# Print paths for debugging
print(f"Base directory: {BASE_DIR}")
print(f"Template directory: {TEMPLATE_DIR}")
print(f"Template exists: {os.path.exists(TEMPLATE_DIR)}")
print(f"index.html exists: {os.path.exists(os.path.join(TEMPLATE_DIR, 'index.html'))}")

# Initialize Flask with absolute paths
app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)


@app.route('/')
def index():
    """
    Render the index.html template.

    Returns:
        str: The rendered HTML content of the index page.
    """
    return render_template('index.html')


@app.route('/emotionDetector', methods=['GET'])
def emotion_detector_route():
    """
    Analyze the emotion of the provided text.

    This endpoint accepts a GET request with a query parameter `textToAnalyze`.
    It analyzes the emotions in the text using the `emotion_detector` function
    and returns a JSON response with the emotion scores or an error message.

    Returns:
        Response: A JSON response containing the emotion scores or an error message.
                  The response also includes an appropriate HTTP status code.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze:
        return jsonify({'error': 'No text provided'}), 400

    emotion_result = emotion_detector(text_to_analyze)

    if 'error' in emotion_result:
        return jsonify(emotion_result), 400

    # Check if dominant_emotion is None
    if emotion_result.get('dominant_emotion') is None:
        return jsonify({'error': 'Invalid text! Please try again!'}), 400

    formatted_response = {
        'anger': emotion_result.get('anger', 0),
        'disgust': emotion_result.get('disgust', 0),
        'fear': emotion_result.get('fear', 0),
        'joy': emotion_result.get('joy', 0),
        'sadness': emotion_result.get('sadness', 0),
        'dominant_emotion': emotion_result.get('dominant_emotion', 'unknown')
    }

    return jsonify(formatted_response)


if __name__ == '__main__':
    """
    Run the Flask application.

    This block starts the Flask development server when the script is executed directly.
    The server listens on all available IP addresses (0.0.0.0) and port 5001.
    Debug mode is enabled for development purposes.
    """
    app.run(host='0.0.0.0', port=5001, debug=True)
