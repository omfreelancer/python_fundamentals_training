    # Function max_of_three(num1, num2, num3)
# If num1 >= num2 and num1 >= num3 → return num1.
# Else if num2 >= num1 and num2 >= num3 → return num2.
# Else → return num3.
    # Main program
# Ask the user for 3 numbers (int or float).
# Validate inputs.
# Call max_of_three(num1, num2, num3).
# Print result in the format

def max_of_three(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
    
while True:
    try:
        num1 = float(input("Enter a number:" ))
        num2 = float(input("Enter a second number:" ))
        num3 = float(input("Enter a third number:" ))

        largest = max_of_three(num1,num2,num3)
        print(f"The largest number among {num1:g}, {num2:g}, and {num3:g} is {largest:g}")

        option = input("Enter 'c' to enter new numbers or 'q' to quit the program: ").strip().lower()
        while option not in ("q","c"):
            print("Invalid input. Enter either 'c' to continue or 'q' to quit.")
            option = input("Enter 'c' to enter new numbers or 'q' to quit the program: ").strip().lower()
        if option == "q":
            break
            
    except ValueError:
        print("Enter a number (e.g., 3.5).")