from tkinter import *
root=Tk()
root.title("Morse Code")
s=StringVar(root)
result=StringVar(root)
def binary():
    n=int(s.get())
    l=[]
    while n>=1:
        if n%2==0:
            l.append(0)
        elif n%2==1:
            l.append(1)
        else:
            l.append(1)
            break
        n=n//2
    l=l[::-1]
    c=''
    for i in l:
        c=c+str(i)
    global result
    result.set(str(c))
def octal():
    n=int(s.get())
    l=[]
    while True:
        if n//8<8:
            l.append(n%8)
            l.append(n//8)
            break
        else:
            l.append(n%8)
        n=n//8
    l=l[::-1]
    c=''
    for i in l:
        c=c+str(i)
    global result
    result.set(str(c))
def hexad():
    n=int(s.get())
    l=[]
    while True:
        if n//16<16:
            l.append(n%16)
            l.append(n//16)
            break
        else:
            l.append(n%16)
        n=n//16
    l=l[::-1]
    c=''
    for i in l:
        if i==10:
            c=c+'A'
        elif i==11:
            c=c+'B'
        elif i==12:
            c=c+'C'
        elif i==13:
            c=c+'D'
        elif i==14:
            c=c+'E'
        elif i==15:
            c=c+'F'
        else:
            c=c+str(i)
    global result
    result.set(str(c))
def encode():
    a=str(s.get())
    b=''
    for i in  a:
        if i==' ':
            b=b+'|'
        elif i.lower()=='a':
            b=b+'.-'
        elif i.lower()=='b':
            b=b+'-...'
        elif i.lower()=='c':
            b=b+'-.-.'
        elif i.lower()=='d':
            b=b+'-..'
        elif i.lower()=='e':
            b=b+'.'
        elif i.lower()=='f':
            b=b+'..-.'
        elif i.lower()=='g':
            b=b+'--.'
        elif i.lower()=='h':
            b=b+'....'
        elif i.lower()=='i':
            b=b+'..'
        elif i.lower()=='j':
            b=b+'.---'
        elif i.lower()=='k':
            b=b+'-.-'
        elif i.lower()=='l':
            b=b+'.-..'
        elif i.lower()=='m':
            b=b+'--'
        elif i.lower()=='n':
            b=b+'-.'
        elif i.lower()=='o':
            b=b+'---'
        elif i.lower()=='p':
            b=b+'.--.'
        elif i.lower()=='q':
            b=b+'--.-'
        elif i.lower()=='r':
            b=b+'.-.'
        elif i.lower()=='s':
            b=b+'...'
        elif i.lower()=='t':
            b=b+'-'
        elif i.lower()=='u':
            b=b+'..-'
        elif i.lower()=='v':
            b=b+'...-'
        elif i.lower()=='w':
            b=b+'.--'
        elif i.lower()=='x':
            b=b+'-..-'
        elif i.lower()=='y':
            b=b+'-.--'
        elif i.lower()=='z':
            b=b+'--..'
        elif i=='0':
            b=b+'----'
        elif i=='1':
            b=b+'.---'
        elif i=='2':
            b=b+'..---'
        elif i=='3':
            b=b+'...--'
        elif i=='4':
            b=b+'....-'
        elif i=='5':
            b=b+'.....'
        elif i=='6':
            b=b+'....'
        elif i=='7':
            b=b+'--...'
        elif i=='8':
            b=b+'---..'
        elif i=='9':
            b=b+'----.'
        b=b+' '
    global result
    result.set(str(b))
def decode():
    a=str(s.get())
    a=a.split()
    b=''
    for i in a:
        if i=='|':
            b=b+' '
        elif i==' ':
            b=b+''
        elif i=='.-':
            b=b+'a'
        elif i=='-...':
            b=b+'b'
        elif i=='-.-.':
            b=b+'c'
        elif i=='-..':
            b=b+'d'
        elif i=='.':
            b=b+'e'
        elif i=='..-.':
            b=b+'f'
        elif i=='--.':
            b=b+'g'
        elif i=='....':
            b=b+'h'
        elif i=='..':
            b=b+'i'
        elif i=='.---':
            b=b+'j'
        elif i=='-.-':
            b=b+'k'
        elif i=='.-..':
            b=b+'l'
        elif i=='--':
            b=b+'m'
        elif i=='-.':
            b=b+'n'
        elif i=='---':
            b=b+'o'
        elif i=='.--.':
            b=b+'p'
        elif i=='--.-':
            b=b+'q'
        elif i=='.-.':
            b=b+'r'
        elif i=='...':
            b=b+'s'
        elif i=='-':
            b=b+'t'
        elif i=='..-':
            b=b+'u'
        elif i=='...-':
            b=b+'v'
        elif i=='.--':
            b=b+'w'
        elif i=='-..-':
            b=b+'x'
        elif i=='-.--':
            b=b+'y'
        elif i=='--..':
            b=b+'z'
        elif i=='-----':
            b=b+'0'
        elif i=='.----':
            b=b+'1'
        elif i=='..---':
            b=b+'2'
        elif i=='...--':
            b=b+'3'
        elif i=='....-':
            b=b+'4'
        elif i=='.....':
            b=b+'5'
        elif i=='-....':
            b=b+'6'
        elif i=='--...':
            b=b+'7'
        elif i=='---..':
            b=b+'8'
        elif i=='----.':
            b=b+'9'
    global result
    result.set(str(b))
def dbin():
    n=int(s.get())
    a=str(n)[::-1]
    c=0
    for i in range (len(a)):
        c=c+(int(a[i])*(2**i))
    global result
    result.set(str(c))
def doct():
    n=int(s.get())
    a=str(n)[::-1]
    c=0
    for i in range (len(a)):
        c=c+(int(a[i])*(8**i))
    global result
    result.set(str(c))
def dhex():
    n=str(s.get())
    a=n[::-1]
    c=0
    for i in range (len(a)):
        if a[i]=='A':
            c=c+(10*(16**i))
        elif a[i]=='B':
            c=c+(11*(16**i))
        elif a[i]=='C':
            c=c+(12*(16**i))
        elif a[i]=='D':
            c=c+(13*(16**i))
        elif a[i]=='E':
            c=c+(14*(16**i))
        elif a[i]=='F':
            c=c+(15*(16**i))
        else:
            c=c+(int(a[i])*(16**i))
    global result
    result.set(str(c))
def cl1():
    if var1.get()==1:
        encode()
    elif var2.get()==1:
        binary()
    elif var3.get()==1:
        octal()
    elif var4.get()==1:
        hexad()
def cl2():
    if var1.get()==1:
        decode()
    elif var2.get()==1:
        dbin()
    elif var3.get()==1:
        doct()
    elif var4.get()==1:
        dhex()
var1=IntVar(root)
var2=IntVar(root)
var3=IntVar(root)
var4=IntVar(root)
chk1=Checkbutton(root,text='Morse Code',variable=var1)
chk2=Checkbutton(root,text='Binary',variable=var2)
chk3=Checkbutton(root,text='Octal',variable=var3)
chk4=Checkbutton(root,text='Hexadecimal',variable=var4)
label1=Label(root,text='Morse Code Encrypt/Decrypt')
label2=Label(root,text='Enter the string: ')
text1=Entry(root,textvariable=s)
button1=Button(root,text='Encrypt',command=cl1)
button2=Button(root,text='Decrypt',command=cl2)
label3=Label(root,textvariable=result)
button3=Button(root,text='Quit',command=root.quit)
label1.grid(row=0)
label2.grid(row=1,column=0)
text1.grid(row=1,column=1)
chk1.grid(row=2,column=0)
chk2.grid(row=2,column=1)
chk3.grid(row=3,column=0)
chk4.grid(row=3,column=1)
button1.grid(row=4,column=0)
button2.grid(row=4,column=1)
label3.grid(row=5)
button3.grid(row=6)
root.mainloop()

