import string

def count_occurrences(lst, target):
    i = 0
    for item in lst:
        if item == target:
            i += 1
    
    return i

def count_vowels(text):
    vowels = ("a","e","i","o","u")
    i = 0
    for char in text:
        if char.lower() in vowels:
            i += 1

    return i

def count_upper(text):
    upper_letters = string.ascii_uppercase
    i = 0
    for char in text:
        if char in upper_letters:
            i += 1

    return i

def count_duplicates(lst):
    counts = {}
    duplicates = {}
    for item in lst:
        if item in counts:
            counts[item] += 1

        else:
            counts[item] = 1
    
    for item, count in counts.items():
        if count > 1:
            duplicates[item] = count

    return duplicates