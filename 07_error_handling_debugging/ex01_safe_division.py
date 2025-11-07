# ask for numerator 
# use try/except to convert it to float and keep asking until you get a correct number
# ask for denominator
# use try/except to convert to float and keep asking until you get a correct number
# we can check with if statement if the denominator is 0
# Or use try/except and make the operation numenator/denominator and catch the error
# print a message and keep asking until you get a denominator > 0

while True:
    try:
        numerator = float(input("Enter the numerator: ").strip())
        print()
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.\n")

while True:
    try:
        denominator = float(input("Enter the denominator: ").strip())
        
        if denominator == 0:
            print("Cannot divide by zero\n")
            continue

        result = numerator / denominator
        print(f"\n{numerator} ÷ {denominator} = {result:.2f}")
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.\n")