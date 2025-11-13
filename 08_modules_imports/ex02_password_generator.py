# import string and random
# make a list of digits and puntuations and letters
# ask user for the desired password length.
# validate the user input is an integer >= 4 re ask if not
# use random.sample to chose random combination and the necessary length

import random, string

combination = string.ascii_letters + string.punctuation + string.digits

def is_number(n):
    try:
        return int(n)
    except ValueError:
        return None
    
def create_password(n):
    password = ""
    for _ in range(n):
        password += random.choice(combination)
    return password

while True:
    user_input = input("Enter password length: ").strip()
    if (n := is_number(user_input)) is None:
        print("Invalid input. Please enter a valid number.")
        continue
    if n < 4:
        print("Invalid length. Please enter a positive number greater or equal 4.")
        continue
    break

password = create_password(n)

print(f"Generated password: {password}")