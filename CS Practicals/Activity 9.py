def factorial(n):
    f=1
    for i in range (1,n+1):
        f=f*i
    return f
def pascal(n):
    for i in range (n):
        for j in range (1,n-i):
            print(" ",end='')
        for k in range (0,i+1):
            c=int(factorial(i)/(factorial(k)*factorial(i-k)))
            print(" ",c,end="")
        print()
n=int(input("Enter the number of rows: "))
pascal(n)