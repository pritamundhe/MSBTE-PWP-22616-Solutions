def validate(value):
    if value<0:
        raise ValueError("Value cannot be less than 0 ")

try:
    num=int(input("Enter a value : "))
    validate(num)
    print("Value is valid")

except ValueError as e:
    print("Error : "+str(e))
