#ask for a password
#check if it is >=8 if not reask and tell me it should be more then 8length
#if yes check for there are numbers if not tell him it should have at least one number
#if yes check if there at least one letter lower or upper
#if all conditions are met print (strong password)
#for every condition unmet print (weak password) and the problem and re ask

print("""Password conditions:

        1.Password length ≥ 8

        2.Contains at least one digit (0-9)

        3.Contains at least one letter (a-z or A-Z)

      """)

while True:

    password = input("Enter a password: ").strip()

    has_leng = len(password) >=8
    has_digit = any(ch.isdigit() for ch in password)
    has_lett = any(ch.isalpha() for ch in password)

    problems = []

    if not has_leng:
        problems.append("- Password must be at least 8.")

    if not has_digit:
        problems.append("- Password must have at least one digit.")

    if not has_lett:
        problems.append("- Password must have at least one letter (a-z or A-Z)")

    if problems:

        print("Weak password")
        print(*problems, sep="\n")
        continue

    print("Strong password ✅ Added successfully!")
    break