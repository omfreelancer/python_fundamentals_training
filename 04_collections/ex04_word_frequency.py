#ask user to enter a sentence or a pragraph
#split that input into words in a list and use re.split(r'[!,.?]+')
#use a loop to calculate how many of each word in the list and save that pair(word:num) in a dic
#don't calculate a word more than once
#print the dic nicely

import re

sentence = input("Enter a group of words: ")

words = [w.lower() for w in re.split(r'[!?.,\s]+',sentence) if w]

dic_words = {}

for word in words:
    dic_words[word] = dic_words.get(word, 0) + 1

print(f"\n==WORDS FREQUENCY ({len(dic_words)} unique, {len(words)} total)==")
for i, (word,frequ) in enumerate(sorted(dic_words.items(), key=lambda x: x[1],reverse=True),1):
    print(f"{i}. {word}: {frequ}")