# import json and create dic data = {}
# ask user for how many entries he'll enter
# use a loop based on user input and ask for key and value
# make sure key is not empty if not give a message and reask
# save all that to data
# save data to data.json
# load data and print it

import json
data = {}    

while True:
    try:
        number = int(input("How many entries?: "))
        break
    except ValueError:
        print("Enter an integer (e.g., 3)")

if number == 0:
    print("No entries to save. Creating an empty JSON file...")

if number > 0:

    for i in range(1,number+1):
        while not (key := input(f"Key #{i}: ").strip()):
            print("Empty input is not valid.")
        value = input(f"Value #{i}: ")
        
        if value.isdigit():
            value = int(value)
        elif value.replace(".", "", 1).isdigit():
            value = float(value)
        data[key] = value

try:
    with open("data.json","w") as file:
        json.dump(data, file, indent=4)
    print("Saved to data.json ✅")
except Exception as e:
    print("An error occurred:",e)

try:
    with open("data.json","r") as file:
        loaded_data = json.load(file)
    print("Loaded from data.json:", json.dumps(loaded_data, indent=4))

except Exception as e:
    print("An error occurred:",e)