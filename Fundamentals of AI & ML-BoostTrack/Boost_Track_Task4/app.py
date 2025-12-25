from flask import Flask, request, jsonify
import joblib
import numpy as np
import datetime

app = Flask(__name__)

model = joblib.load("final_model.pkl")
MODEL_VERSION = "1.0"

EXPECTED_FEATURES = model.n_features_in_

@app.route("/")
def home():
    return "Student Performance Prediction"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json["features"]

    data = list(data)

    if len(data) < EXPECTED_FEATURES:
        data = data + [0] * (EXPECTED_FEATURES - len(data))
    else:
        data = data[:EXPECTED_FEATURES]

    data = np.array(data).reshape(1, -1)

    prediction = model.predict(data)[0]

    with open("prediction_logs.txt", "a") as f:
        f.write(str(datetime.datetime.now()) + "," + str(prediction) + "\n")

    return jsonify({
        "model_version": MODEL_VERSION,
        "prediction": float(prediction)
    })

if __name__ == "__main__":
    app.run(debug=True)
