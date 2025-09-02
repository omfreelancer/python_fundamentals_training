#ask the user a number
#check if it's a number
#check if it is > 1
#loop and look if any number from 2 to n the remainder is 0 n%2 , n%3 ... 
#print the result

while True:
    try:
        n = int(input("Enter a number: "))

        if n <= 1:

            print(f"{n} is not a prime number.")

            break

        if n == 2:

            print("2 is a prime number.")

            break

        for i in range(2, int(n ** 0.5) + 1):

            result = n % i

            if result == 0:

                print(f"{n} is not a prime number.")

                break
        else:
            
            print(f"{n} is a prime number.")

            break

    except ValueError:

        print("Enter a number (e.g., 12).")
