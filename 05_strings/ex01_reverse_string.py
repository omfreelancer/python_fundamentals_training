#user_input = input("Enter a string: ")
#if input is empty ==> print Empty input. Nothing to reverse.
#eles:
    #reversed_text = "".join(reversed(user_input))
    #print(f"{user_input} ==> {reversed}")

import re

user_text = input("Enter a string: ")
if not user_text:
    print("Empty input. Nothing to reverse.")
else:

    full_reverse = "".join(reversed(user_text))

    words_reversed = re.sub(r'\s', lambda m: m.group(0)[::-1], user_text)
    
    print(f"\nOriginal: {user_text}")
    print(f"Full reversed: {full_reverse}")
    print(f"Word-by-word reversed: {words_reversed}")