from pygame import mixer  
from gtts import gTTS 
import os 
from tkinter import*
r=Tk()
e=Entry(r)
e.pack()

def create():
	try:
		os.remove("C:\\Users\\MANISH\\Desktop\\text-speech2.mp3")
	except:
		print ("ok")
	tex=e.get()
	language ="hi"
	myobj = gTTS(text=tex, lang=language, slow=False) 
	myobj.save('C:\\Users\\MANISH\\Desktop\\text-speech2.mp3')
	mixer.init()
	mixer.music.load('C:\\Users\\MANISH\\Desktop\\text-speech2.mp3')
	mixer.music.play()
   

b=Button(r,text='play',command=create)
b.pack()
r.mainloop()
