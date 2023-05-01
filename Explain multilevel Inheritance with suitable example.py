
#Multilevel Inheritance: When a child class becomes a parent class for another child class. 

class Parent:
    def fun1(self):
        print("This is Parent Function")
class Child(Parent):
    def fun2(self):
        print("This is First child function")
class Child1(Child):
    def fun3(self):
        print("This is Second child function")
ob=Child1()
ob.fun1()
ob.fun2()
ob.fun3()
