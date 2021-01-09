#Activity 7

def count(n):
    a = len(str(n))
    print(a)

def reverse(n):
    print(str(n)[::-1])

def hasdigit(n):
    if str(n).isdigit() == True:
        print(True)
    else:
        print(False)

def show(n):
    a = len(str(n))
    s = ''
    for i in (str(n)):
        if a != 0:
            s += str(int(i) * (10 ** (a-1))) + '+'
        else:
            s += str(int(i) * (10**(a-1)))
        a-=1
    print(s)

n=int(input('Enter a number: '))
count(n)
reverse(n)
hasdigit(n)
show(n)