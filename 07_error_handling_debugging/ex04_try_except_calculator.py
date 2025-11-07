# open notes.txt and use try/except
# if found read all content in text
#   if text is empty print a message
#   else print the content
# except valuefilenotfound print a message


print("Reading from notes.txt...\n")
try:
    with open("notes.txt", "r") as f:
        text = f.read().strip()
        if not text:
            print("The file 'notes.txt' is empty.")
        else:
            print("File content:\n")
            print(text)
except FileNotFoundError:
    print("Error: The file 'notes.txt' was not found.")