#choose a password= "pyhton123"
#ask the user for password and compare it to password 
#If they get it right → print "Access granted ✅".
#If they fail 3 times → print "Access denied ❌".

password = "python123"
tries = 3

while tries > 0:

    user_input = input("Enter the password: ")

    if user_input == password:

        print("Access granted ✅")

        break

    else:

        tries -= 1

        if tries != 0:

            print("Incorrect password")
            print(f"You have {tries} attempt(s) left.")

        else:

            print("Access denied ❌")