    #Function bmi(weight,height)
#result = weight / (height ** 2)
#return result
    #Main program
#ask user for weight in kg and height in cm
#check if numbers and if > 0
#convert height_cm to height_m
#apply the function bmi(weight,height)
#print result rounded to 2 decimals
#check category:
    #if result < 18.5 print Underweight
    # if result between 18.5–24.9 print Normal
    # if result between 25–29.9 print Overweight
    # if result ≥30 print Obesity

def bmi(weight,height):
    result = weight / (height ** 2)
    return result

while True:
    try:
        weight = float(input("Enter your weight in kg: "))
        height_cm = float(input("Enter your height in cm: "))

        if weight <= 0 or height_cm <= 0:
            print("Weight and height must be greater than 0.")
            continue

        
        height_m = height_cm / 100
        result = bmi(weight,height_m)

        print(f"Your bmi = {result:.2f}")

        if result < 18.5:
            print("You are Underweight.")
        elif result <= 24.9:
            print("You have a normal weight.")
        elif result <= 29.9:
            print("You are overweight.")
        else:
            print("You are obese.")

        break

    except ValueError:
        print("Enter numbers (e.g., 75.5).")