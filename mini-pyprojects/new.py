from tkinter import *
import time as t
r=Tk()
x=700
l=Canvas(r,height=500,width=10000,bg="white")
l.place(x=700,y=0)
p=Canvas(r,height=10,width=10,bg="black")
p.place(x=720,y=0)
cy=0
cv=0
def cre():
    global x,cv,cy
    x-=3
    l.place(x=x,y=0)
    cy=cv
    cv=py
    
    l.create_oval(720-x,py-125,(720-x)+2,py-127,fill="black")
for i in range(1000,100001,100):
    r.after(i,cre)
def crt(event):
    x,y=event.x,event.y
    l.create_line(x,y,x+2,y,fill="black")
def crt2(event):
    x,y=event.x,event.y
    l.create_line(x,y,x+2,y,fill="black")

def crt3(event):
    global py
    r.update()
    py= p.winfo_rooty()
    ey=event.y
    if ey>490:
        ey=490
    p.place(x=720,y=ey)
    

l.bind("<Button-1>",crt)
l.bind("<B1-Motion>",crt2)
l.bind("<Motion>",crt3)
r.geometry("800x800+100+100")
r.mainloop()
