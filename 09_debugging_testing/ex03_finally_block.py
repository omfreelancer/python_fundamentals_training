file = input("Enter file name: ").strip()

if not file:
    print("Invalid input. Filename cannot be empty.")

else:
    try:
        with open(file,"r") as f:
            content = f.readlines()
            if content:
                for line in content:
                    if line.strip():
                        print(line.strip())
            else:
                print("The file is empty.")
    except FileNotFoundError:
        print("Error: File not found.")
    finally:
        print("\nOperation finished.")