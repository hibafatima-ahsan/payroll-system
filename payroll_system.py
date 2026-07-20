import json

FILE_NAME = "employees.json"


# ----------------------------
# Load Employees
# ----------------------------
def load_employees():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


# ----------------------------
# Save Employees
# ----------------------------
def save_employees(employees):
    with open(FILE_NAME, "w") as file:
        json.dump(employees, file, indent=4)


# ----------------------------
# Calculate Salary
# ----------------------------
def calculate_salary(basic_salary):
    bonus = basic_salary * 0.10
    tax = basic_salary * 0.05
    net_salary = basic_salary + bonus - tax

    return bonus, tax, net_salary


# ----------------------------
# Add Employee
# ----------------------------
def add_employee():
    employees = load_employees()

    emp_id = input("Employee ID: ")
    name = input("Employee Name: ")
    department = input("Department: ")

    while True:
        try:
            basic_salary = float(input("Basic Salary: "))
            break
        except ValueError:
            print("Invalid Salary!")

    bonus, tax, net_salary = calculate_salary(basic_salary)

    employee = {
        "id": emp_id,
        "name": name,
        "department": department,
        "basic_salary": basic_salary,
        "bonus": bonus,
        "tax": tax,
        "net_salary": net_salary
    }

    employees.append(employee)
    save_employees(employees)

    print("\nEmployee Added Successfully!\n")


# ----------------------------
# View Employees
# ----------------------------
def view_employees():
    employees = load_employees()

    if not employees:
        print("\nNo Employee Found\n")
        return

    print("\n========== Employee List ==========\n")

    for emp in employees:
        print(f"ID         : {emp['id']}")
        print(f"Name       : {emp['name']}")
        print(f"Department : {emp['department']}")
        print(f"Basic      : ${emp['basic_salary']}")
        print(f"Bonus      : ${emp['bonus']}")
        print(f"Tax        : ${emp['tax']}")
        print(f"Net Salary : ${emp['net_salary']}")
        print("-" * 35)


# ----------------------------
# Search Employee
# ----------------------------
def search_employee():
    employees = load_employees()

    emp_id = input("Enter Employee ID: ")

    for emp in employees:
        if emp["id"] == emp_id:
            print("\nEmployee Found\n")
            print(emp)
            return

    print("Employee Not Found")


# ----------------------------
# Update Salary
# ----------------------------
def update_salary():
    employees = load_employees()

    emp_id = input("Enter Employee ID: ")

    for emp in employees:

        if emp["id"] == emp_id:

            while True:
                try:
                    new_salary = float(input("New Basic Salary: "))
                    break
                except ValueError:
                    print("Invalid Salary!")

            bonus, tax, net_salary = calculate_salary(new_salary)

            emp["basic_salary"] = new_salary
            emp["bonus"] = bonus
            emp["tax"] = tax
            emp["net_salary"] = net_salary

            save_employees(employees)

            print("Salary Updated Successfully!")
            return

    print("Employee Not Found")


# ----------------------------
# Delete Employee
# ----------------------------
def delete_employee():
    employees = load_employees()

    emp_id = input("Enter Employee ID: ")

    for emp in employees:

        if emp["id"] == emp_id:
            employees.remove(emp)
            save_employees(employees)

            print("Employee Deleted Successfully!")
            return

    print("Employee Not Found")


# ----------------------------
# Payroll Summary
# ----------------------------
def payroll_summary():
    employees = load_employees()

    total_salary = sum(emp["net_salary"] for emp in employees)

    print("\n========== Payroll Summary ==========")
    print("Total Employees :", len(employees))
    print("Total Payroll   : $", total_salary)
# ----------------------------
# Display Highest Salary
# ----------------------------
def display_highest_salary():
    employees = load_employees()

    if not employees:
        print("\nNo Employee Found!\n")
        return

    highest_paid = max(employees, key=lambda emp: emp["net_salary"])

    print("\n========== Highest Salary Employee ==========\n")
    print(f"ID         : {highest_paid['id']}")
    print(f"Name       : {highest_paid['name']}")
    print(f"Department : {highest_paid['department']}")
    print(f"Basic      : ${highest_paid['basic_salary']}")
    print(f"Bonus      : ${highest_paid['bonus']}")
    print(f"Tax        : ${highest_paid['tax']}")
    print(f"Net Salary : ${highest_paid['net_salary']}")

# ----------------------------
# Menu
# ----------------------------
def menu():

    while True:

        print("\n========== Employee Payroll System ==========")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Update Salary")
        print("5. Delete Employee")
        print("6. Payroll Summary")
        print("7. Display Highest Salary")
        print("8. Exit")
        choice = input("Enter Choice: ")

        if choice == "1":
            add_employee()

        elif choice == "2":
            view_employees()

        elif choice == "3":
            search_employee()

        elif choice == "4":
            update_salary()

        elif choice == "5":
            delete_employee()

        elif choice == "6":
            payroll_summary()

        elif choice == "7":
            display_highest_salary()
        elif choice=="8":    
            print("Thank You!")
            break
        else:
            print("Invalid Choice")


menu()