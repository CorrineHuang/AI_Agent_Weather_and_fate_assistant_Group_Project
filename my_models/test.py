# from model import generate_analysis

# prompt = "What is the meaning of life?"
# response = generate_analysis(prompt)
# print(response)

import requests
import json

url = "https://wcode.net/api/gpt/v1/chat/completions"

payload = json.dumps({
  "model": "deepseek-r1",
  "messages": [
    {
      "role": "system",
      "content": "You are a helpful assistant."
    },
    {
      "role": "user",
      "content": "你好，请介绍一下你自己"
    }
  ]
})

headers = {
  'Content-Type': 'application/json',
  'Authorization': 'sk-206.1qf2vKdOEVDAF1aNLPUvyGOUGAKqD7lorVh6OuKwzVKTAlZO'  
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)