from tkinter import *
from tkinter import ttk
from pytube import YouTube
import time

root=Tk()
root.title("YT Downloader")
root.resizable(False,False)

s=StringVar(root)
p=StringVar(root)
pic=PhotoImage(file="./main.PNG")

def download():
	try:
		def bar():
			pb['value'] = 20
			root.update_idletasks() 
			time.sleep(1) 
			pb['value'] = 40
			root.update_idletasks() 
			time.sleep(1) 
			pb['value'] = 50
			root.update_idletasks() 
			time.sleep(1) 
			pb['value'] = 60
			root.update_idletasks() 
			time.sleep(1) 
			pb['value'] = 80
			root.update_idletasks() 
			time.sleep(1) 
			pb['value'] = 100
		p.set("Downloading...")
		root.update()
		bar()
		YouTube(s.get()).streams.first().download()
		p.set("Downloaded")
	except:
		p.set("Error")
		root.update()
		p.set("Enter a valid link")

label1=Label(root,text="Enter the video link:")
text1=Entry(root,textvariable=s)
label2=Label(root,textvariable=p)
button1=Button(root,text="Download",command=download)
button2=Button(root,text="Quit",command=root.destroy)
label3=Label(root,image=pic)
pb=ttk.Progressbar(root, orient=HORIZONTAL, mode='determinate') 

label3.grid(row=1,columnspan=2,rowspan=2,sticky=N+S)
label1.grid(row=3,column=0)
text1.grid(row=3,column=1,sticky=W+E+N+S)
label2.grid(row=4,column=0)
pb.grid(row=4,column=1,sticky=W+E+N+S)
button1.grid(row=5,column=0,sticky=W+E+N+S)
button2.grid(row=5,column=1,sticky=W+E+N+S)
root.mainloop()
