# Emotion Detection Web Application

## Introduction
Welcome to the **Emotion Detection Web Application** project! This project will help you apply your knowledge and skills in AI-based app creation and web deployment. You will develop an **emotion detection application** using **IBM Watson AI** and deploy it as a web application using **Flask**. 

Throughout this project, you will complete structured tasks to build, test, and deploy your application. Follow the instructions carefully to ensure successful completion.

## What is Emotion Detection?
Emotion detection is an advanced form of **sentiment analysis** that identifies nuanced emotions such as **joy, sadness, anger, fear, and more** from text statements. This capability is crucial for applications like **chatbots, recommendation systems, and customer feedback analysis**.

In this project, we will leverage **IBM Watson AI** to create an emotion detection application that analyzes text input and identifies underlying emotions.

---

## Project Files
The following files are used in this project:
- `emotion_detection.py` – Implements the emotion detection logic.
- `__init__.py` – Initializes the application as a package.
- `server.py` – Runs the Flask web application.
- `test_emotion_detection.py` – Contains unit tests for validating the application.

---

## Project Tasks
To complete this project successfully, follow these **step-by-step** tasks:

### **Task 1: Clone the Project Repository**
1. Open a terminal or command prompt.
2. Clone the repository using:
   ```sh
   git clone https://github.com/Nooraldin2001/Final-Project-Emotion-Detector.git
   ```
3. Navigate to the project directory:
   ```sh
   cd Final-Project-Emotion-Detector
   ```

### **Task 2: Create the Emotion Detection Application**
1. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```
2. Utilize **IBM Watson NLP** to analyze text input for emotional content.
3. Implement a function that takes user input and classifies emotions.

### **Task 3: Format the Output**
1. Ensure the application provides clear and structured output.
2. Display emotions detected in a **user-friendly format**, such as:
   ```sh
   Emotion detected: Joy (Confidence: 85%)
   ```

### **Task 4: Package the Application**
1. Organize your code into meaningful **modules and scripts**.
2. Create a `README.md` file with installation and usage instructions.
3. Ensure a `requirements.txt` file is included for easy setup.

### **Task 5: Run Unit Tests**
1. Write unit tests in `test_emotion_detection.py` to validate your application’s functionality.
2. Run tests using:
   ```sh
   pytest test_emotion_detection.py
   ```
3. Fix any failing tests before proceeding.

### **Task 6: Deploy as a Web Application Using Flask**
1. Implement the web interface in `server.py` using **Flask**.
2. Define routes to accept text input and display detected emotions.
3. Start the Flask server:
   ```sh
   python server.py
   ```
4. Open a web browser and test your application.

### **Task 7: Implement Error Handling**
1. Handle unexpected inputs gracefully.
2. Implement try-except blocks to catch errors and prevent application crashes.

### **Task 8: Perform Static Code Analysis**
1. Check for code quality and best practices using **PyLint**:
   ```sh
   pylint server.py
   ```
2. Fix any reported issues before final submission.

---

## **Final Steps**
- Ensure that your application runs smoothly and meets all requirements.


### **Good Luck! 🚀**
Follow the instructions carefully and enjoy building your **Emotion Detection Web Application**!

