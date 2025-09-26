# Define a function is_palindrome(text)
    # Convert to lowercase.
    # Remove spaces.
    # Reverse the string ([::-1]).
    # Compare with original.
    # Return True if palindrome, else False.
# In main program:
    # Ask the user for input string.
    # Call is_palindrome(text).
    # Print "X is a palindrome ✅" or "X is not a palindrome ❌".

def is_palindrome(text):

    text = text.lower()
    new_text = ""

    for ch in text:
        if ch.isalpha():
            new_text += ch

    text_reversed = new_text[::-1]
    return new_text == text_reversed
    
user_input = input("Enter a text: ")
result = is_palindrome(user_input)

print(f'"{user_input}" is a palindrome ✅' if result else f'"{user_input}" is not a palindrome ❌')