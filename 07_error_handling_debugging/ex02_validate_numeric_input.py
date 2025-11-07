# open numbers.txt in read mode ==> use try/except to handle file not found
# loop through file object 
# if it is a number add it else skip it and print that you skip such and such
# each time you have a number you will add 1 to count so you know how many
# If count = 0 → print “The file is empty or contains no valid numbers.” and end
# each time you add previous number to the new so you have the total
# average = total / count

try:
    with open("numbers.txt","r") as f:
        count = 0
        total = 0

        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                line = float(line)
                count += 1
                total += line
            except ValueError:
                print(f"Skipping invalid input: '{line}'")

        if count == 0:
            print("The file is empty or contains no valid numbers.")

        else:

            average = total / count
            print(f"Total = {total:.2f}")
            print(f"Average = {average:.2f}")

except FileNotFoundError:
    print("The file 'numbers.txt' was not found.")