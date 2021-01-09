#Activity 12

from tkinter import *

def si():
    a = int(p.get())
    b = int(t.get())
    c = int(r.get())
    s = (a * b * c) / 100
    global result
    result.set(str(s))

root = Tk()
root.title('SI Calculator')

p = StringVar(root)
t = StringVar(root)
r = StringVar(root)
result = StringVar(root)

label1 = Label(root, text = 'Simple Interest Calculator')
label2 = Label(root, text = 'Enter the principal amount: ')
text1 = Entry(root, textvariable = p)
label3 = Label(root, text = 'Enter the time period: ')
text2 = Entry(root, textvariable = t)
label4 = Label(root, text = 'Enter the rate of interest: ')
text3 = Entry(root, textvariable = r)

label1.grid(row = 0)
label2.grid(row = 1, column = 0)
text1.grid(row = 1, column = 1)
label3.grid(row = 2, column = 0)
text2.grid(row = 2, column = 1)
label4.grid(row = 3, column = 0)
text3.grid(row = 3, column = 1)

label5 = Label(root, textvariable = result)
button1 = Button(root, text = 'Submit', command = si)
button1.grid(row = 4)
label5.grid(row = 5)
root.mainloop()