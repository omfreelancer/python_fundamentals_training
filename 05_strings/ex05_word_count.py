# 1. Import re and create an empty dictionary (words_dictionary = {}).
# 2. Ask user for a sentence or paragraph and convert to lowercase.
# 3. Clean the text using regex to remove punctuation and digits.
# 4. Split the cleaned text into words.
# 5. For each word in the list:
#        if word exists in words_dictionary:
#             increase its count by 1
#        else:
#             set its count to 1
# 6. Print "Word count:".
# 7. For each word in sorted order of dictionary keys:
#        print word and its count.

import re
words_dictionary = {}
user_input = input("Enter a sentence or a paragraph: ")
cleaned_input = re.sub(r'[^a-zA-Z\s]',"",user_input.lower())
words = cleaned_input.split()
for word in words:
    if word in words_dictionary:
        words_dictionary[word] += 1
    else:
        words_dictionary[word] = 1
print("Word count:")
for word in sorted(words_dictionary):
    print(f"{word} : {words_dictionary[word]}")