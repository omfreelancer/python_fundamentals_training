# import math
# show the menu (1–5) of operations
# ask the user to choose an option
# validate the choice (must be one of 1–5)

# if choice == 1 (square root)
#     ask for a number
#     if number is negative number, print error
#     result = math.sqrt(number)

# elif choice == 2 (factorial)
#     ask for a number
#     if number is negative or not integer, print error
#     else result = math.factorial(number)

# elif choice in (3, 4, 5):  # sine, cosine, tangent
#     ask for angle in degrees
#     convert degrees → radians using math.radians()
#     compute the chosen trig function

# print the result nicely (formatted number)

import math

def show_menu():
    print("""Choose operation:
1) Square root
2) Factorial
3) Sine
4) Cosine
5) Tangent""")
    
def is_number(n):
    try:
        return float(n)
    except ValueError:
        return None

menu = ("1","2","3","4","5")
names = {"1": "√", "2": "factorial", "3": "sin", "4": "cos", "5": "tan"}
trig_actions = {"3":math.sin,"4":math.cos,"5":math.tan}

while True:
    print()
    show_menu()
    choice = input("\nEnter a choice (1-5): ").strip()
    if choice not in menu:
        print("Invalid input. Enter a valid number (1-5).")
    else:
        break

while True:
    number = input("Enter a number: ").strip()
    n = is_number(number)
    if n is None:
        print("Invalid number. Enter a valid number.")
        continue
    if choice == "1":
        if n >= 0:
            result = math.sqrt(n)
            break
        else:
            print("Invalid input. Square root requires a positive number.")
            continue
    elif choice == "2":
        if n.is_integer() and n >= 0:
            result = math.factorial(int(n))
            break
        else:
            print("Invalid input. Factorial requires a positive integer (e.g., 15).")
            continue
    else:
        radian = math.radians(n)
        result = trig_actions[choice](radian)
        break

print(f"Result {names[choice]}({number}) = {result:5f}")