def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

num=int(input("Enter number to find factorial"))

if num<0:
        print("Factorial is not defined for nr=egative numbers!!")
else:
    result=factorial(num)
    print("Factorial of : ",num," is ",result)
