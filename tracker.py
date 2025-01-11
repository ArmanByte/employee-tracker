import datetime

# Employee class (coming soon)
class Employee:
    def __init__(self, id, name, surname, birth, position, start_date, salary):
        self.id = id
        self.name = name
        self.surname = surname
        self.birth = birth
        self.position = position
        self.start_date = start_date
        self.salary = salary

# Menu
def menu():
    read_log()
    print("1: Add employee.\n2: Edit employee.\n3: Remove employee.\n")
    choice = input("Choice: ")
    if choice == "1":
        add_employee()
    elif choice == "2": 
        edit_employee()
    elif choice == "3":
        remove_employee()
    else:
        print("Wrong choice, try again (1/2/3).\n")
        menu()

# Read Log File
def read_log():
    log_id = 1
    try:
        with open('data.txt', 'r') as file:
            global get_id
            lines = file.readlines()
            get_id = int(lines[log_id].strip())
            get_id += 1
            lines[log_id] = str(get_id) + "\n"

        # Write updated ID back to file
        with open('data.txt', 'w') as file:
            file.writelines(lines)

    except FileNotFoundError:
        print("Log file not found.")
        exit()
    except ValueError:
        print("Log file value error.")
        exit()

# Add Employee Information
def add_employee():
    print("Adding new employee. Enter employee information.\n")
    employee_name = input("Enter employee name: ")
    employee_surname = input("Enter employee surname: ")
    employee_position = input("Employee position: ")
    employee_birth = input("Enter employee date of birth (Day/Month/Year): ")
    employee_salary = input("Enter employee salary (Month/USD): ")
    date_now = datetime.datetime.now()
    date_of_employment = date_now.strftime("%d/%m/%Y")
    
    try:
        with open('workers.txt', 'a') as file:
            file.write(f"Employee ID: {str(get_id)}.\n")
            file.write(f"Name: {employee_name}.\n")
            file.write(f"Surname: {employee_surname}.\n")
            file.write(f"Position: {employee_position}.\n")
            file.write(f"Start Date: {date_of_employment}.\n")
            file.write(f"Date of Birth: {employee_birth}.\n")
            file.write(f"Salary: {employee_salary} USD.\n\n")
    except FileNotFoundError:
        print("File not found.")
        exit()

# Edit Employee Information (Coming Soon)
def edit_employee():
    print("Enter employee ID to make changes.")
    employee_id = input("Employee ID: ")
    # Coming Soon...

# Remove Employee Information (Coming Soon)
def remove_employee():
    print("Removing employee. Enter employee ID.")
    employee_id = input("Employee ID:")
    # Coming Soon...

menu()

print("Added again. new feature2")