from datetime import date

current_year = date.today().year

birth = int(input("Type the year of your birth: "))
age = current_year - birth

print(f"You are {age} years old.")