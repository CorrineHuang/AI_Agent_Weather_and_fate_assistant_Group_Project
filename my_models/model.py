# Google Gemini 
from google import genai
import re 

def generate_analysis(prompt, api_key):
    client = genai.Client(api_key= [your_api_key:you need to change me here])
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents= prompt
    )
    formatted_response = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', response.text)
    formatted_response = re.sub(r"^(Okay,? here:?|Sure,? here:?|Here.*?:)\s*", "", formatted_response, flags=re.IGNORECASE).strip()
    return formatted_response

if __name__ =="__main__":
    #prompt =  f"Based on traditional Chinese theories such as the I Ching (Yi Jing), Zhou Yi, and Zi Wei (Purple Star) astrology, if a person's information is female ,birthday 1993-09-07,birthplace is beijing, please provide an analysis of their personality, career prospects, and life advice in 200 words. Answers should be straight forward, do not start with Okay,Here."
    prompt =  f"Analyze the personality, career prospects, dominant Five Element (Wu Xing) influences, and fortune for 2025 of a person based on traditional Chinese metaphysics, including the I Ching (Yi Jing), Zhou Yi, Zi Wei Dou Shu (Purple Star Astrology), and the Five Elements. The person's information is female ,birthday 1993-09-07,birthplace is beijing. Provide a concise yet insightful reading within 200 words, avoiding unnecessary introductions or explanations. The response should be written as a single, well-structured paragraph that seamlessly integrates personality traits, career tendencies, Five Element balance, and key opportunities and challenges in 2025, offering meaningful life guidance in a direct and practical manner."
    print(generate_analysis(prompt))
    
