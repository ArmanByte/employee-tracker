class Employee:
    def __init__(self, id, name, surname, birth, position, start_date, salary):
        self.id = id
        self.name = name
        self.surname = surname
        self.birth = birth
        self.position = position
        self.start_date = start_date
        self.salary = salary

def add_employee():
    print("Adding new employee. Enter employee information.\n")
    new_employee_name = input("Enter employee name: ")
    new_employee_surname = input("Enter employee surname: ")
    new_employee_age = input("Enter employee date of birth (day/month/year): ")

def edit_employee():
    print("Enter employee id to make changes.")
    edit_employee_id = input("Employee id: ")
    
def remove_employee():
    print("Removing employee. Enter employee id.")