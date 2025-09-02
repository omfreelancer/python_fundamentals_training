#ask user for a positive integer n
#check if it's a number if not reask
#check if n>0 if not reask
#use for range(1,n+1) and calculate
#print the result

while True:
    try:
        n = int(input("Enter a positive number: "))

        if n < 0:
            print("number must be 0 or greater.")
            continue

        f = 1
        formula_list = []
        
        for i in range(1, n+1):

            f *= i
            formula_list.append(str(i))

        if n == 0:

            print("0! = 1")

        else:

            formula_str = "*".join(formula_list)

            print(f"{n}! = {formula_str} = {f}")

        break

    except ValueError:
        print("Enter a number e.g., 7.")