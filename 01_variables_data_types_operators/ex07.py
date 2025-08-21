exam1 = float(input("Enter the 1st exam score: "))
exam2 = float(input("Enter the 2nd exam score: "))
exam3 = float(input("Enter the 3rd exam score: "))

average = (exam1 + exam2 + exam3) / 3

if average >= 90:
    print(f"Your average is {average:.2f} → Excellent")
elif average >= 75:
    print(f"Your average is {average:.2f} → Good")
elif average >= 50:
    print(f"Your average is {average:.2f} → Pass")
else:
    print(f"Your average is {average:.2f} → Fail")