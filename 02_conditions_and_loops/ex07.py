#ask the user for a positive number n 
#check if n>0 and if not reask
#use for range (0,n+1,2) for even numbers and add them to a list 
#use for range (1,n+1,2) for odd numbers and add them to a list 
#calculate sum(list) and print the result 

while True:

    try:

        number = int(input("Enter a positive number: "))

        if not number > 0:

            print("Number must be at least be 1.")
            continue

        even, odd = [], []
        
        sum_even = 0
        sum_odd = 0

        for i in range(2,number+1,2):

            even.append(str(i))
            sum_even += i

        for i in range(1,number+1,2):

            odd.append(str(i))
            sum_odd += i

        even_str = "+".join(even) if even else "0"
        odd_str = "+".join(odd) if odd else "0"

        print(f"Even sum: {even_str} = {sum_even}")
        print(f"Odd sum: {odd_str} = {sum_odd}")

        break

    except ValueError:

        print("Enter a number e.g., 12.")