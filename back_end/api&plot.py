# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 16:09:26 2025

@author: 嘤嘤
"""

import requests

# 替换为你的 OpenWeatherMap API 密钥
API_KEY = '46fa3d6db66fac5c21a055e7171b052a'

url = f"https://api.openweathermap.org/data/2.5/weather?q=Singapore&appid={API_KEY}"

response = requests.get(url)

# 检查响应状态码
if response.status_code == 200:
    print("API 密钥有效！")
    weather_data = response.json()
    print("天气数据：", weather_data)
else:
    print("API 密钥无效或尚未生效。")
    print("错误信息：", response.text)
#%%
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Singapore 2025-01-28 to 2025-02-15.csv")

df['datetime'] = pd.to_datetime(df['datetime'])

plt.figure(figsize=(12, 6))

plt.plot(df['datetime'], df['temp'], label='avg temperature', marker='o', color='blue')
plt.plot(df['datetime'], df['feelslike'], label='avg feellike temperature', marker='o', color='orange')
plt.title('Singapore avg temperature and feellike temperature from 2025-01-28 to 2025-02-15')
plt.xlabel('date')
plt.ylabel('Temperature (℃)')
plt.legend()

plt.xticks(rotation=45)
plt.grid(True)

plt.show()