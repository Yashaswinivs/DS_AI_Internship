from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load model
model = pickle.load(open("model.pkl", "rb"))

# Home route
@app.route("/")
def home():
    return "Flask API is running!"

# Prediction route
@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    
    features = np.array(list(data.values())).reshape(1, -1)
    
    prediction = model.predict(features)
    
    return jsonify({
        "prediction": prediction.tolist()
    })

# Run app
if __name__ == "__main__":
    app.run(debug=True)