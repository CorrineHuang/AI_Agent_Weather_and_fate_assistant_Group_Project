import requests
import json

def generate_analysis(prompt, api_key, model="deepseek-r1"):
    """Send a request to the API and return only the generated content."""
    url = "https://wcode.net/api/gpt/v1/chat/completions"
    
    payload = json.dumps({
        "model": model,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    })
    
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}' 
    }
    
    response = requests.post(url, headers=headers, data=payload)
    
    if response.status_code == 200:
        return response.json().get("choices", [{}])[0].get("message", {}).get("content", "")
    else:
        return "Error: Request failed with status code " + str(response.status_code)

if __name__ =="__main__":
    api_key = "sk-206.1qf2vKdOEVDAF1aNLPUvyGOUGAKqD7lorVh6OuKwzVKTAlZO" 
    prompt = "Hello, who are you?"
    result = generate_analysis(prompt, api_key)
    print(result)




