from tkinter import *
from tkinter import ttk
from googletrans import Translator
from tkinter import messagebox
import gtts
import os
from datetime import *
from playsound import playsound
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

def osp():
	d={'af': 'Afrikaans', 'sq': 'Albanian', 'ar': 'Arabic', 'hy': 'Armenian', 'bn': 'Bengali', 'bs': 'Bosnian', 'ca': 'Catalan', 'hr': 'Croatian', 'cs': 'Czech', 'da': 'Danish', 'nl': 'Dutch', 'en': 'English', 'eo': 'Esperanto', 'et': 'Estonian', 'tl': 'Filipino', 'fi': 'Finnish', 'fr': 'French', 'de': 'German', 'el': 'Greek', 'gu': 'Gujarati', 'hi': 'Hindi', 'hu': 'Hungarian', 'is': 'Icelandic', 'id': 'Indonesian', 'it': 'Italian', 'ja': 'Japanese', 'jw': 'Javanese', 'kn': 'Kannada', 'km': 'Khmer', 'ko': 'Korean', 'la': 'Latin', 'lv': 'Latvian', 'mk': 'Macedonian', 'ml': 'Malayalam', 'mr':'Marathi', 'my': 'Myanmar (Burmese)', 'ne': 'Nepali', 'no': 'Norwegian', 'pl': 'Polish', 'pt': 'Portuguese', 'ro': 'Romanian', 'ru': 'Russian', 'sr': 'Serbian', 'si': 'Sinhala', 'sk': 'Slovak', 'es': 'Spanish', 'su': 'Sundanese', 'sw': 'Swahili', 'sv': 'Swedish', 'ta': 'Tamil', 'te': 'Telugu', 'th': 'Thai', 'tr': 'Turkish', 'uk': 'Ukrainian', 'ur': 'Urdu', 'vi': 'Vietnamese', 'cy': 'Welsh', 'zh-cn': 'Chinese', 'en-us': 'English', 'fr-fr': 'French', 'pt-pt': 'Portuguese', 'es-es': 'Spanish'}
	t=text2.get("1.0","end-1c")
	c=chooseLang.get()
	if c in d.values():
		e=list(d.keys())[list(d.values()).index(c)]
		tts=gtts.gTTS(str(t),lang=str(e))
		ds=datetime.now().strftime("%d%m%Y%H%M%S")
		f="new"+ds+".mp3"
		tts.save(f)
		playsound(f)
		os.remove(f)
	else:
		messagebox.showerror("Error","Language not supported")
	
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
button5=Button(root,text="Output -> Speech",command=osp)

d.grid(row=1,column=0,sticky=W+E+N+S)
chooseLang.grid(row=1,column=1,sticky=W+E+N+S)
text1.grid(row=3,column=0,sticky=W+E+N+S)
text2.grid(row=3,column=1,sticky=W+E+N+S)
button0.grid(row=5,column=0,sticky=W+E+N+S)
button2.grid(row=5,column=1,sticky=W+E+N+S)
button5.grid(row=6,columnspan=2,sticky=W+E+N+S)
button1.grid(row=7,column=0,sticky=W+E+N+S)
button3.grid(row=7,column=1,sticky=W+E+N+S)

root.mainloop()
