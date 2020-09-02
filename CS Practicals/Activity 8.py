n=int(input('Enter a number: '))
#1
def Generatefactors(n):
    l=[]
    for i in range (1,int(n//2)+1):
        if n%i==0:
            l.append(i) 
    return l

#2
def isPrimeNo(n):
    flag=False
    for i in range (2,int(n**0.5)+1):
        if n%i==0:
            flag=True
            break
    if flag==True:
        print('{} is not a prime number'.format(n))
    else:
        print('{} is a prime number'.format(n))
isPrimeNo(n)

#3
def isPerfectNo(n):
    ln=Generatefactors(n)
    if sum(ln)==n:
        print('{} is a perfect number'.format(n))
    else:
        print('{} is not a perfect number'.format(n))
isPerfectNo(n)
