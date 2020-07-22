from tkinter import *
root=Tk()
root.title("Encrypt/Decrypt")
def encrypt():
    a=str(s.get())
    s1=''
    for i in a:
        if i.isalpha():
            s1=s1+chr(ord(i)+1)
        elif i.isdigit():
            s1=s1+chr(ord(i)+2)
        else:
            s1=s1+i
    global result
    result.set(str(s1))
def decrypt():
    a=str(s.get())
    s1=''
    for i in a:
        if ord(i) in range (65,93) or ord(i) in range (97,124):
            s1=s1+chr(ord(i)-1)
        elif ord(i) in range(48,61):
            s1=s1+chr(ord(i)-2)
        else:
            s1=s1+i
    global result
    result.set(str(s1))
s=StringVar(root)
result=StringVar(root)
label1=Label(root,text='Encryption/Decryption')
label2=Label(root,text='Enter the string')
text1=Entry(root,textvariable=s)
button1=Button(root,text='Encrypt',command=encrypt)
button2=Button(root,text='Decrypt',command=decrypt)
label3=Label(root,textvariable=result)
label1.grid(row=0)
label2.grid(row=1,column=0)
text1.grid(row=1,column=1)
button1.grid(row=2,column=0)
button2.grid(row=2,column=1)
label3.grid(row=3)
root.mainloop()
