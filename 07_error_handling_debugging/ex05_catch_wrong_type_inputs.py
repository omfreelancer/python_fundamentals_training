# loop and ask for first number until it's valid
# loop and ask for second number until it's valid
# compute the total = first number + second number
# print the result nicely print(result : firstnumber + secondnumber = total)

def is_number(n):
    try:
        return float(n)
    except ValueError:
        return None

def get_number(prompt):
    while (n := is_number(number := input(prompt).strip())) is None:
        print("Invalid input. Please enter a valid number.")
    return n
    
n1 = get_number("Enter first number: ")
n2 = get_number("Enter second number: ")

result = n1 + n2

print(f"Sum: {n1:g} + {n2:g} = {result:g}")