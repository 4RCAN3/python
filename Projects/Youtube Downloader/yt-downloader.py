from tkinter import *
from pytube import YouTube

root=Tk()
root.title("YT Downloader")
root.resizable(False,False)

s=StringVar(root)
p=StringVar(root)
pic=PhotoImage(file="./main.PNG")

def download():
	try:
		p.set("Downloading...")
		root.update()
		YouTube(s.get()).streams.first().download()
		p.set("Video downloaded, saved in current directory")
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

label3.grid(row=1,columnspan=2,rowspan=2,sticky=N+S)
label1.grid(row=3,column=0)
text1.grid(row=3,column=1)
label2.grid(row=4,sticky=N)
button1.grid(row=5,column=0,sticky=W+E+N+S)
button2.grid(row=5,column=1,sticky=W+E+N+S)
root.mainloop()
