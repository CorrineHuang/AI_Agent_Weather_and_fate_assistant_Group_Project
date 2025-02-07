# Google Gemini 
# AIzaSyCKJTExnt8gIGuzy6Z9EznVKzamlI8own4
from google import genai
import re 

def generate_analysis(prompt, api_key="AIzaSyCKJTExnt8gIGuzy6Z9EznVKzamlI8own4"):
    client = genai.Client(api_key= api_key)
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents= prompt
    )
    formatted_response = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', response.text)
    formatted_response = re.sub(r"^(Okay,? here:?|Sure,? here:?|Here.*?:)\s*", "", formatted_response, flags=re.IGNORECASE).strip()
    return formatted_response

if __name__ =="__main__":
    prompt =  f"Based on traditional Chinese theories such as the I Ching (Yi Jing), Zhou Yi, and Zi Wei (Purple Star) astrology, if a person's information is female ,birthday 1993-09-07,birthplace is beijing, please provide an analysis of their personality, career prospects, and life advice in 200 words. Answers should be straight forward, do not start with Okay,Here."

    print(generate_analysis(prompt))
    


# This API has a limit .
# import requests
# import json

# # For now , it's the API key of kun.
# def generate_analysis(prompt, api_key="sk-206.1qf2vKdOEVDAF1aNLPUvyGOUGAKqD7lorVh6OuKwzVKTAlZO", model="deepseek-r1"):
#     """Send a request to the API and return only the generated content."""
#     url = "https://wcode.net/api/gpt/v1/chat/completions"
    
#     payload = json.dumps({
#         "model": model,
#         "messages": [
#             {"role": "system", "content": "You are a helpful assistant."},
#             {"role": "user", "content": prompt}
#         ]
#     })
    
#     headers = {
#         'Content-Type': 'application/json',
#         'Authorization': f'Bearer {api_key}' 
#     }
    
#     response = requests.post(url, headers=headers, data=payload)
    
#     if response.status_code == 200:
#         return response.json().get("choices", [{}])[0].get("message", {}).get("content", "")
#     else:
#         return "Error: Request failed with status code " + str(response.status_code)

# if __name__ =="__main__":
#     api_key = "sk-206.1qf2vKdOEVDAF1aNLPUvyGOUGAKqD7lorVh6OuKwzVKTAlZO" 
#     prompt = "Hello, who are you?"
#     result = generate_analysis(prompt, api_key)
#     print(result)


# we have no chane to buy deepseek API so that we can use deepseek.
# from openai import OpenAI

# client = OpenAI(api_key="", base_url="https://api.deepseek.com")

# response = client.chat.completions.create(
#     model="deepseek-chat",
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant"},
#         {"role": "user", "content": "Hello"},
#     ],
#     stream=False
# )

# print(response.choices[0].message.content)


