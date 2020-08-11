from tkinter import *
from tkinter import ttk
from googletrans import Translator
from tkinter import messagebox
import pyperclip

root=Tk()
root.title("Translator")
root.resizable(False,False)

def translate():
	l1=text1.get("1.0","end-1c")
	cl=chooseLang.get()
	if l1=='':
		messagebox.showerror('Translator','Enter valid text')
	else:
		t=Translator()
		r=t.translate(l1,dest=cl)
		text2.insert('end',r.text)
		
def clear():
	text1.delete(1.0,'end')
	text2.delete(1.0,'end')
	
def copy_to_clipboard():
	pyperclip.copy(text2.get("1.0","end-1c"))
	
s=StringVar(root)
d=ttk.Combobox(root,width=20,textvariable=s,state='readonly')
d['values']=('Auto\ Detect')
d.current(0)

p=StringVar(root)
chooseLang=ttk.Combobox(root,width=20,textvariable=p,state='readonly')
chooseLang['values']=('Afrikaans','Albanian','Arabic','Armenian',' Azerbaijani','Basque','Belarusian','Bengali','Bosnian','Bulgarian','Catalan','Cebuano','Chichewa','Chinese','Corsican','Croatian','Czech','Danish','Dutch','English','Esperanto','Estonian','Filipino','Finnish','French','Frisian','Galician','Georgian','German','Greek','Gujarati','Haitian Creole','Hausa','Hawaiian','Hebrew','Hindi','Hmong','Hungarian','Icelandic','Igbo','Indonesian','Irish','Italian','Japanese','Javanese','Kannada','Kazakh','Khmer','Kinyarwanda','Korean','Kurdish','Kyrgyz','Lao','Latin','Latvian','Lithuanian','Luxembourgish','Macedonian','Malagasy','Malay','Malayalam','Maltese','Maori','Marathi','Mongolian','Myanmar','Nepali','Norwegian''Odia','Pashto','Persian','Polish','Portuguese','Punjabi','Romanian','Russian','Samoan','Scots Gaelic','Serbian','Sesotho','Shona','Sindhi','Sinhala','Slovak','Slovenian','Somali','Spanish','Sundanese','Swahili','Swedish','Tajik','Tamil','Tatar','Telugu','Thai','Turkish','Turkmen','Ukrainian','Urdu','Uyghur','Uzbek','Vietnamese','Welsh','Xhosa''Yiddish','Yoruba','Zulu')
chooseLang.current(0)

text1=Text(root,width=30,height=10,borderwidth=5)
text2=Text(root,width=30,height=10,borderwidth=5)
button0=Button(root,text="Translate",command=translate)
button1=Button(root,text="Clear",command=clear)
button2=Button(root,text="Copy",command=copy_to_clipboard)
button3=Button(root,text="Quit",command=root.destroy)

d.grid(row=1,column=0,sticky=W+E+N+S)
chooseLang.grid(row=1,column=1,sticky=W+E+N+S)
text1.grid(row=3,column=0,sticky=W+E+N+S)
text2.grid(row=3,column=1,sticky=W+E+N+S)
button0.grid(row=5,column=0,sticky=W+E+N+S)
button2.grid(row=5,column=1,sticky=W+E+N+S)
button1.grid(row=6,column=0,sticky=W+E+N+S)
button3.grid(row=6,column=1,sticky=W+E+N+S)

root.mainloop()
