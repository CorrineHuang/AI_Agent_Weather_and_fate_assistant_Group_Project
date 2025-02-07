from flask import Flask, request, jsonify, render_template
#from model.deepseek_model import generate_analysis
from model import generate_analysis
from bazi import analyze_bazi
from tarot import tarot_cards,analyze_tarot
#from tarot import analyze_tarot
import random

app = Flask(__name__)

# 🟢 Render the frontend page
@app.route("/",methods =["GET","POST"])
def index():
    return render_template("index.html")

# 🟢 Handle Weather Data Request
@app.route("/api/weather", methods=["GET"])
def get_weather_data():
    country = request.args.get("country", "Singapore")
    try:
        df = pd.read_excel(csv_file,header=1)
        data=df.iloc[1:]
        country_data = data[data["name"] == country]
        latest_record = country_data.iloc[-1].to_dict()
        
        # Get time-series data
        timeseries = country_data[["datetime", "temp"]].rename(columns={"datetime": "Date", "temp": "Temperature"}).to_dict(orient="records")

        response = {
            "Country": latest_record["name"],
            "Date": latest_record["datetime"],
            "Temperature": latest_record["temp"],
            "Humidity": latest_record["humidity"],
            "AirQuality": latest_record["visibility"],
            "timeseries": timeseries
        }
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/bazi_analysis', methods=['GET'])
def bazi_analysis_form():
    return render_template('bazi_analysis.html')

@app.route('/generate_bazi_analysis', methods=['POST'])
def generate_bazi_analysis():
    birthdate = request.form.get('birth_date')  # 'YYYY-MM-DD'
    gender = request.form.get('gender')
    birthplace = request.form.get('birth_place')

    if not birthdate or not birthplace:
        return jsonify({"error": "Please provide complete birth details."}), 400

    # Calculate Bazi information  
    bazi_info,year_element,year_animal = analyze_bazi(gender, birthdate, birthplace)
    
    # Generate personality analysis using DeepSeek AI
    analysis = generate_analysis(f"Based on Bazi principles, {bazi_info}. Please generate a detailed personality analysis and life advice.")

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
    app.run()
