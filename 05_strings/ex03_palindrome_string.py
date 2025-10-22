#user_input = enter a string.strip().lower()
#plain_text = ""
#reversed_text = ""
#for char in user_input:
    #if char.isalpha():
        #plain_text += char
#reversed_text = plain_text[::-1]
#if reversed text == plain text --> print It's a palindrome ✅
#else ==> print Not a palindrome ❌

user_input = input("Enter a word or a sentence: ").strip().lower()
while not user_input:
    print("Empty input is invalid.")
    user_input = input("Enter a word or a sentence: ").strip().lower()
plain_text = "".join([char for char in user_input if char.isalpha()])
reversed_text = plain_text[::-1]
if reversed_text == plain_text:
    print("It's a palindrome ✅")
else:
    print("Not a palindrome ❌")