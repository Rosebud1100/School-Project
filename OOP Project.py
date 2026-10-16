employees = []


def add_employee():
    print("\n--- Add New Employee ---")

    employee_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    role = input("Enter Job Title (Driver, Dispatcher, etc.): ")
    phone = input("Enter Phone Number: ")
    vehicle = input("Enter Vehicle Information: ")
    hourly_rate = float(input("Enter Hourly Pay Rate: "))

    employee = {
        "Employee ID": employee_id,
        "Name": name,
        "Role": role,
        "Phone": phone,
        "Vehicle": vehicle,
        "Hourly Rate": hourly_rate
    }

    employees.append(employee)
    print("Employee added successfully!")


def view_employees():
    print("\n--- Employee Records ---")

    if not employees:
        print("No employee records found.")
        return

    for employee in employees:
        print("-" * 35)
        for key, value in employee.items():
            print(f"{key}: {value}")


def search_employee():
    employee_id = input("Enter Employee ID to search: ")

    for employee in employees:
        if employee["Employee ID"] == employee_id:
            print("\nEmployee Found:")
            for key, value in employee.items():
                print(f"{key}: {value}")
            return

    print("Employee not found.")


def main():
    while True:
        print("\n===== RIDESHARE EMPLOYEE SYSTEM =====")
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


if __name__ == "__main__":
    main()


