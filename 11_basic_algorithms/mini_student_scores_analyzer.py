def is_number(text):
    while True:
        try:
            result = int(input(text))
            return result
        except ValueError:
            print("Invalid input. Enter a valid number.")

def get_students():
    students = []
    number_students = is_number("How many students?: ")

    for _ in range(number_students):
        student = {}

        while not (name := input("Enter a name: ").strip()):
            print("Name cannot be empty.")

        score = is_number(f"Enter {name}'s score: ")
        
        student["name"] = name
        student["score"] = score

        students.append(student)

    return students

def get_scores(students):

    total_score = sum(student["score"] for student in students)

    average = total_score / len(students)

    scores = {"total_score": total_score, "average": average}

    return scores

def get_highest_and_lowest(students):

    first = students[0]

    highest_score = first["score"]
    highest_name = first["name"]

    lowest_score = first["score"]
    lowest_name = first["name"]

    for student in students:
        if student["score"] > highest_score:
            highest_score = student["score"]
            highest_name = student["name"]
        
        if student["score"] < lowest_score:
            lowest_score = student["score"]
            lowest_name = student["name"]

    highest = {"name": highest_name, "score": highest_score}
    lowest = {"name": lowest_name, "score": lowest_score}

    extremes = {"highest": highest, "lowest": lowest}

    return extremes

def sort_students(students):
    if len(students) < 2:
        return students
    
    while True:
        swapped = False
        for i in range(len(students) -1):
            if students[i]["score"] > students[i+1]["score"]:
                students[i], students[i+1] = students[i+1], students[i]
                swapped = True

        if not swapped:
            return students
        
def print_report(students, scores, extremes, sorted_students):
    average = scores["average"]
    highest = extremes["highest"]
    lowest = extremes["lowest"]

    print("---- Student Score Report ----")
    print(f"Total students: {len(students)}")
    print(f"Average score: {average:.2f}")
    print(f"Top student: {highest['name']} ({highest['score']})")
    print(f"Lowest student: {lowest['name']} ({lowest['score']})")
    print("Sorted (low → high):")
    for i,student in enumerate(sorted_students,1):
        print(f"{i}. {student['name']} — {student['score']}")

students = get_students()
scores = get_scores(students)
extremes = get_highest_and_lowest(students)
sorted_students = sort_students(students)
print_report(students, scores, extremes, sorted_students)