from tkinter import *
import pyshorteners as ps
import pyperclip

root=Tk()
root.title("URL Shortener")
root.resizable(False,False)

s=StringVar(root)
r=StringVar(root)

def shorten():
	n=str(s.get())
	k=ps.Shortener()
	m=k.tinyurl.short(n)
	global r
	r.set(str(m))
	
def copy_to_clipboard():
	pyperclip.copy(r.get())
	
label1=Label(root,text="Enter the URL: ")
text1=Entry(root,textvariable=s,width=40)
button1=Button(root,text="Shorten",command=shorten)
label2=Label(root,text="Shortened URL: ")
text2=Entry(root,textvariable=r,width=40)
button2=Button(root,text="Copy",command=copy_to_clipboard)
button3=Button(root,text="Quit",command=root.destroy)

label1.grid(row=1,column=0,sticky=W)
text1.grid(row=1,column=1)
button1.grid(row=2,sticky=N+S+E+W)
label2.grid(row=3,column=0,sticky=W)
text2.grid(row=3,column=1)
button2.grid(row=4,column=0,sticky=W+E+N+S)
button3.grid(row=4,column=1,sticky=N+S+E+W)

root.mainloop()
