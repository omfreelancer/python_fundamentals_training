import json
import sys
import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")

menu = ("1","2","3","4","5")

def save():
    logging.debug("Starting saving data.")
    try:
        with open("contacts.json","w") as file:
            json.dump(contacts,file, indent=4)
            logging.info("Data saved successfully.")
    except Exception:
        logging.exception("Failed to save data.")

def show_menu():
    print(f"Contacts (loaded: {len(contacts)})")
    print("1) Add   2) List   3) Search   4) Remove   5) Exit")

def add():
    logging.debug(" the function add() has started.")
    dic = {}
    while not (name := input("Enter name: ").strip()):
        print("Empty input is invalid.")
    assert isinstance(name, str), "name must be a string"

    if any(char.isdigit() for char in name):
        print("Name must not contain digits.")
        return
    
    for contact in contacts:
        if contact["name"].casefold() == name.casefold():
            logging.warning(f"Attempt to add duplicate contact: <{name}>")
            print(f"{name} is already in your contact list.")
            return

    phone = input("Enter phone: +212 ").replace(" ", "")
    if not all(number.isdigit() for number in phone):
        print("Phone number must contain ONLY digits after +212")
        return
    
    if len(phone) != 8:
        print("Phone number must have 8 numbers after +212")
        return
    
    assert isinstance(phone, str), "phone must be a string."
    assert phone, "phone can't be empty."
    phone = "+212" + phone
    assert phone.startswith("+212"), "phone must starts with +212"
    email = input("Enter email (optional): ")
    dic["name"] = name
    assert "name" in dic, "dictionary must have 'name'."
    dic["phone"] = phone
    assert "phone" in dic, "dictionary must have 'phone'."
    if email:
        dic["email"] = email
        assert "@" in dic["email"], "email must contain '@'."
    print(f"Added {name.capitalize()} | {phone}")
    logging.debug(f"name: {name}, phone: {phone}, email: {email if email else 'None'}")
    contacts.append(dic)
    save()
    logging.info(f"Contact added and saved successfully: <{name}>")

def list_contacts():
    print("--All Contacts--")
    for i, dic in enumerate(contacts,1):
        email = dic.get("email","")
        if email:
            print(f'{i}. {dic["name"]} | {dic["phone"]} | {email}')
        else:
            print(f'{i}. {dic["name"]} | {dic["phone"]}')

def search():
    logging.debug("Starting the function search()")
    query = input("Search name: ")
    logging.info(f"Searching for <{query}>")
    print("Result:")
    i = 0
    found = False
    for dic in contacts:
        i += 1
        if (dic["name"]).casefold() == query.casefold() or query.casefold() in dic["name"].casefold():
            logging.info(f"Match found for <{query}> → contact <{dic['name']}>")
            email = dic.get("email","")
            if email:
                print(f'{i}. {dic["name"]} | {dic["phone"]} | {email}')
            else:
                print(f'{i}. {dic["name"]} | {dic["phone"]}')
            found = True
    if not found:
        logging.warning(f"No results found for <{query}>.")
        print("No contacts found.")

def remove():
    logging.debug("Starting remove()")
    name = input("Remove name (exact): ")
    logging.info(f"Attempting to remove <{name}>")

    for dic in contacts:
        if dic["name"].casefold() == name.casefold():
            logging.info(f"Contact found for removal : <{name}>")
            while True:
                check = input(f"Are you sure you want to remove {name} (Y/N): ").strip().lower()
                if check in ("y","n"):
                    break
                print("Enter either Y or N.")
            if check == "y":
                logging.info(f"Removing contact : <{name}>")
                contacts.remove(dic)
                save()
                print(f"Removed: {name}")
                return
            else:
                logging.info(f"Removal canceled for <{name}>")
                print("Removal canceled.")
                return
    else:
        logging.warning(f"Remove failed -- <{name}> not found")
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

def validate_phone(phone):
    if not phone or not (all(number.isdigit() for number in phone)) or not (len(phone) ==8):
        return False
    return True

def add_contact(contacts,name,phone,email=None):
    if any(name.casefold() == contact["name"].casefold() for contact in contacts) \
        or not validate_phone(phone):
        return False
    
    phone = "+212" + phone

    dictionary = {"name":name, "phone":phone}
    if email:
        dictionary["email"] = email

    contacts.append(dictionary)

    return True

def search_contact(contacts,query):
    results = []
    for contact in contacts:
        if query.casefold() == contact["name"].casefold() \
            or query.casefold() in contact["name"].casefold():
            results.append(contact)
    return results

def remove_contact(contacts, name):
    for contact in contacts:
        if name.casefold() == contact["name"].casefold():
            contacts.remove(contact)
            return True
    return False

try:
    with open("contacts.json","r") as file:
        contacts = json.load(file)
        assert isinstance(contacts,list), "Contacts must be a list"
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