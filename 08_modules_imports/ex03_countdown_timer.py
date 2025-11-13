# import time
# ask for user input "n" number and make sure it's a positive integer >= 1
# loop i in range(n to 1):
#   print time left {i}
#   time.sleep(1)
# print Time's up! ⏰

import time

def is_number(n):
    try:
        return int(n)
    except ValueError:
        return None
    
while (n := is_number(user_input := input("Enter countdown time in seconds: ").strip())) is None or n < 1:
    print("Invalid input. Please enter a positive number.")

left = n
for _ in range(n):
    print(f"Time left: {left}s")
    left -= 1
    time.sleep(1)
print("Time's up! ⏰")