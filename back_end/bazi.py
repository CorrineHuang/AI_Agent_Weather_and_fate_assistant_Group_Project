def analyze_bazi(gender, birthdate, birthplace):
# birthdata format: need to check with front end.
    year, month, day = map(int, birthdate.split("-"))
    year_element = ["Wood", "Fire", "Earth", "Metal", "Water"][(year-4) % 5]
    year_animal = ["Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"][(year-4) % 12]

    bazi_info =  f'''
    The people's information is:
    Gender:{gender};
    Birthday:{birthdate} in solar calender;
    Birth place is in {birthplace}'''
    return year_element,year_animal,bazi_info

if __name__=="__main__":
    print(analyze_bazi('female','1997-08-09','Singapore'))