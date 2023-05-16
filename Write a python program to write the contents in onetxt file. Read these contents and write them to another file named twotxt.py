print("how many lines you want to write : ")
n=int(input())
outfile=open("one.txt","wt")
for i in range(n):
    print("Enter the line..")
    line=input()
    outfile.write("\n"+line)
outfile.close()

infile=open("one.txt","rt")
outfile=open("two.txt","wt")
i=0
for i in range(n+1):
    line=infile.readline()
    outfile.write("\n"+line)
infile.close()
outfile.close()

infile=open("two.txt","rt")
print(infile.read())
infile.close()
