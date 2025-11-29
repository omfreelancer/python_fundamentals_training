class Student:
    def __init__(self, name, student_id, courses=None):
        self.name = name
        self.student_id = student_id
        self.courses = [] if courses is None else courses

    def enroll(self,course):
        if course not in self.courses:
            self.courses.append(course)
            course.add_student(self)
            return f"{self.name} enrolled in {course.title}"


    def list_courses(self):
        return [course.title for course in self.courses]
    
class Course:
    def __init__(self, title, code, students=None):
        self.title = title
        self.code = code
        self.students = [] if students is None else students

    def add_student(self,student):
        if student not in self.students:
            self.students.append(student)
        
    def list_students(self):
        return [student.name for student in self.students]