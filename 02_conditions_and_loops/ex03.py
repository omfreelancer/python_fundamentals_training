#ask for 3 numbers
#check if number and reask
#calculate length by len()
#check if 3 numbers and re ask
#turn to list by list()
#turn each number to float
#append numbers to list
#use max and min
#print the result

while True:

    user_input = input("Enter 3 numbers seperated by spaces (e.g., 10 20 30): ").split()
    
    if len(user_input) != 3:

        print("Please enter 3 numbers seperated by spaces!")

        continue

    else:

        try:

            numbers = [float(part) for part in user_input]

            biggest_number = max(numbers)

            smallest_number = min(numbers)

            print(f"The biggest number is: {biggest_number:.2f}")
            print(f"The smallest number is {smallest_number:.2f}")

            break

        except ValueError:
            
            print("Invalid input. Enter numbers only (e.g., 34 50 60)")

                