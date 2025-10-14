#ask user for two groups of words/numbers
#convert them to lists
#convert the lists to sets by set(list)
#use set.intersection(set) or set1 & set2
#print the common words if no word is there print No common elements found

import re

first_group = input("Enter the first group of words/numbers: ").strip().lower()
second_group = input("Enter the second group of words/numbers: ").strip().lower()

first_list = [w for w in re.split(r'[,.!?\s]+', first_group) if w]
second_list = [w for w in re.split(r'[,.!?\s]+', second_group) if w]

if not first_group or not second_group:
    print("You must enter at least one item in each group.")
    exit()

set1 = set(first_list)
set2 = set(second_list)

common = set1 & set2

if not common:
    print("No common elements found")
else:
    print(f"\nGroup 1: {set1}")
    print(f"Group 2: {set2}")
    print(f"=== Common items ({len(common)} total)===")
    for w in sorted(common):
        print(f"- {w}")