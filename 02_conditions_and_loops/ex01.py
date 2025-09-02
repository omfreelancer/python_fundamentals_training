#ask for numeric score(0-100) and save it in score variable
#check if not a number print enter a number and re ask 
#check if it's out of range and re ask 
#if it's in the range look if
#90–100 → A
#80–89 → B
#70–79 → C
#60–69 → D
#0–59 → F

while True:
    score = input("Enter your numeric score: ")
    try:
        score = float(score)
        if score < 0 or score >100:
            print("Score should be between 0 and 100.")
            continue
        if score>=90:
            print("Your Grade is: A")
        elif score>=80:
            print("Your Grade is: B")
        elif score>=70:
            print("Your Grade is: C")
        elif score>=60:
            print("Your Grade is: D")
        else:
            print("You failed!")
        break
    except ValueError:
        print("Enter a number (e.g., 89).")