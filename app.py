from flask import Flask, request, render_template, url_for
import os
import joblib
import librosa
import numpy as np

app = Flask(__name__)

# Load trained model and label encoder
model = joblib.load("audio_classification_model_xgb.pkl")
labelencoder = joblib.load("label_encoder.pkl")

predictions_dict = {
    "hungry": {"category": "Hungry!🍼", "message": "I'm hungry, please feed me!", "image": "hungry.png"},
    "discomfort": {"category": "Discomfort!😩", "message": "Please change my diaper!", "image": "diaper.png"},
    "tired": {"category": "Tired!😴", "message": "I need sleep!", "image": "sleepy.png"},
    "belly_pain": {"category": "Belly Pain!💩", "message": "I need to poop!", "image": "poop.png"},
    "burping": {"category": "Burping!🤢", "message": "Tap on my back!", "image": "burping.png"},
}

def features_extractor(file):
    audio, sample_rate = librosa.load(file, res_type="kaiser_fast")
    mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
    return np.mean(mfccs.T, axis=0)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    audio_file = request.files["audio_file"]
    
    if not audio_file.filename.endswith(".wav"):
        return "Only .wav files allowed", 400

    file_path = os.path.join("uploads", audio_file.filename)
    audio_file.save(file_path)

    features = features_extractor(file_path).reshape(1, -1)
    predicted_class = labelencoder.inverse_transform(model.predict(features))[0]
    prediction_info = predictions_dict.get(predicted_class, {"category": "Unknown", "message": "No message available", "image": "default.png"})

    return render_template("result.html", category=prediction_info["category"], message=prediction_info["message"], image_url=url_for('static', filename=prediction_info["image"]))

if __name__ == "__main__":
    app.run(debug=True)
