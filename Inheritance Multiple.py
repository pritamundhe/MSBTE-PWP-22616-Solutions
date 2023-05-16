#Multiple Inheritance

class Parent:
    def fun1(self):
        print("This is fun1 of Parent class")
    
class Child:
    def fun2(self):
        print("This is fun2 of Child class")

class child(Parent,Child):
    def fun3(self):
        print("Hello i am class 3")

ob=child()
ob.fun1()
ob.fun2()
ob.fun3()
