
user_name = input("What is your name?")
print("Hello, " + user_name + "!")
age_text = input("How old are you?")
age_number = int(age_text) # Превратили текст в число!
сity_text = input("What city do you live in?")
birth_year = 2026 - age_number
print(f"Hello, {user_name}! You are {age_number} years old and you live in {city_text}. So you were born around {birth_year}.")