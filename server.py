from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route('/emotionDetector')
def sent_detector():
    # Retrieve the text to analyze from the request argument
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Check if the response contains None, indicating an error or invalid input
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    else:
        #Return formatted string
        return f"For the given statement, the system response is \
                'anger': {response['anger']}, \
                'disgust': {response['disgust']}, \
                'fear': {response['fear']}, \
                'joy': {response['joy']} and \
                'sadness': {response['sadness']}. \
                The dominant emotion is {response['dominant_emotion']}."

@app.route('/')
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)