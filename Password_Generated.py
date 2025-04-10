import string
import random

def generate_password(min_length, numbers=True, special_characters=True):
    s1 = string.ascii_letters
    s2 = string.digits
    s3 = string.punctuation
    
    characters = s1
    if numbers:
        characters += s2
    if special_characters:
        characters += s3
    
    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False
    
    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char
        
        if new_char in s2:
            has_number = True
        elif new_char in s3:
            has_special = True
        
        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special
    
    return pwd

# Predefined values to avoid I/O error in sandboxed environments
default_min_length = 12
default_has_number = True
default_has_special = True

try:
    min_length = default_min_length
    has_number = default_has_number
    has_special = default_has_special
    
    pwd = generate_password(min_length, has_number, has_special)
    print("Your password is:", pwd)
except ValueError as e:
    print("Invalid input:", e)
except OSError as e:
    print("I/O error occurred:", e)
