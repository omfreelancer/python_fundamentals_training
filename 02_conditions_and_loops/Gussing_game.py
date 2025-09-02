#program guess a number between 1-100
#ask the user to guess a number
#After each guess:
# If guess < target → print "Too low!".
# If guess > target → print "Too high!".
# Limit attempts (e.g. 7 or 10 tries).
# Track attempts and print score (number of tries used).
# If guessed correctly → print "Correct! You won in X tries 🎉".
# If out of attempts → reveal the number.

import random

target = random.randint(1,100)
attempts = 7
tries = 0

print("I picked a number between 1 and 100. You have 7 attempts.")

while attempts > 0:

    raw = input("Enter your guess (1-100): ").strip()

    if not raw.isdigit():

        print("Invalid input. Please enter an integer (e.g., 47)")
        continue

    guess = int(raw)

    if not (1 <= guess <= 100):

        print("Out of range. Enter a number between 1 and 100.")
        continue

    attempts -= 1
    tries += 1

    if guess == target:

        print(f"Correct! you won in {tries} attempt(s)🎉")
        break

    else:

        if guess > target:
            print("Too high!")
        else:
            print("Too low!")

    if attempts > 0:
        print(f"{attempts} attempt(s) left.\n")

else:

    print("You're out of attempts! ❌")
    print(f"Correct number: {target}")