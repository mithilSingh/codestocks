'''ideas for improvement
[help option in data window

use the saved data in ]-in the menu bar
'''
from tkinter import*
from tkinter import messagebox
from sklearn import svm
import numpy as np 
import random as rr
import time as t
import os 
import  tkinter.ttk as tk
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
    nk={}
    for i in ll:
        if i in nk:
            nk[i][0]+=1
        else:
            nk[i]=[1]
    mc+=1
    c.delete("all")
    l=np.zeros((w*w))
    la=Label(root,text=f"done {e.get(),nk[e.get()]}",bg="black",fg="white")
    la.pack()
    root.after(500,lambda : la.destroy())
    

    
def main_train():
    global tl,ll,ca
    ca=svm.SVC()
    ca.fit(tl,ll)

def draw(event):
    global l
    try:
        x,y=event.x,event.y
        Xm=((x//k)*k)
        Ym=((y//k)*k)

        c.create_oval(Xm,Ym,Xm+k+cv,Ym+k+cv,fill="black",outline="black")
        l[(((Ym//k))*w)+Xm//k]=rr.randint(1,3)

    except IndexError:
        pass
def main_test():
    global ca
    la=Label(root,text=f"prediction:{str(ca.predict(l.reshape(1,-1)))[2:-2]}",bg="black",fg="white")
    la.pack()
    root.after(3000,lambda : la.destroy())

def clear():
    global l
    c.delete("all")
    l=np.zeros((w*w))

def sel_pix():
    global k,w,c,l,mc,tl,ll
    
    if len(tl)!=0:
        mb=messagebox.askyesno("are you sure?"," All the training data will be erassed")
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
    def clear_data():
        global tl,ll,mc
        mb2=messagebox.askyesno("are you sure?", "All the training data will be erassed")
        if mb2==True:
            tl=np.array([])
            ll=np.array([])
            mc=1
            dtl.destroy()
    def save_data():
        def sav():
            global tl ,ll
            cwd=os.getcwd()
            try:
                os.mkdir(os.path.join(os.getcwd(),"saved_data"))
            except FileExistsError:
                pass
            
            rk=os.getcwd()
            os.chdir((os.path.join(os.getcwd(),"saved_data")))

            np.savez(e1.get(),traning_data=tl,training_labels=ll)
            os.chdir(rk)
            ttt.destroy()
            la=Label(root,text="data saved",bg="black",fg="white")
            la.pack()
            root.after(1000,lambda : la.destroy())
        ttt=Toplevel()
        Label(ttt,text="file name" ).pack()
        e1=Entry(ttt)
        e1.pack()   
        b2=Button(ttt,text="SAVE",command=sav)
        b2.pack()
    def load_data():
        def opn():
            global tl ,ll,ca
            try:
                ko=os.getcwd()
                os.chdir(os.path.join(os.getcwd(),"saved_data"))
                loaded_file=np.load(f"{e2.get()}.npz")
                tl,ll=loaded_file["traning_data"],loaded_file["training_labels"]
                main_train()
                os.chdir(ko)
                la=Label(root,text="data loaded",bg="black",fg="white")
                la.pack()
                root.after(1000,lambda : la.destroy())
            except FileNotFoundError:
                la=Label(lll,text="no such file",bg="black",fg="white")
                la.pack()
                lll.after(1000,lambda : la.destroy())
        lll=Toplevel()
        Label(lll,text="file name" ).pack()
        e2=Entry(lll)
        e2.pack()   
        b3=Button(lll,text="OPEN",command=opn)
        b3.pack()
    global mc ,ll,nd
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
    Label(dtl,text=f"number of samples {mc-1}").pack()
    Label(dtl,text=f"types of sample are \n{kt}").pack()
    #Label(dtl,text=f"number of {}").pack()
    but=Button(dtl,text="OK",command=dtl.quit)
    me2=Menu(root,tearoff=0)
    me2.add_command(label="clear data", command=clear_data)
    me2.add_command(label="save data", command=save_data)
    me2.add_command(label="load data", command=load_data)
    #me2.add_command(label="save", command=save)
    dtl.config(menu=me2)
    
def HELP():
    htl=Toplevel()
    Label(htl,text="""
              MAKE YOUR SHAPE AND LET THE COMPUTER RECONGNIZE THEM!                    

    Yes, in this program you can draw any shape and then see the computer guess  
    it in just 4 easy steps.  

    Instructions:
        -You can start with drawing any shape on the canvas (white area) by 
        pressing the left mouse button and draging the mouse .  

        -Now mention the shape you drawed on the canvas in the entry bellow the 
        canvas.Now click right mouse button to register the shape drawn such 
        computer can learn from it.

        -Draw some more same types of shapes ,for Example if you want the program 
        to classify a triangle drawn and a square drawn atleast 20 triangle 
        mentioning the name "triangle" and do the same when drawing square .

        -After giving several examples click on train button in menubar to train 
        the program about the different shapes you drew .

        CONGRATULATION!! You have trained your program  now draw any shape on the 
        canvas and click the test button to test them.

        TIPS :
            >Not getting the expectecd results ?
            -try gving more examples 
            -you can also change the Canvas size in size option in menue bar
            -try classifing shapes such as -forward slash/backward slash , line and
            a closed object triangle and square etc.

    """,bg="black",fg="grey80",font = "Helvetica 14").pack()

me=Menu(root,tearoff=0)
me.add_command(label="clear", command=clear)
me.add_command(label="train", command=main_train)
me.add_command(label="test", command=main_test)
me.add_command(label="size", command=canvas_config)
me.add_command(label="data", command=datat)
me.add_command(label="help", command=HELP)
c=Canvas(root,height=w*k,width=w*k)
c.pack()
e=Entry(root)
e.pack()
root.bind("<Button-3>",train_data)
c.bind("<Button-1>",draw)
c.bind("<B1-Motion>",draw)
root.config(menu=me)
root.geometry(f"{w*k+120}x{w*k+50}")
root.mainloop()