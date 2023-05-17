class intchar:
    def display(self,a,b):
        if(type(a)==int):
            print("Integer : ",a)
            print("Character : ",b)
        else:
            print("Interger : ",b)
            print("Character : ",a)
In=intchar()
print(display(1,'Pritam'))
print(display('Pritam',8))