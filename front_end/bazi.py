def analyze_bazi(gender, birthdate, birthplace):
    year, month, day = map(int, birthdate.split("-"))

    year_element = ["Wood", "Fire", "Earth", "Metal", "Water"][year % 5]
    year_animal = ["Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"][year % 12]

    return f"Your Bazi element is {year_element}, and your zodiac sign is {year_animal}.",year_element,year_animal
