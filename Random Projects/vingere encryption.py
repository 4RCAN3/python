def encode():
    n=input("Enter a string: ")
    k=input("Enter the key: ")
    s=''
    a=[ord(i) for i in (n)]
    b=[ord(j) for j in (k)]
    for x in range (len(n)):
        d=(a[x]+b[x%len(k)])%26
        s=s+chr(65+d)
    print(s)
def decode():
    n=input("Enter a string: ")
    k=input("Enter the key: ")
    s=''
    a=[ord(i) for i in (n)]
    b=[ord(j) for j in (k)]
    for x in range (len(n)):
        d=(a[x]-b[x%len(k)])%26
        s=s+chr(65+d)
    print(s)
while (True):
    print("1. Encode")
    print("2. Decode")
    print("3. Exit")
    v=int(input("Enter your choice: "))
    if v==(1):
        encode()
    elif v==(2):
        decode()
    elif v==(3):
        break
    else:
        print("Enter a correct input.")