#user input = enter a sentence(.strip())
#words = user input.split()
#cleaned words = [re.split(r'[:;,.!?]',user input) for word in words]
#max length = max(cleaned words, key=len)
#longest words = [word for word in words if len(re.split(r'[:;,.!?]',word)) == max length]
#print the longest words

import re

user_input = input("Enter a sentence: ").strip()
if not user_input:
    print("No input provided.")
    exit()
else:
    words = user_input.split()
    cleaned_words = [(word, re.sub(r"[^a-zA-Z]","",word)) for word in words]
    max_length = max(len(c) for _, c in cleaned_words)
    longest_words = [w for w, c in cleaned_words if len(c) == max_length]
    print(f'Longest word(s): {", ".join(longest_words)}')
    print(f"Length: {max_length}")