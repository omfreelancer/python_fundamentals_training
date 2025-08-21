digits = int(input("Enter a 3-digit number: "))

if digits >= 100 and digits <= 999:
    num1 = digits // 100
    num2 = (digits // 10) % 10
    num3 = digits % 10

    print(f"{num1} + {num2} + {num3} = {num1+num2+num3}")
else:
    print("Enter a three-digit number")