import json

FILE_NAME = "employees.json"


def load_employees():

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []


def save_employees():

    with open(FILE_NAME, "w") as file:
        json.dump(employees, file, indent=4)


employees = load_employees()


def add_employee():

    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    department = input("Enter Department: ")

    try:
        salary = float(input("Enter Salary: "))

    except ValueError:
        print("\nInvalid salary input.")
        return

    employee = {
        "id": emp_id,
        "name": name,
        "department": department,
        "salary": salary
    }

    employees.append(employee)
    save_employees()

    print("\nEmployee added successfully!")


def view_employees():

    if len(employees) == 0:
        print("\nNo employee records found.")
        return

    print("\n========== EMPLOYEE RECORDS ==========")

    for emp in employees:

        print(f"""
Employee ID : {emp['id']}
Name        : {emp['name']}
Department  : {emp['department']}
Salary      : ₹{emp['salary']}
----------------------------------------
""")


def search_employee():

    search_id = input("Enter Employee ID to search: ")

    found = False

    for emp in employees:

        if emp["id"] == search_id:

            print("\nEmployee Found")
            print(f"Name       : {emp['name']}")
            print(f"Department : {emp['department']}")
            print(f"Salary     : ₹{emp['salary']}")

            found = True
            break

    if not found:
        print("\nEmployee not found.")


def update_employee():

    emp_id = input("Enter Employee ID to update: ")

    for emp in employees:

        if emp["id"] == emp_id:

            emp["name"] = input("Enter New Name: ")
            emp["department"] = input("Enter New Department: ")

            try:
                emp["salary"] = float(input("Enter New Salary: "))

            except ValueError:
                print("\nInvalid salary input.")
                return

            save_employees()

            print("\nEmployee updated successfully!")
            return

    print("\nEmployee not found.")


def remove_employee():

    emp_id = input("Enter Employee ID to remove: ")

    for emp in employees:

        if emp["id"] == emp_id:

            employees.remove(emp)
            save_employees()

            print("\nEmployee removed successfully!")
            return

    print("\nEmployee not found.")


while True:

    print("\n" + "=" * 40)
    print("     EMPLOYEE MANAGEMENT SYSTEM")
    print("=" * 40)

    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Remove Employee")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_employee()

    elif choice == "2":
        view_employees()

    elif choice == "3":
        search_employee()

    elif choice == "4":
        update_employee()

    elif choice == "5":
        remove_employee()

    elif choice == "6":
        print("\nExiting system...")
        break

    else:
        print("\nInvalid choice.")