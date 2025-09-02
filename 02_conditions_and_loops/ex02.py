#ask for a year
#check is it a number and re ask if not
#if divide by 4 look if divide by 100 and 400 ==> leap
#if not divide by 4 ==> not leap 

while True:
    year = input("Eter a year: ")
    try:
        year = int(year)

        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 :

            print(f"The year {year} is a leap year.")
        
        else:
            print(f"The year {year} is not a leap year.")
        
        break

    except ValueError:

        print("Enter a number e.g., 1978.")