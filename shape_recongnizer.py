from tkinter import*
from sklearn import svm
import numpy as np 
import matplotlib.pyplot as plt
import random as rr
import time as t
root=Tk()
root.config(bg="black")
w=10
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
    print(">",tl,ll)
    mc+=1
    print(type(ll),mc)
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
    print(l)
def main_test():
    global ca
    print(ca.predict(l.reshape(1,-1)))
def clear():
    global l
    c.delete("all")
    l=np.zeros((w*w))
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
root.geometry("200x200")
root.mainloop()

