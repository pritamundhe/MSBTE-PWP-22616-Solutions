class BaseClass1 
#Body of base class 
class DerivedClass(BaseClass1):
    - 

class Example: 
    parentname = ""     
    childname = ""      
    def show_parent(self):      
        print(self.parentname) 


class Child(Parent):     
    def show_child(self):         
        print(self.childname) 
ch1 = Child()    	 	
ch1.parentname = "Vijay"   
ch1.childname = "Parth" 
ch1.show_parent()     
ch1.show_child()     	 	
