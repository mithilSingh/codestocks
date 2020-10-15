from tkinter import*
from tkinter import messagebox
from sklearn import svm
import numpy as np 
from IPython.display import display 
import pandas as pd 
import random as rr
import time as t
root=Tk()
root.config(bg="black")
w=30
k=4
cv=3*k
l=np.zeros((w*w))
tl=np.array([])
ll=np.array([])

mc=1



def train_data(event):
    global tl,ll,l,mc
    ll=np.append(ll,e.get())
    tl=np.append(tl,(l.reshape(1,-1)))
    
    #plt.imshow(tl.reshape(10,10))
    #plt.show()
    tl=tl.reshape(mc,w*w)

    mc+=1
    c.delete("all")
    l=np.zeros((w*w))

    
def main_train():
    global tl,ll,ca
    ca=svm.SVC()
    ca.fit(tl,ll)

def draw(event):
    global l
    x,y=event.x,event.y
    Xm=((x//k)*k)
    Ym=((y//k)*k)
    
    c.create_oval(Xm,Ym,Xm+k+cv,Ym+k+cv,fill="black",outline="black")
    l[(((Ym//k))*w)+Xm//k]=rr.randint(1,3)

    
def main_test():
    global ca
    la=Label(root,text=f"prediction:{str(ca.predict(l.reshape(1,-1)))[2:-2]}")
    la.pack()
    root.after(3000,lambda : la.destroy())

def clear():
    global l
    c.delete("all")
    l=np.zeros((w*w))
def sel_pix():
    global k,w,c,l,mc,tl,ll
    
    if len(tl)!=0:
        mb=messagebox.askyesno("are you sure?", "All the training data will be erassed")
    else:
        mb=True
  
    if mb==True:
        mc=1
        c.delete("all")
        w=scale.get()
        k=scale2.get()
        c.config(height=w*k,width=w*k)
        l=np.zeros((w*w))
        root.geometry(f"{w*k+100}x{w*k+40}")
        tl=np.array([])
        ll=np.array([])

    if var1.get()==1:
        tol.destroy()

def canvas_config():
    global scale,scale2,w,k,cb,var1,tol
    tol=Toplevel()
    tol.config(bg="white")
    scale = Scale( tol, from_=20 ,to=60, orient=HORIZONTAL ,label="canvas lenth",cursor="dot")
    scale.pack(anchor=CENTER)
    scale2 = Scale( tol, from_=3 ,to=10, orient=HORIZONTAL,label="pixel lenth",cursor="dot")
    scale2.pack(anchor=CENTER)
    button = Button(tol, text="change",command=sel_pix)
    button.pack(anchor=CENTER)
    var1 = IntVar()
    cb=Checkbutton(tol, text="close the window after change", variable=var1)
    cb.pack()
    cb.select()
    scale.set (w)
    scale2.set (k)
    tol.geometry("200x180")
    tol.resizable(0,0)
def datat():
    global mc ,ll
    nd={}

    for i in ll:
        if i in nd:
            nd[i][0]+=1
        else:
            nd[i]=[1]

    dtl=Toplevel()
    kt=""
    for k in nd:
        kt+=str(k)+":"+str(nd[k])[1:-1]+"\n"
    Label(dtl,text=f"number of samples {mc}").pack()
    Label(dtl,text=f"types of sample are \n{kt}").pack()
    #Label(dtl,text=f"number of {}").pack()
    but=Button(dtl,text="OK",command=dtl.quit)
    


me=Menu(root,tearoff=0)
me.add_command(label="clear", command=clear)
me.add_command(label="train", command=main_train)
me.add_command(label="test", command=main_test)
me.add_command(label="size", command=canvas_config)
me.add_command(label="data", command=datat)
c=Canvas(root,height=w*k,width=w*k)
c.pack()
e=Entry(root)
e.pack()
root.bind("<Button-3>",train_data)
c.bind("<Button-1>",draw)
c.bind("<B1-Motion>",draw)
root.config(menu=me)
root.geometry(f"{w*k+100}x{w*k+40}")
root.mainloop()
