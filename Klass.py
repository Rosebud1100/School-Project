#Putting objects into class (template) Abstraction.
#list of students' Names - Class Student (Name, hair, eye, height)
class Student:
    def __init__ (self):
        self.ID = ""
        self.name = ""
        self.course = ""
        self.department = ""
        self.advisor = ""
    def create_new_student(self):
        self.ID = input("Enter your ID: ")
        self.name = input("Enter your name: ")
        self.course = input("Enter your course: ")
        self.department = input("Enter your department: ")
        self.advisor = input("Enter your advisor: ")
    def display_students(self):
        print(self.ID)
        print(self.name)
        print(self.course)
        print(self.department)
        print(self.advisor)
class Faculty:
    def __init__ (self):
        self.ID = ""
        self.name = ""
        self.department = ""
        self.students = ""
    def create_new_faculty (self):
        self.ID = input("Enter your ID: ")
        self.name = input("Enter your name: ")
        self.department = input("Enter your department: ")
        self.students = input("Enter your students: ")
    def display_faculty (self):
        print(self.ID)
        print(self.name)
        print(self.department)
        print(self.students)

myStudentsList = []
myFacultyList = []
myCourseList = []
while True:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        stu = Student()
        stu.create_new_student()
        myStudentsList.append(stu)
        stu.display_students()
    elif choice == 2:
        fac = Faculty()
        fac.create_new_faculty()
        myFacultyList.append(fac)
        fac.display_faculty()
    else:
        exit()
