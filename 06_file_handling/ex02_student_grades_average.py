# open the file grades.txt and check with try if it exist
# if not print a message
# if founded complete
# if empty print a message
# if not compete
# use .readlines() and .strip() to remove \n to have a list of all numbers
# compute sum / len(list)
# print the result

def safe_float(n):
    try:
        return float(n)
        
    except ValueError:
        return None
try:
    with open("grades.txt","r") as f:
        lines = [num for n in f if (num := safe_float(n.strip())) is not None]

        if not lines:
            print("The file \"grades.txt\" is empty.")
        else:
            average = sum(lines) / len(lines)
            print(f"Average grade: {average:.2f} (based on {len(lines)} grades)")
            
except FileNotFoundError:
    print("The file 'grades.txt' was not found. Please create it first.")