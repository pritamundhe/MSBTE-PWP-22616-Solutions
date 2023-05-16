#Single Inheritance

class Parent:
    def fun1(self):
        print("This is fun1 of Parent class")
    
class Child(Parent):
    def fun2(self):
        print("This is fun2 of Child class")

ob=Child()
ob.fun1()
ob.fun2()
