# loop for ever
# use try to convert to float and print that number and break the loop
# if not converted print a message and re ask

while True:
    try:
        number = float(input("Enter a number: ").strip())
        print(f"You entered: {number:g}")
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.\n")