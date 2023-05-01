class Employee:
    def read_employee_info(self):
        self.name=input("Enter Name : ")
        self.department=input("Enter Department : ")
        self.salary=float(input("Enter Salary : "))
    def print_employee_info(self):
        print("Name : ",self.name)
        print("Department : ",self.department)
        print("Salary : ",self.salary)
ob=Employee()
ob.read_employee_info()
ob.print_employee_info()
