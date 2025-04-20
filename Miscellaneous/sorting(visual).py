from tkinter import *
import random as ra
def arg(l):
    t=len(l)
    t2=t
    for i in range(t):
        for ti in range(1,t2):
            a=l[ti-1]
            if a>l[ti]:
                l[ti-1],l[ti]=l[ti],l[ti-1]
        t2-=1
    return(l)
r=Tk()
le=[]
for itr in range(1,401):
    le.append(itr)

def np():
    global pr
    pr=[]
    c=Canvas(r,width=1000,height=500)
    c.place(x=0,y=0)
    x=0
    for ik in range(100):
        pr.append(ra.choice(le))
    for i in pr:
        x+=10
        c.create_rectangle(x,500,x-5,500-i,fill="red")
    global kkt
    kkt=arg(pr)
def off():
    c2=Canvas(r,width=1000,height=500)
    c2.place(x=0,y=0)
    x=0
    for i in kkt:
        x+=10
        c2.create_rectangle(x,500,x-5,500-i,fill="red")




Button(r,text="arrange",command=off).place(x=400,y=550)
Button(r,text="new",command=np).place(x=300,y=550) 
np()
r.geometry("1000x1000")
r.mainloop()