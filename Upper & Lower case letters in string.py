def strdemo(s):
    upc = 0
    lc = 0
    for i in s:
        if i.isupper():
            upc += 1
        if i.islower():
            lc += 1
    return upc, lc

uc, lc = strdemo(input("Enter a String: "))

print("Number of Upper case letters are:", uc)
print("Number of Lower case letters are:", lc)
