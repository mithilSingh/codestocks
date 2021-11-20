import tkinter
import gtts
from playsound import playsound
import os
from tkinter import *
from time import sleep
    
pos=0
def proced(text):
    global lrec,l,f,word
    f=Frame(root,height= 500 ,width=600)
    f.place(x=0,y=0)
    te=Label(root,text="working on it")
    te.pack()
    f.update()
    l=text.split()
    
    lrec=[]
    k=0
    kt=Label(root)
    kt.pack()
    for i in l:
        tts = gtts.gTTS(i)
        tts.save(f"{k}.mp3")
        lrec.append(f"{k}.mp3")
        kt.config(text=f"{round((k+1)/len(l)*100,2)}%")
        f.update()
        
        k+=1

    te.destroy()
    tee=Label(root,text="DONE")
    tee.pack()
    sleep(1)
    f.update()
    tee.destroy()
    kt.destroy()
    word=Label(root,text="",font=('Helvatical bold',30))
    word.pack()
    root.focus_set()

def play(e):
    global pos
    try:
        if pos+1>len(lrec):
            f.destroy() 
            pos=0
            word.config(text="")

            
        else:

            word.config(text=l[pos])
            f.update()
            playsound(lrec[pos])
            
            
            pos+=1 
    except:
        print("nu")
def replay(e):
    playsound(lrec[pos-1])
   
    
    


root=tkinter.Tk()

t=Text(root)
t.pack()
b=Button(root,text="convert",font=('Helvatical bold',20),command=lambda :proced(t.get(1.0, "end-1c")))
b.pack()
root.bind("<space>",play)
root.bind("<j>",replay)

root.geometry("600x500")
root.mainloop()
try:
    for i in lrec:
        os.remove(i)
except:
    print("nothing was converted")