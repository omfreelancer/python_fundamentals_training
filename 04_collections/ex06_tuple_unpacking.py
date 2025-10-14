#ask user to enter three values seperated by comma use re.split
#convert the list to a tuple
#unpack and print
#swap two values and print them

import re

user_input = input("Enter your name, age and country seperated by comma: ")

items_tuple = tuple(item.strip() for item in re.split(r'[,\s]+',user_input) if item)

if len(items_tuple) != 3:
    print(f"Invalid input. Expected 3 values, got {len(items_tuple)}.")
    exit()
else:
    print("Packed tuple:", items_tuple)

    name, age, country = items_tuple
    print("\nUnpacked")
    print("Name:",name)
    print("Age:",age)
    print("Country:",country)

    age, country = country, age
    new_tuple = (name, age, country)
    print("\nAfter swapping using tuple unpacking:")
    print(new_tuple)