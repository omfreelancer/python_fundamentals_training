# Define function factorial(n):
    # Start with result = 1.
    # Loop from 1 to n (inclusive), multiplying into result.
    # Return result.
# Main program:
    # Ask the user for a number.
    # Validate it (must be integer ≥ 0).
    # Call factorial(n) and print n! = result.

def factorial(n):

    result = 1
    if n >= 0:
        for i in range(1,n+1):
            result *= i
        return result
    
    else:
        return None
    
while True:
    
    try:
        n = int(input("Enter a non negative integer: "))
        fact = factorial(n)

        if fact == None:
            print("Factorial is not defined for negative numbers.")
            continue

        else:
            print(f"{n}! = {fact}")
            break

    except ValueError:
        print("Enter a valid integer (e.g., 13).")