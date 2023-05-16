class Error (Exception):
    print("Value cant be 0.")

number=0
try:
    if number == 0:
        raise Error
    else:
        print("Value is more than 0.")
except Error:
    pass