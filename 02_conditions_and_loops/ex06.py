#ask user for a number
#check if it's number if not reask
#ask for how far the table should go(1-20)
#loop to the max number that user gave doing multiplications and print every time

while True:

    try:

        number = int(input("Enter a number: "))
        max_number = int(input("Enter the edge of the multiplacation table: "))
        

        if number < 1:
            
            print("The number should be at least 1.")
            continue

        if not (1 <= max_number <= 20):

            print("Please enter a table edge between 1 and 20.")
            continue

        print(f"\nThe multiplication table of {number}: ")

        for i in range(1,max_number+1):
                
            print(f"{number} x {i} = {number*i}")

        break

    except ValueError:

        print("Enter a number e.g., 9 , 8.")