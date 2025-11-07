# take first number with try except and loop until it's a float
# take the operator (+, -, *, /) loop until it's valid
# take second number with try except and loop until it's a float
# result = firstnumber operator secondnumber
# use try exept for division by zero
# print the result nicely


def is_number(n):
    try:
        return float(n)
    except ValueError:
        return None
    
def plus(n1,n2):
    return n1 + n2

def minus(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    try:
        return n1 / n2
    except ZeroDivisionError:
        return None
    
actions = {
        "+": plus,
        "-": minus,
        "*": multiply,
        "/": divide,
    }
    
while (first_value := is_number(first_number := input("Enter first number: ").strip())) is None:
    print("Invalid number. Please try again.")
first_number = first_value

while (operator := input("Enter operator(+, -, *, /): ").strip()) not in ("+","-","*","/"):
    print("Invalid operator. Please choose one of +, -, *, /.")

while True:
    second_number = input("Enter second number: ").strip()
    second_number = is_number(second_number)
    if second_number is None:
        print("Invalid number. Please try again.")
        continue

    action = actions[operator]
    result = action(first_number,second_number)

    if result is None:
        print("Cannot divide by zero. Try again.")
        continue

    print(f"Result: {first_number:g} {operator} {second_number:g} = {result:.2f}")
    break