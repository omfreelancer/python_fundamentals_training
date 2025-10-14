#shopping_cart = {}
#loop
    #show menu add | remove | view | clear | quit
    #choice = user input.strip().clear
    #if quit
        #break
    #if add 
        # enter item 
        #loop 
            # until enter float(price)
        # print added "item" ($price) to the cart
    #if remove 
        #user enter the item name.strip().clear()
        #check if the item is in shopping_cart
        #if no ==> print the item is not in the list
        #if yes ==> remove it and print that you removed it
    #if view
        #print the items in a numerate way(1. item - price:.2f) 
        #and print the sum
    #if clear
        #ask if he's sure
        #if yes do it with clear(dic)
        #if no don't do anything
    #else:
        #print invalid input

shopping_cart = {}
def show_menu():
    print("Menu: add | remove | view | clear | quit\n")

def add():
    item = input("Enter item name: ").strip().lower()
    if not item:
        print("Item name cannot be empty.")
        return
    if item in shopping_cart:
        print(f'"{item}" is already in the cart.')
        return
    while True:
        try:
            price = float(input("Enter item price: "))
            if price <= 0:
                print("Price must be greater than 0.")
                continue
            break
        except ValueError:
            print("Enter a valid price (e.g., 15.99).")
    shopping_cart[item] = price
    print(f'Added "{item}" (${price:.2f}) to the cart.')

def remove():
    if not shopping_cart:
        print("Cart is empty. Nothing to remove.")
        return
    item = input("Enter the item name you want to remove: ").strip().lower()
    if not item:
        print("Item name cannot be empty.")
        return
    if item in shopping_cart:
        confirm = input(f'Are you sure you want to remove "{item}"? (y/n): ').strip().lower()
        if confirm == "y":
            shopping_cart.pop(item)
            print(f'"{item}" was removed successfully.')
        else:
            print("Removal cancelled.")
    else:
        print(f'"{item}" was not found in the shopping cart.')

def view():
    if not shopping_cart:
        print("No items to show.")
    else:
        print("\n=== Cart ===")
        for i, (name, price) in enumerate(shopping_cart.items(), 1):
            print(f"{i}. {name} — ${price:.2f}")
        print(f"Total: ${sum(shopping_cart.values()):.2f}")

def clear():
    if not shopping_cart:
        print("Cart is already empty.")
        return
    check = input("Are you sure you want to clear the shopping cart (y/n): ").strip().lower()
    while check not in ("y", "n"):
        check = input("Invalid input. Enter 'y' to clear or 'n' to cancel: ").strip().lower()
    if check == "y":
        shopping_cart.clear()
        print("Shopping cart was cleared successfully.")
    else:
        print("Shopping cart was not cleared.")

while True:
    show_menu()
    choice = input("Enter your choice: ").strip().lower()
    if choice == "quit":
        print("Goodbye!")
        break
    elif choice == "add":
        add()
    elif choice == "remove":
        remove()
    elif choice == "view":
        view()
    elif choice == "clear":
        clear()
    else:
        print("Invalid input. Enter a valid choice from the menu.")