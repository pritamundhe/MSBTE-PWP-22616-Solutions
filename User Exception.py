class Employee:
    def __init__(self):
        self.id = ""
        self.name = ""

    def read_employee_info(self):
        self.id = input("Enter employee id: ")
        self.name = input("Enter name: ")
       
    def print_employee_info(self):
        print("Employee Information:")
        print("id:", self.id)
        print("name:", self.name)
       

employee = Employee()

employee.read_employee_info()
employee.print_employee_info()
