# import re and create a dictionary counter = {}
# read the file and save it to a variable 
# make that text all lower and and use re.split and ignore anything
# else text to have a list
# use a loop to count each word 
# add that data to the dic
# print the result alphabetcly

import re
counter = {}

try:
    with open("article.txt","r") as f:
        lines = f.readlines()
        if not lines:
            print("The file 'article.txt' is empty.")
            exit()

        line = " ".join(line.strip().lower() for line in lines if line.strip())
        clean_line = [w for w in (re.split(r"[^\w']+",line)) if w.strip()]

        for word in clean_line:
            if word in counter:
                counter[word] += 1
            else:
                counter[word] = 1
        print("Word count:")
        for w, c in sorted(counter.items()):
            print(w,":",c)

except FileNotFoundError:
    print("The file 'article.txt' was not found.")