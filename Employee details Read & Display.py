class Employee:
    def __init__(self):
        self.name=""
        self.department=""
        self.salary=0.0
        
    def readinfo(self):
        self.name=input("Enter your name : ")
        self.department=input("Enter your Department : ")
        self.salary=float(input("Enter your Salary : "))
                          
    def dispinfo(self):
        print("Name of employee is : "+self.name)
        print("Department of employee is : "+self.department)
        print("Salary of employee is : ",self.salary)
        
employee= Employee()

employee.readinfo()
employee.dispinfo()
