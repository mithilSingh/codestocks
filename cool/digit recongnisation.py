from tkinter import*
from sklearn import svm,datasets
import numpy as np 
import matplotlib.pyplot as plt 
import random
di=datasets.load_digits()
x,y=di.data[0:len(di.data)*8//10],di.target[0:len(di.target)*8//10]
c=svm.SVC()
c.fit(x,y)

ak=np.array([[0.,0., 0., 0., 0., 0., 0., 0.],
            [0.,0., 0., 0., 0., 0., 0., 0.],
            [0.,0., 0., 0., 0., 0., 0., 0.],
            [0.,0., 0., 0., 0., 0., 0., 0.],
            [0.,0., 0., 0., 0., 0., 0., 0.],
            [0.,0., 0., 0., 0., 0., 0., 0.],
            [0.,0., 0., 0., 0., 0., 0., 0.],
            [0.,0., 0., 0., 0., 0., 0., 0.]])
root=Tk()
cp=Canvas(root,height=400,width=400,bg="white")
cp.pack()
def mo(event):
    global Xm,Ym
    cx,cy=event.x,event.y
    
    Xm=((cx//50)*50)
    Ym=((cy//50)*50)
    #print(cx,cy,Xm,Ym)
    cp.create_rectangle(Xm,Ym,Xm+50,Ym+50,fill="black",outline="black")
    ak[cy//50][cx//50]=random.randint(13,16)
def mo1(event):
    global Xm,Ym
    cx,cy=event.x,event.y
    
    Xm=((cx//50)*50)
    Ym=((cy//50)*50)
    #print(cx,cy,Xm,Ym)
    cp.create_rectangle(Xm,Ym,Xm+50,Ym+50,fill="white",outline="white")
    ak[cy//50][cx//50]=0
def peri():
    Label(root,text=f"It looks like {str(c.predict(ak.reshape((1,64))))[1:-1]} to me").place(x=150,y=460)

root.bind("<B1-Motion>",mo)
root.bind("<Button-1>",mo)
root.bind("<B3-Motion>",mo1)
b=Button(root,text="predict",command=peri)
b.pack()
root.bind("<Button-3>",mo1)
root.geometry("400x500")
root.mainloop()
