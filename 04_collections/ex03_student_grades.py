#use a loop ask the user for a name then for a grade 
#give him an option "done" to stop the loop
#every time i'll add that pair of name:grade to a dic
#finding the max and min key and value usin max/min(grade,key=dic.get)
#calclulate average sum(dic)/len(sum)
#print them in a net way

grades = {}
while True:
    name = input("Enter the student name (or 'done' to stop): ").strip().lower()
    if name == "done":
        break
    if not name:
        print("Empty input is not valid.")
        continue
    if name in grades:
        print(f"{name} is already exists.")
        continue
    while True:
        try:
            grade = float(input(f"Enter the grade of {name}: "))
            if not (0 <= grade <= 100):
                print("Grade must be between 0 and 100.")
                continue
            break        
        except ValueError:
            print("Enter a valid grade number (e.g, 75).")
    grades[name] = grade

if not grades:
    print("No data entered.")
else:
    highest_student_name = max(grades, key=grades.get)
    highest_student_grade = grades[highest_student_name]
    lowest_student_name = min(grades, key=grades.get)
    lowest_student_grade = grades[lowest_student_name]

    average_grade = sum(grades.values()) / len(grades)

    print("\n=== Grade Report ===")
    print(f"Student count: {len(grades)}")
    print(f"Average grade: {average_grade:.2f}")
    print(f"Highest: {highest_student_name.title()} ({highest_student_grade})")
    print(f"Lowest: {lowest_student_name.title()} ({lowest_student_grade})")

    print(f"\nAll students sorted by grade ({len(grades)} total):")
    for i, (name, grade) in enumerate(sorted(grades.items(), key=lambda x: x[1], reverse=True), 1):
        print(f"{name.title()}: {grade:.2f}")