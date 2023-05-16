n=int(input("Enter value of n : "))
a=0
b=1
i=0
print("Fibonacci series is..")
while i<n:
    print(a)
    c=a+b
    a=b
    b=c
    i=i+1
