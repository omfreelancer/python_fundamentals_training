#user_input = enter a string
#vowels = ("a","e","i","o","u")
#vowels_count = 0
#consonants_count = 0
#for char in user_input.strip().lower():
    #if char in vowels ==> vowels_count += 1 
    #elif char.isalpha() ==> consonants_count += 1
#total_letters = vowels_count + consonants_count
#print(f"vowels: {vowels_count}")
#print(f"consonants: {consonants_count}")
#print(f"total letters: {total_letters}")

user_input = input("Enter a string: ").strip().lower()
if not user_input:
    print("You entered an empty string.")
    exit()
vowels = {"a","e","i","o","u"}
vowels_count = 0
consonants_count = 0
for char in user_input:
    if char in vowels:
        vowels_count += 1
    elif char.isalpha():
        consonants_count += 1
total_letters = vowels_count + consonants_count
print(f"Vowels: {vowels_count}")
print(f"Consonants: {consonants_count}")
print(f"Total letters: {total_letters}")