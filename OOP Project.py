
myCarList = {}
i = 1
class Vehicles:
    def __init__(self):
        self.make = None
        self.model = None
        self.year = None
        self.color = None
        self.vin = None
        self.license_plate = None
    def new_car(self):
        global i
        self.make = input("Enter your make : ")
        self.model = input("Enter your model : ")
        self.year = input("Enter your year : ")
        self.color = input("Enter your color : ")
        self.vin = input("Enter your vin : ")
        self.license_plate = input("Enter your license_plate : ")
        myCarList.update({"c"+str(i):{"Make":self.make, "Model":self.model, "Year":self.year, "Color":self.color, "Vin":self.vin, "License_plate":self.license_plate}})
        i=i+1
    def display_car(self):
        print(myCarList)
    def delete_car(self):
        car_code = input("Enter car code: ")
        if car_code in myCarList:
            del myCarList[car_code]
            print ("Car deleted")
        else:
            print("Car not found")
employees = {}
   
def add_employee():
    print("Add New Employee")

    employee_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    role = input("Enter Job Title (Driver, Dispatcher, etc.): ")
    phone = input("Enter Phone Number: ")
    vehicle = input("Enter Vehicle Information: ")
    hourly_rate = float(input("Enter Hourly Pay Rate: "))
    employees.update = ({
        "Employee ID": employee_id,
        "Name": name,
        "Role": role,
        "Phone": phone,
        "Vehicle": vehicle,
        "Hourly Rate": hourly_rate
    })
    print("Employee added successfully!")


def view_employees():
    print("\n--- Employee Records ---")
    print(employees)
    
    
    
def search_employee():
    employee_id = input("Enter Employee ID to search: ")

    for employee in employees:
        if employee["Employee ID"] == employee_id:
            print("\nEmployee Found:")
            for key, value in employee.items():
                print(f"{key}: {value}")
            return

    print("Employee not found.")



while True:
    print("RIDESHARE EMPLOYEE SYSTEM ")
    print("1. Add Employee")
    print("2. View All Employees")
    print("3. Search Employee")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        view_employees()
    elif choice == "3":
        search_employee()
    elif choice == "4":
        print("Exiting employee system. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

car = Vehicles()


car.display_car()
while True:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        car.new_car()
    elif choice == 2:
        car.delete_car()
    elif choice == 3:
        car.display_car()
    else:
        exit()



