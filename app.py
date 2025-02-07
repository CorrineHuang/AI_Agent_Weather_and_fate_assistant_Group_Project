from flask import Flask, request, jsonify, render_template
from back_end.bazi import analyze_bazi
from back_end.tarot import analyze_tarot
from my_models.model import generate_analysis

app = Flask(__name__,template_folder="front_end/templates")

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
    # need to change 
    # Calculate Bazi information  
    year_element,year_animal,bazi_info = analyze_bazi(gender, birthdate, birthplace)
    
    # Generate personality analysis using DeepSeek AI
    analysis = generate_analysis(f"Based on traditional Chinese theories such as the I Ching (Yi Jing), Zhou Yi, and Zi Wei (Purple Star) astrology, if a person's information is {bazi_info}, please provide an analysis of their personality, career prospects, and life advice in English")

    return render_template('bazi_analysis_result.html', birth_date=birthdate, gender=gender, zodiac=year_animal, five_element = year_element,analysis=analysis)

@app.route('/tarot_card_reading')
def tarot_card_reading():
    return render_template('tarot_card_reading.html', tarot_cards=tarot_cards)

@app.route('/tarot_reading/<card_name>')
def get_card_info(card_name):
    if not card_name:
        return jsonify({"error": "Please select a Tarot card."}), 400

    tarot_info = analyze_tarot(card_name)

    # Generate detailed Tarot reading using DeepSeek AI
    analysis = generate_analysis(f"You drew the {card_name}. {tarot_info}. Please generate a detailed analysis of love, career, and financial aspects.")

    return jsonify({'card_name': card_name, 'card_description': tarot_info,'analysis': analysis})

if __name__ == "__main__":
    app.run(debug=True)
