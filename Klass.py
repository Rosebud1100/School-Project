#Putting objects into class (template) Abstraction.
#list of students' Names - Class Student (Name, hair, eye, height)
class Student:
    def __init__ (self):
        self.ID = ""
        self.name = ""
        self.course = ""
        self.department = ""
    def create_new_student(self):
        self.ID = input("Enter your ID: ")
        self.name = input("Enter your name: ")
        self.department = input("Enter your department: ")
    def display_students(self):
        print(self.ID)
        print(self.name)
        print(self.department)
class Faculty:
    def __init__ (self):
        self.ID = ""
        self.name = ""
        self.department = ""
    def create_new_faculty (self):
        self.ID = input("Enter your ID: ")
        self.name = input("Enter your name: ")
        self.department = input("Enter your department: ")
    def display_faculty (self):
        print(self.ID)
        print(self.name)
        print(self.department)
myStudents = []
stu = Student()
stu.create_new_student()



myStudents.append(stu)
print(myStudents)