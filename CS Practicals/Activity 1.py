f=open("1.txt","w")
f.write("I'm a master coder\n")
f.write("I know python and C++\n")
f.close()
f=open("1.txt","r")
x=f.read().splitlines()
print(x[-1])
s=f.readline()
print(s[10:])
n=int(input("Enter the line number: "))
for i in range (len(x)):
    if i==(n-1):
        print(x[i])
    else:
        break
f.close()
f=open("1.txt")
a=f.read().split()
c=0
for i in a:
    if i[0] not in a:
        c=1
    else:
        c+=1
    print("Words beginning with ",i[0],"are: ",c)
f.close()
