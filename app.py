from flask import Flask, request, jsonify
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load models and datasets from 'models/' folder
kmeans = joblib.load("models/kmeans_model.pkl")
scaler = joblib.load("models/scaler.pkl")
cluster_profile = joblib.load("models/cluster_profile.pkl")
cluster_insights = joblib.load("models/cluster_insights.pkl")
elasticity_summary = joblib.load("models/elasticity_summary.pkl")
price_simulations = joblib.load("models/price_simulations.pkl")

@app.route("/")
def home():
    return {"message": "LG Customer Segmentation & Pricing API is running!"}

@app.route("/predict", methods=["POST"])
def predict():
    """
    Predict customer cluster based on input features.
    Example JSON:
    {
        "features": [34, 45000, 70, 0.85]
    }
    """
    try:
        data = request.json
        features = np.array(data["features"]).reshape(1, -1)
        features_scaled = scaler.transform(features)
        cluster = kmeans.predict(features_scaled)[0]
        return {"cluster": int(cluster)}
    except Exception as e:
        return {"error": str(e)}

@app.route("/cluster_profile/<int:cluster_id>", methods=["GET"])
def get_cluster_profile(cluster_id):
    """Get profile details for a specific cluster."""
    try:
        profile = cluster_profile.loc[cluster_id].to_dict()
        return jsonify(profile)
    except Exception as e:
        return {"error": str(e)}

@app.route("/cluster_insights", methods=["GET"])
def get_cluster_insights():
    """Get general cluster insights."""
    try:
        return jsonify(cluster_insights.to_dict())
    except Exception as e:
        return {"error": str(e)}

@app.route("/elasticity", methods=["GET"])
def get_elasticity():
    """Get price elasticity summary."""
    try:
        return jsonify(elasticity_summary.to_dict())
    except Exception as e:
        return {"error": str(e)}

@app.route("/simulate_price", methods=["POST"])
def simulate_price():
    """
    Run price simul
