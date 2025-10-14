#item_list=[]
#show menu(add, remove, view, clear, quit)
#save user_choice in choice
#if user choice is quit end the program
#if choice is empty loop until find one
#choice = choice.strip().lower()
#if choice is not in menu loop until find one
#if choice is add ==> append to the list and print confirmation
#if choice is remove ask for the item name and make sure it's in the list 
#if it is there remove it and print confirmation if not say so
#if view see if the list is empty say so if not show numbered items
#if choice is clear → empty the list and print confirmation.

items_list = []

def count_list():
    return len(items_list)

def get_valid_choice():
    menu = ("add","remove","view","clear","quit")
    while True:
        choice = input("\nWhat is your choice: ").strip().lower()
        if not choice:
            print("Empty input is not valid. Please Enter a valid choice.")
            continue
        if choice in menu:
            return choice
        else:
            print("Invalid input. Please enter a valid choice.")

def add_item_to_list():
    while True:
        item = input("Enter the item you want to add: ").strip()
        if not item:
            print("Empty input is not valid. Please Enter a valid item name.")
            continue
        else:
            items_list.append(item)
            print(f"{item} was added to the list.")
            break

def remove_item_from_list():

    if not items_list:
        print("List is empty. Nothing to remove.")
        return
    
    else:
        while True:
            item = input("Enter the item you want to remove from the list: ").strip()
            if not item:
                print("Empty input is not valid. Please Enter a valid item name.")
                continue
            
            index = next((i for i,value in enumerate(items_list) if value.lower() == item.lower() ),None)
            if index is not None: 
                items_list.pop(index)
                print(f"{item} was removed successfully.")
                break
            else:
                print(f'"{item}" is not found in the list.')

def show_items_list():
    if not items_list:
        print("List is empty.")
    else:
        print("\n==The Shopping List==")
        print(f"{count_list()} items:")
        for i, item in enumerate(items_list,1):
            print(f"{i}. {item}")
        print("==" * 20)

def print_count():
    print(f"List has now {count_list()} item(s).")
        
print("Welcome in The Shopping List program.")

while True:
    print("\nThe menu: add, remove, view, clear, quit")
    choice = get_valid_choice()

    if choice == "quit":
        print("Goodbye.")
        break

    elif choice == "add":
        add_item_to_list()
        print_count()

    elif choice == "remove":
        before = count_list()
        remove_item_from_list()
        if count_list() != before:  
            print_count()

    elif choice == "view":
        show_items_list()
    
    elif choice == "clear":
        confirm = input("Are you sure you want to clear the whole list? (y/n): ").lower()
        if confirm == "y":
            count = count_list()
            items_list.clear()
            print(f"Cleared {count} item(s) successfully.")
        else:
            print("Clear cancelled.")