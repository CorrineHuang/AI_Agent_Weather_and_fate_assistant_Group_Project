# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 21:04:50 2025

@author: 嘤嘤
"""

def recommend_outfit(temp):
    if 0 <= temp < 5:
        outfit = "Thick coat, Sweater"
        food = "Hot soup, Hot chocolate"
    elif 5 <= temp < 10:
        outfit = "Jacket, Scarf"
        food = "Hot tea, Roasted sweet potato"
    elif 10 <= temp < 15:
        outfit = "Trench coat, Thick sweater"
        food = "Sandwich, Hot porridge"
    elif 15 <= temp < 20:
        outfit = "Thin sweater, Denim jacket"
        food = "Light salad, Fruit"
    elif 20 <= temp < 25:
        outfit = "Short-sleeved shirt, Thin coat"
        food = "Cold noodles, Yogurt"
    elif 25 <= temp < 30:
        outfit = "Short-sleeved shirt, Shorts"
        food = "Ice cream, Iced tea"
    elif 30 <= temp < 35:
        outfit = "Thin short-sleeved shirt, Sun hat"
        food = "Ice cream, Iced watermelon"
    elif 35 <= temp < 40:
        outfit = "Ultra-thin short-sleeved shirt, Sun umbrella"
        food = "Slush, Iced lemonade"
    else:
        outfit = "Unknown recommendation"
        food = "Unknown recommendation"
    
    return outfit, food

temp = 28 
outfit, food = recommend_outfit(temp)
print(f"For a temperature of {temp} degrees, recommend wearing: {outfit} and eating/drinking: {food}")