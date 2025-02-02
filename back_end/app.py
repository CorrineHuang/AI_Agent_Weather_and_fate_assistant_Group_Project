from flask import Flask, request, jsonify, render_template
from models.deepseek_model import generate_analysis
from backend.bazi_logic import analyze_bazi
from backend.tarot_logic import analyze_tarot
import random

app = Flask(__name__)

# 🟢 Render the frontend page
@app.route("/")
def index():
    return render_template("index.html")

# 🟢 Handle Bazi Analysis Request
@app.route("/analyze_bazi", methods=["POST"])
def analyze_bazi_route():
    data = request.json
    gender = data.get("gender")
    birthdate = data.get("birthdate")
    birthplace = data.get("birthplace")

    if not birthdate or not birthplace:
        return jsonify({"error": "Please provide complete birth details."}), 400

    # Calculate Bazi information
    bazi_info = analyze_bazi(gender, birthdate, birthplace)

    # Generate personality analysis using DeepSeek AI
    analysis = generate_analysis(f"Based on Bazi principles, {bazi_info}. Please generate a detailed personality analysis and life advice.")

    return jsonify({"result": analysis})

# 🟢 Handle Tarot Card Analysis Request
@app.route("/analyze_tarot", methods=["POST"])
def analyze_tarot_route():
    data = request.json
    selected_card = data.get("selected_card")

    if not selected_card:
        return jsonify({"error": "Please select a Tarot card."}), 400

    tarot_info = analyze_tarot(selected_card)

    # Generate detailed Tarot reading using DeepSeek AI
    analysis = generate_analysis(f"You drew the {selected_card}. {tarot_info}. Please generate a detailed analysis of love, career, and financial aspects.")

    return jsonify({"result": analysis})

if __name__ == "__main__":
    app.run(debug=True)
