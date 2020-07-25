from tkinter import *
root=Tk()
root.title("Morse Code")
s=StringVar(root)
result=StringVar(root)
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
label1=Label(root,text='Morse Code Encrypt/Decrypt')
label2=Label(root,text='Enter the code: ')
text1=Entry(root,textvariable=s)
button1=Button(root,text='Encrypt',command=encode)
button2=Button(root,text='Decrypt',command=decode)
label3=Label(root,textvariable=result)
label1.grid(row=0)
label2.grid(row=1,column=0)
text1.grid(row=1,column=1)
button1.grid(row=2,column=0)
button2.grid(row=2,column=1)
label3.grid(row=3)
root.mainloop()
