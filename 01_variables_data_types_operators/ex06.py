num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Choose an operator (* / + -): ")

if operator == "*":
    print(f"{num1} {operator} {num2} = {num1 * num2}")
elif operator == "/":
    if num2 != 0:
        print(f"{num1} {operator} {num2} = {num1 / num2:.2f}")
    else:
        print("Error: can't divide by zero.")
elif operator == "+":
    print(f"{num1} {operator} {num2} = {num1 + num2}")
elif operator == "-":
    print(f"{num1} {operator} {num2} = {num1 - num2}")
else:
    print("Invalid operator!")