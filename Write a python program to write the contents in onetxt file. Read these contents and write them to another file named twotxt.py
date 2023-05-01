
n=int(input("How many lines you want to write: "))

with open("one.txt","w") as outfile:
    for i in range(n):
        line=input("Enter the line :")
        outfile.write(line+"\n")

with open("one.txt","r") as infile, open("two.txt","w") as outfile:
    for linr in infile:
        outfile.write(line)

print("The contents of files are...")
with open("two.txt","r") as infile:
    print(infile.read())
