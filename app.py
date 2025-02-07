from flask import Flask, request, jsonify, render_template
from back_end.bazi import analyze_bazi
from back_end.tarot import analyze_tarot
from my_models.model import generate_analysis

app = Flask(__name__,template_folder="front_end/templates",static_folder="front_end/static")

# Frontend
@app.route("/",methods =["GET","POST"])
def index():
    return render_template("index.html")

# Bazi page
@app.route('/bazi_analysis', methods=['GET'])
def bazi_analysis_form():
    return render_template('bazi_analysis.html')

# bazi result 
@app.route('/generate_bazi_analysis', methods=['POST'])
def generate_bazi_analysis():
    birthdate = request.form.get('birth_date')
    gender = request.form.get('gender')
    birthplace = request.form.get('birth_place')

    if not birthdate or not birthplace:
        return jsonify({"error": "Please provide complete birth details."}), 400
    # Calculate Bazi information  
    year_element,year_animal,bazi_info = analyze_bazi(gender, birthdate, birthplace)
    
    # Generate personality analysis using Google Gemini
    analysis = generate_analysis(f"Based on traditional Chinese theories such as the I Ching (Yi Jing), Zhou Yi, and Zi Wei (Purple Star) astrology, assume that my information is {bazi_info}, please provide an analysis of their personality, career prospects, and life advice in English and in 100 words.Answers should be straight forward, do not start with Okay,Here,sure.")

    return render_template('bazi_analysis_result.html', birth_date=birthdate, gender=gender, zodiac=year_animal, five_element = year_element,analysis=analysis)

tarot_cards = {
    "The Fool": "Symbolizes new beginnings, freedom, and adventure.",
    "The Magician": "Represents creativity, intelligence, and control.",
    "The High Priestess": "Symbolizes intuition, subconscious, and wisdom.",
    "The Empress": "Symbolizes nurturing, love, and creativity.",
    "The Emperor": "Symbolizes power, stability, and responsibility.",
    "The Lovers": "Represents love, relationships, and choices.",
    "The Chariot": "Represents willpower, victory, and progress.",
    "The Hermit": "Symbolizes introspection, wisdom, and solitude.",
    "Wheel of Fortune": "Represents destiny, cycles, and changes."
}

@app.route('/tarot_card_reading')
def tarot_card_reading():
    return render_template('tarot_card_reading.html', tarot_cards=tarot_cards)

@app.route('/tarot_reading/<card_name>')
def get_card_info(card_name):
    if not card_name:
        return jsonify({"error": "Please select a Tarot card."}), 400

    tarot_info = analyze_tarot(card_name)

    # Generate detailed Tarot reading using Google Gemini
    analysis = generate_analysis(f"According to Tarot theory, the card {card_name}: {tarot_info}. Please generate a detailed analysis of love, career, and financial aspects in 10-20 words.Answers should be straight forward, do not start with Okay,Here,sure.")

    return jsonify({'card_name': card_name, 'card_description': tarot_info,'analysis': analysis})

if __name__ == "__main__":
    app.run(debug=True)
