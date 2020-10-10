from tkinter import*
from tkinter import messagebox
from sklearn import svm
import numpy as np 

import random as rr
import time as t
root=Tk()
root.config(bg="black")
w=30
k=6
l=np.zeros((w*w))
tl=np.array([])
ll=np.array([])
print(l)
mc=1

c=Canvas(root,height=w*k,width=w*k)
c.pack()

def train_data(event):
    global tl,ll,l,mc
    ll=np.append(ll,e.get())
    tl=np.append(tl,(l.reshape(1,-1)))
    
    #plt.imshow(tl.reshape(10,10))
    #plt.show()
    tl=tl.reshape(mc,w*w)
    print(">",ll)
    mc+=1
    c.delete("all")
    l=np.zeros((w*w))
    print(mc-1)
def main_train():
    global tl,ll,ca
    ca=svm.SVC()
    ca.fit(tl,ll)
    print("done")
def draw(event):
    global l
    x,y=event.x,event.y
    Xm=((x//k)*k)
    Ym=((y//k)*k)
    
    c.create_rectangle(Xm,Ym,Xm+k,Ym+k,fill="black",outline="black")
    l[(((Ym//k))*w)+Xm//k]=rr.randint(1,3)
    print(Xm,Ym)
    
def main_test():
    global ca
    print(ca.predict(l.reshape(1,-1)))
def clear():
    global l
    c.delete("all")
    l=np.zeros((w*w))
def sel():
    global w,c,l
    
    if len(tl)!=0:
        mb=messagebox.askyesno("are you sure?", "All the training data will be erassed")
    else:
        mb=True
    print(mb)
    if mb==True:
        
        c.delete("all")
        w=scale.get()
        c.config(height=w*k,width=w*k)
        l=np.zeros((w*w))
        root.geometry(f"{w*k}x{w*k+230}")
     

e=Entry(root)
e.pack()
root.bind("<Button-3>",train_data)
c.bind("<Button-1>",draw)
c.bind("<B1-Motion>",draw)
b=Button(root,text="clear",command=clear)
b.pack()
b1=Button(root,text="train",command=main_train)
b1.pack()
b2=Button(root,text="test",command=main_test)
b2.pack()
scale = Scale( root, from_=10 ,to=100, orient=HORIZONTAL)
scale.pack(anchor=CENTER)
button = Button(root, text="change canvas size",command=sel)
button.pack(anchor=CENTER)

root.geometry(f"{w*k}x{w*k+230}")
root.mainloop()