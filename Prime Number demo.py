def primedemo(num):
    flag=0
    for i in range(2,num):
        if(num%i==0):
            flag=1
            break
    if(flag==0):
        print(num,"is a prime number")
    else:
        print(num,"is not a prime number")

primedemo(int(input("Enter a Number : ")))
