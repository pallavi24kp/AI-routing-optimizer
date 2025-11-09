from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('routing_model.pkl')

@app.route('/')
def home():
    return "AI Routing Path Optimizer API"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = np.array([
        data['latency_ms'],
        data['bandwidth_mbps'],
        data['traffic_load'],
        data['hop_count']
    ]).reshape(1, -1)
    
    prediction = model.predict(features)[0]
    return jsonify({'predicted_score': round(prediction, 2)})

if __name__ == '__main__':
    app.run(debug=True)
