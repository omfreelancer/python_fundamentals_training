#ask the user for their age
#check if it's a number if not reask
#check if age>0 if not reask
#If age < 18 → print “Not eligible for a driving license.” 
#If 18 ≤ age < 70 → print “Eligible for a driving license.” 
#If age ≥ 70 → print “Eligible, but requires a medical check.” 

while True:

    age = input("How old are you?: ")

    try:
        age = int(age)

        if age > 0:

            if age < 18:

                print('Not eligible for a driving license.')
                break

            elif age >= 18 and age <70:

                print("Eligible for a driving license.")
                break

            elif age >= 70:

                print("Eligible, but requires a medical check.")
                break

        else:

            print("Age must be greater than 0.")
            continue

    except ValueError:
        print("Enter a number (e.g., 25)")