class Student():
    def __init__(self,student_id,name,age):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.assigned_courses = []
    def assign_course(self,course):
        self.assigned_courses.append(course)
    def display_info(self):
        print("STUDENT DETAILS")
        print(f"Student ID: {self.student_id}")
        print(f"Student Name: {self.name}")
        print(f"Age: {self.age}")
        print("Courses:", ", ".join([c.course_name for c in self.assigned_courses]) or "None")
class Course():
    def __init__(self,course_id,course_name,instructor):
        self.course_id = course_id
        self.course_name = course_name
        self.instructor = instructor
    def display_course(self):
        print("COURSE DETAILS")
        print(f"Course ID: {self.course_id:<10}")
        print(f"Course Name: {self.course_name:<20}")
        print(f"Instructor: {self.instructor:<20}")
students_list = []
courses_list = []
u_studentid = 1
u_courseid = 1
def add_student():
    global u_studentid
    name = input("Enter Student Name:")
    age = int(input("Enter Student Age"))
    student = Student(u_studentid,name,age)
    students_list.append(student)
    print(f"Student Added: {u_studentid}")
    u_studentid+=1
def add_courses():
    global u_courseid
    course_name = input("Enter Course name:")
    instructor = input("Enter Instructor Name:")
    course = Course(u_courseid,course_name,instructor)
    courses_list.append(course)
    print(f"Course Added: {u_courseid}")
    u_courseid+=1
def assigncourse():
    student_id = int(input("Enter student ID:"))
    course_id = int(input("Enter Course ID: "))
    student = next((s for s in students_list if s.student_id == student_id),None)
    course = next((c for c in courses_list if c.course_id == course_id),None)
    if student is None:
        print("Student ID does not exist")
        return
    if course is None:
        print("Course ID does not exist")
        return
    student.assign_course(course)
    print("Course Assigned Successfully")
def view_details():
    student_id = int(input("Enter Student ID:"))
    student = next((s for s in students_list if s.student_id == student_id),None)
    if student is None:
        print("Invalid Student ID")
        return
    student.display_info()
def list_students():
    print("List of Students")
    print(f"{'student_id':<10}{'name':<20}{'age':<10}{'assigned_courses'}")
    print("-"*60)
    for s in students_list:
        courses = ",".join([c.course_name for c in s.assigned_courses]) or "None"
        print(f"{s.student_id:<10}{s.name:<20}{s.age:<20}{courses}")
def list_courses():
    print("List of Courses")
    print(f"{'course_id':<10}{'course_name':<20}{'instructor':<20}")
    print("-"*50)
    for c in courses_list:
     print(f"{c.course_id:<10}{c.course_name:<20}{c.instructor:<20}")    
while True:
    print("Student Course Management System")
    print("1.Add a Student")
    print("2.Add a Course")
    print("3.Assign a Course to a Student")
    print("4.View Student Details")
    print("5.List all Students")
    print("6.List all Courses")
    print("7.Exit")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        add_student()
    elif choice == 2:
        add_courses()    
    elif choice == 3:
        assigncourse()
    elif choice == 4:
        view_details()
    elif choice == 5:
        list_students()
    elif choice == 6:
        list_courses()
    elif choice == 7:
        print("Exit")
        break
    else:
        print("Invalid choice")