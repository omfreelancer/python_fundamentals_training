    # Function is_prime(n)
# If n <= 1 → return False.
# If n == 2 → return True.
# If n is even → return False.
# Loop from 3 to √n (inclusive), step = 2:
# If n % i == 0 → return False.
# Return True.
    # Function primes_in_range(start, end)
# Initialize empty list primes.
# Loop from start to end inclusive:
# If is_prime(number) → append to primes.
# Return primes.
    # Main program
# Ask for start and end.
# Validate both inputs are integers and start <= end.
# Call primes_in_range(start, end).
# If result is empty → print "No prime numbers in this range.".
# Else → print primes comma-separated.

def is_prime(n):
    if n <= 1:
        return False
    
    if n == 2:
        return True
    
    if n % 2 == 0:
        return False

    else:
        limit = int(n ** 0.5)
        for i in range(3,limit+1,2):
            if n % i == 0:
                return False
        
        return True
        
def primes_in_range(start, end):
    
    return [i for i in range(start,end+1) if is_prime(i)]

while True:

    try: 
        start = int(input("Enter your start number range: "))
        end = int(input("Enter your end number range: "))

        if end < start:
            print("End number must be greater than or equal to start number.")
            continue

        print(f"Searching for prime numbers betwen {start} and {end} ...")

        result = primes_in_range(start,end)

        if result:
            print("Prime numbers:",", ".join(map(str,result)))
            break
        else:
            print("No prime numbers in this range.")
            break
    except ValueError:
        print("Invalid input. Enter a number(e.g., 9)")