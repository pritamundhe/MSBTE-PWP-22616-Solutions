
#Function overriding: When child class has a definition for one of the member functions
#of parent class.That parent function is said to be overridden.

class A:
    def explore(self):
        print("explore() method of class A")
class B(A):
    def explore(self):
        print("explore() method of class B")
a_ob=A()
b_ob=B()
a_ob.explore()
b_ob.explore()
