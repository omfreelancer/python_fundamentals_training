# import random 
# make a function that gives a random number between 1 and 6
# ask user how many times he wants to roll the dice
# loop in range of user number choice:
#   use the function 
#   print the random number

import random, time

def random_number():
    return random.randint(1,6)

def is_number(n):
    try:
        return int(n)
    except ValueError:
        return None
    
results = []
    
while (times := is_number(user_input := input("How many times do you want to roll the dice?: ").strip())) is None:
    print("Invalid input. Please enter a valid number.")

print("\nRolling the dice...\n")
time.sleep(1)

for i in range(1, times+1):
    rolling = random_number()
    print(f"Roll {i}: {rolling} 🎲")
    results.append(rolling)

print("\nResults:", results)
print("Highest roll:", max(results))
