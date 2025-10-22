# rules = 0
# ask user to enter a password
# check every rule 
#   if rule met add 1 to rules
# If rules equal to 5 → print “Password is STRONG ✅” 
# If rules equal to 3 or 4 → print “Password is MEDIUM ⚠️” 
# If rules < 3 → print “Password is WEAK ❌”

import string

missings = []
rules = 0
user_input = input("Enter a password: ").strip()
if not user_input:
    print("Empty input is invalid.")
    exit()
special_char = set(string.punctuation)
if len(user_input) >= 8:
    rules += 1
else:
    missings.append("Should have at least 8 characters.")
if any(c.isupper() for c in user_input):
    rules += 1
else:
    missings.append("Add at least one uppercase letter.")
if any(c.islower() for c in user_input):
    rules += 1
else:
    missings.append("Add at least one lowercase letter.")
if any(c.isdigit() for c in user_input):
    rules += 1
else:
    missings.append("Add at least one digit.")
if any(c in special_char for c in user_input):
    rules += 1
else:
    missings.append("Add at least one special character.")
if rules == 5:
    print("Password is STRONG ✅")
elif rules == 3 or rules == 4:
    print("Password is MEDIUM ⚠️")
else:
    print("Password is WEAK ❌")
if missings:
    print("\n".join(missings))