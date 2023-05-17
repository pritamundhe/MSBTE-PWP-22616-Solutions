class degree:
    def getDegree(self):
        print("I got Degree!")

class undergraduate(degree):
    def getDegree(self):
        print("I am undergreduate!")

class postgraduate(degree):
    def getDegree(self):
        print("I am a postgraduate!")

d=degree()
d.getDegree()
u=undergraduate()
u.getDegree()
p=postgraduate()
p.getDegree()