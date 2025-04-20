from tkinter import*
import random
root=Tk()
root.configure(bg="GREY")
bt=True
def move():
    r=random.choice([300,400,500,600,350,450,550,650])
    yr=random.choice([300,400,500,600,350,450,550,650])
    b.place(x=r,y=yr)
    
    
b=Button(root,text="PLAY",font="Gill_Sans_Ultra_Bold",command=move)
if bt==True:
    b.place(x=480,y=370)
    b.configure(bg="grey")
    bt=False
    l=Label(root,text='''Click on "play" to start the game''')
    l.configure(bg="grey",font="Gill_Sans_Ultra_Bold")
    l.place(x=420,y=0)
root.geometry("1000x690+0+0")
root.mainloop()