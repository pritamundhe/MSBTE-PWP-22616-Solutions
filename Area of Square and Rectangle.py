class area:
    def display(self,l,b=None):
        if(b==None):
            print("Area of square is : ",l*l)
        else:
            print("Area of rectangle is : ",l*b)
a=area()
a.display(9)
a.display(2,5)