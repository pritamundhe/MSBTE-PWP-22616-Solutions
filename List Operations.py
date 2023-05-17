L=[10,20,30,40,50,60,70,80,90,100]
L2=[20,40,60,80,100]

print("items in list = ",L)
print("Sum is : ",sum(L))

print("Multiplication of list elements using for loop : ")
mul=1
for i in L:
    mul=mul*i
print(mul)

print("Largest Number  is : ",max(L))
print("Smallest Number  is : ",min(L))
L.reverse()
print("Reverse List : ",L)


print("Original elements ",L)
for i in L:
    if(i%2==0):
        print(i)
