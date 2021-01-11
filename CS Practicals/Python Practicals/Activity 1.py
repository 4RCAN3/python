#Activity 1

def create_file():
	f = open("1.txt", "a")
	f.write('Neither apple nor pine are in pineapple. Boxing rings are square\n')
	f.write('Writers write, but fingers don’t fing. Overlook and oversee are opposites.\n')
	f.write('A house can burn up as it burns down. An alarm goes off by going on.\n')
	f.close()

create_file()

#1
f = open("1.txt")
print(f.read())
f.close()

#2
f = open("1.txt", "a")
f.write("I like to code\n")
f.write("I'm a python developer\n")
f.close()

#3
f = open("1.txt", "r")
x = f.read().splitlines()
print(x[-1])

#4
s = f.readline()
print(s[10:])

#5
n = int(input("Enter the line number: "))
for i in range (len(x)):
    if i == (n - 1):
        print(x[i])
    else:
        break
f.close()

#6
f = open("1.txt")
a = f.read().split()
c = 0
for i in a:
    if i[0] not in a:
        c = 1
    else:
        c += 1
    print(f"Words beginning with {i[0]} are: {c}")
f.close()
