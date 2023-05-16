#Hirarchical Inheritance

class Parent:
    def fun1(self):
        print("This is fun1 of Parent class")
    
class Child(Parent):
    def fun2(self):
        print("This is fun2 of Child class")

class child(Parent):
    def fun3(self):
        print("Hello i am class 3")

ob=child()
ob1=Child()
ob.fun1()
ob1.fun2()
ob.fun3()
