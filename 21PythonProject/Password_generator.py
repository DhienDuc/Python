import random
import string

def password_generator(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    specials = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += specials

    pwd = ""
    meet_criteria = False
    has_number = False
    has_special = False

    while  not meet_criteria or len(pwd) < min_length:
        char = random.choice(characters)
        pwd += char

        if char in digits:
            has_number = True
        if char in specials:
            has_special = True

        meet_criteria = True
        if numbers:
            meet_criteria = has_number
        if special_characters:
            meet_criteria = meet_criteria and has_special
        
    return pwd

pwd = password_generator(3)
print(f"Your random password:[{pwd}]")
