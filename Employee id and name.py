class Employee:
    def __init__(self):
        self.id=""
        self.name=""

    def readin(self):
        self.id=int(input("Enter your id :"))
        self.name=input("Enter your name :")

    def printin(self):
        print("Employee id is : ",self.id)
        print("Employee name is : "+self.name)

employee= Employee()

employee.readin()
employee.printin()
