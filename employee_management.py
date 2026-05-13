employees = []

def add_employee():

    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    department = input("Enter Department: ")
    salary = float(input("Enter Salary: "))

    employee = {
        "id": emp_id,
        "name": name,
        "department": department,
        "salary": salary
    }

    employees.append(employee)

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


def remove_employee():

    emp_id = input("Enter Employee ID to remove: ")

    for emp in employees:

        if emp["id"] == emp_id:
            employees.remove(emp)
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
    print("4. Remove Employee")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_employee()

    elif choice == "2":
        view_employees()

    elif choice == "3":
        search_employee()

    elif choice == "4":
        remove_employee()

    elif choice == "5":
        print("\nExiting system...")
        break

    else:
        print("\nInvalid choice.")