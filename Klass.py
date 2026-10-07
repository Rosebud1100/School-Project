#Putting objects into class (template) Abstraction.
#list of students' Names - Class Student (Name, hair, eye, height)
class Student:
    def __init__ (self):
        self.ID = ""
        self.name = ""
        self.department = ""
        self.advisor = ""
    def create_new_student(self):
        self.ID = input("Enter your ID: ")
        self.name = input("Enter your name: ")
        self.department = input("Enter your department: ")
    def display_students(self):
        print(self.ID)
        print(self.name)
        print(self.department)
        print(self.advisor.name)
    def assign_advisor(self, advisor):
        self.advisor = advisor
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
    def display_faculty (self):
        print(self.ID)
        print(self.name)
        print(self.department)
class course:
    def __init__ (self):
        self.ID = ""
        self.name = ""
        self.department = ""
        self.enrolled_students=[]
    def create_new_course (self):
        self.ID = input("Enter class ID: ")
        self.name = input("Enter class name: ")
        self.department = input("Enter class department: ")
    def display_course (self):
        print(self.ID)
        print(self.name)
        print(self.department)
    def enroll_students(self, sid):
        self.enrolled_students.append(sid)


myStudentsList = []
myFacultyList = []
myCourseList = []
while True:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        stu = Student()
        stu.create_new_student()
        myStudentsList.append(stu)
        get_advisor = input("Enter your advisor ID: ")
        for f in myFacultyList:
            if f.ID == get_advisor:
                stu.assign_advisor(f)
        stu.display_students()
    elif choice == 2:
        fac = Faculty()
        fac.create_new_faculty()
        myFacultyList.append(fac)
        fac.display_faculty()
    elif choice == 3:
        cour = course()
        cour.create_new_course()
        cour.enroll_students(sid)
        myCourseList.append(cour)
        cour.display_course()
    else:
        exit()
