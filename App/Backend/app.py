from flask import Flask, jsonify
from flask_cors import CORS
import os
import json

app = Flask(__name__)
CORS(app)  # 🔥 Allows React to fetch data

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
RESULTS_FILE = os.path.join(DATA_DIR, "results.json")
EVENTS_FILE = os.path.join(DATA_DIR, "events.json")  # or CSV later

@app.route("/")
def home():
    return jsonify({"message": "Brent Oil Change Point API is running."})

@app.route("/api/change-point", methods=["GET"])
def get_change_point():
    if not os.path.exists(RESULTS_FILE):
        return jsonify({"error": "results.json not found"}), 404
    with open(RESULTS_FILE, "r") as file:
        data = json.load(file)
    return jsonify(data)

@app.route("/api/events", methods=["GET"])
def get_events():
    if not os.path.exists(EVENTS_FILE):
        return jsonify({"error": "events.json not found"}), 404
    with open(EVENTS_FILE, "r") as file:
        events = json.load(file)
    return jsonify(events)

if __name__ == "__main__":
    app.run(debug=True)
