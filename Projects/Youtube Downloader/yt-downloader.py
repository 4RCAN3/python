from tkinter import *
from pytube import Youtube

root=Tk()
root.title("YT Downloader")
root.resizable(False,False)

s=StringVar(root)
r=StringVar(root)
p=StringVar(root)

def download():
	try:
		p.set("Downloading...")
		root.update()
		Youtube(s.get()).streams.first().download()
		p.set("Video downloaded")
	except:
		p.set("Error")
		root.update()
		p.set("Enter a valid link")

label1=Label(root,text="Enter the video link")
text1=Entry(root,textvariable=s)
label2=Label(root,textvariable=p)
text2=Entry(root,textvariable=r)
button1=Button(root,text="Download",command=download)
button2=Button(root,text="Quit",command=root.destroy)
label3=Label(root,image=pic)

