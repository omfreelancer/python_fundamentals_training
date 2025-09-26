    #function add(a,b):
#return a + b
    #function substract(a, b):
#return a - b
    #function multiply(a, b):
#return a * b
    #function divide(a, b):
#if b == 0 return None
#else return a / b
    #Main program
#ask user for two numbers
#ask for an operator
#if operator not within (+,-,/,*) print invalid input and reask
#call the right function
#return the result
#if result is none print("Error: Cannot divide by zero")
#ask if user want to continue or quit

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return None
    return a / b

while True:
    try:
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter a second number: "))

        ops ={"+":add, "-":subtract, "*":multiply, "/":divide}
        operator = input('Enter an operator ("/","+","-","*"): ').strip()

        if operator not in ops:
            print('Invalid operator. choose between: "/","+","-","*" ')
            continue

        func = ops[operator]
        result = func(num1, num2)

        if result is None:
            print("Error: Cannot divide by zero.")

        else:
            print(f"{num1:g} {operator} {num2:g} = {result:.10g}")

        option = input("Enter 'c' to continue or 'q' to quit: ").strip().lower()
        while not option in ("c","q"):
            print("Invalid input!")
            option = input("Enter 'c' to continue or 'q' to quit: ").strip().lower()
        
        if option == "q":
            break

    except ValueError:
        print("Enter a number (e.g., 7)")