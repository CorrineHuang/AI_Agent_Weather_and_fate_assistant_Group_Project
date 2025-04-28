# 🌦️🔮 Weather and Fate Assistant

> A Python-based desktop application combining real-time weather forecasts with daily fortune messages to provide users with both practical information and inspirational guidance.

---

## 📚 Project Overview

**Weather and Fate Assistant** is a desktop application developed in Python.  
It allows users to access **current weather information** and receive **randomized daily fortune messages** from a single user-friendly interface.  
The application integrates weather data retrieval via API and random fortune generation to enhance users' everyday experience.

---

## 🧰 Features

- **Real-time Weather Lookup**:  
  Input a city name to retrieve up-to-date weather conditions, temperature, humidity, and more.
  
- **Daily Fortune Generator**:  
  Generate a motivational or insightful fortune message each day.

- **Graphical User Interface (GUI)**:  
  Built with Tkinter for a clean, easy-to-use desktop interface.

- **Multi-language Support**:  
  Supports both English and Chinese interfaces.

---

## 🗂️ Project Structure

```
Weather_and_fate_assistant_Group_Project/
├── main.py                 # Main entry point for launching the application
├── weather_module.py       # Module handling weather data retrieval
├── fate_module.py          # Module generating random fortune messages
├── gui.py                  # Module building the Tkinter GUI
├── requirements.txt        # List of required Python packages
└── README.md               # Project documentation
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/CorrineHuang/Weather_and_fate_assistant_Group_Project.git
cd Weather_and_fate_assistant_Group_Project
```

### 2. Get and put you API key in Model.py
The place is [your_api_key:you need to change me here]
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python main.py
```


## 📊 Technologies Used

- **Programming Language**: Python 3.x
- **GUI Framework**: Tkinter
- **Weather API**: OpenWeatherMap API
- **Libraries**: requests, json, random

---

## 🧪 API Endpoints (if any)

This is a local desktop application and does not expose external API endpoints.  
However, it **calls OpenWeatherMap's public API** internally to fetch real-time weather data.

---


