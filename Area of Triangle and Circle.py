import math

base=float(input("Enter the base of triangle : "))
height=float(input("Enter the height of triangle :"))

radius=float(input("Enter radius of circle : "))

atriangle=0.5*base*height
print("Area of trianngle is : ",atriangle)

acircle=math.pi*radius**2
print("Area of Circle is : ",acircle)
