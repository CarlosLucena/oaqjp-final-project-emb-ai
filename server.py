from flask import Flask, request, render_template
from EmotionDetection import emotion_detection

app=Flask("emotion_detector")

@app.route("/")
def index():
    return render_template('index.html') 

@app.route("/emotionDetector", methods=["GET"])
def emotion_detector():
    textToAnalyze = request.args.get("textToAnalyze")
    emotion = emotion_detection.emotion_detector(textToAnalyze)
    return emotion, 200

if __name__ == "__main__":
    app.run(debug = True)
