#Activity 10

def binary(n):
    l = []
    while n >= 1:
        if n % 2 == 0:
            l.append(0)
        elif n % 2 == 1:
            l.append(1)
        else:
            l.append(1)
            break
        n = n // 2
    l = l[::-1]
    s = ''.join(map(str, l))
    print(s)

def octal(n):
    l = []
    while True:
        if n // 8 < 8:
            l.append(n % 8)
            l.append(n // 8)
            break
        else:
            l.append(n % 8)
        n = n // 8
    l = l[::-1]
    s = ''.join(map(str, l))
    print(s)

def hex(n):
    l = []
    while True:
        if n // 16 < 16:
            l.append(n % 16)
            l.append(n // 16)
            break
        else:
            l.append(n % 16)
        n=n // 16
    l = l[::-1]
    s = ''
    for i in l:
        if i == 10:
            s += 'A'
        elif i == 11:
            s += 'B'
        elif i == 12:
            s += 'C'
        elif i == 13:
            s += 'D'
        elif i == 14:
            s += 'E'
        elif i == 15:
            s += 'F'
        else:
            s += str(i)
    print(s)

while True:
    n = int(input("Enter the Number: "))
    d = input("Enter 'B' for binary, 'O' for octal, 'H' for hexa-decimal or 'E' to exit: ")
    if d == 'B':
        binary(n)
    elif d == 'O':
        octal(n)
    elif d == 'H':
        hex(n)
    elif d == 'E':
        print("Terminating Program")
        break
    else:
        print("Enter a correct input")