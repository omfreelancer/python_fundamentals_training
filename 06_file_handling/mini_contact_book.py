# import json and create a list named contacts = [] and a dic contact = {}
# show the menu : 1) Add   2) List   3) Search   4) Remove   5) Exit
# get user choice
# if exit say good bye and end the program with exit()
# if add: 
#   ask for name and reask if emty and add the name to the dic
#   ask for the phone number and add it to the dic
#   ask for email and add it to the dic
#   add the dic to the list
# if list:
#   print the list nicely with dumps
# if search:
#   get user name input
#   search in list one dic at a time and search if the name == input or input in name
#   if name is there print it 
#   else print a message telling the user
# if remove:
#   ask for the name if there remove that dic
#   else tell him that that name is not in the list
# else:
#   print a message tell him to chose one of the options not else

import json
import sys

menu = ("1","2","3","4","5")

def save():
    with open("contacts.json","w") as file:
        json.dump(contacts,file, indent=4)

def show_menu():
    print(f"Contacts (loaded: {len(contacts)})")
    print("1) Add   2) List   3) Search   4) Remove   5) Exit")

def add():
    dic = {}
    while not (name := input("Enter name: ").strip()):
        print("Empty input is invalid.")
    for contact in contacts:
        if contact["name"].casefold() == name.casefold():
            print(f"{name} is already in your contact list.")
            return
    phone = input("Enter phone: +212 ").replace(" ", "")
    phone = "+212" + phone
    email = input("Enter email (optional): ")
    dic["name"] = name
    dic["phone"] = phone
    if email:
        dic["email"] = email
    print(f"Added {name.capitalize()} | {phone}")
    contacts.append(dic)
    save()

def list_contacts():
    print("--All Contacts--")
    for i, dic in enumerate(contacts,1):
        email = dic.get("email","")
        if email:
            print(f'{i}. {dic["name"]} | {dic["phone"]} | {email}')
        else:
            print(f'{i}. {dic["name"]} | {dic["phone"]}')

def search():
    query = input("Search name: ")
    print("Result:")
    i = 0
    found = False
    for dic in contacts:
        i += 1
        if (dic["name"]).casefold() == query.casefold() or query.casefold() in dic["name"].casefold():
            email = dic.get("email","")
            if email:
                print(f'{i}. {dic["name"]} | {dic["phone"]} | {email}')
            else:
                print(f'{i}. {dic["name"]} | {dic["phone"]}')
            found = True
    if not found:
        print("No contacts found.")

def remove():
    name = input("Remove name (exact): ")

    for dic in contacts:
        if dic["name"].casefold() == name.casefold():
            while True:
                check = input(f"Are you sure you want to remove {name} (Y/N): ").strip().lower()
                if check in ("y","n"):
                    break
                print("Enter either Y or N.")
            if check == "y":
                contacts.remove(dic)
                save()
                print(f"Removed: {name}")
                return
            else:
                print("Removal canceled.")
                return
    else:
        print(f"{name} is not in contacts list.")

def exit_app():
    save()
    print("Saved to contacts.json ✅")
    sys.exit()

actions = {
    1: add,              
    2: list_contacts,
    3: search,
    4: remove,
    5: exit_app,
}

try:
    with open("contacts.json","r") as file:
        contacts = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    contacts = []

while True:

    show_menu()
    while (choice := input("Choose: ")) not in menu:
        print("Invalid input. Try again.")

    choice = int(choice)

    if choice not in (1, 5) and not contacts:
        print("List of contacts is empty.")
        continue

    action = actions.get(choice)
    action()