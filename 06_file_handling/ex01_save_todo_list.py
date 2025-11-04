# ask user to write a line of text
# save it to a file named notes.txt
# overwrite it if already exists
# print a confirmation message

user_input = input("Enter something to save: ").strip()
if not user_input:
    print("Empty input is not saved.")
else:
    with open("notes.txt","w") as file:
        file.write(user_input)
    print("Text saved successfully to notes.txt ✅")