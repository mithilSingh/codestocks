from tkinter import*
root= Tk()
root.title("CALCULATOR")
e=Entry(root,width=46,bg="black",bd=0,fg="grey50",justify="right",insertbackground="grey80")
root.configure(bg="black")
count=0
cheek=True
b="black"
g="grey80"
mc=3
bk=0
ms="7413924"
def mn1(nu):
    e.insert(100,nu)    
    global count
    count+=1
def n1():
    mn1("1")
def n2():
    mn1("2")
def n3():
    mn1("3")
def n4():
    mn1("4")
def n5():
    mn1("5")
def n6():
    mn1("6")
def n7():
    mn1("7")
def n8():
    mn1("8")
def n9():
    mn1("9")
def n0():
    mn1("0")
def nad():
    mn1("+")
def nsb():
    mn1("-")
def nml():
    mn1("*")
def ndv():
    mn1("/")
def neq():
    global cheek
    global count
    global bk
    global mc
    if bk != mc :
        try:
            ans=e.get()
            e.delete(first=0,last=1000)
            fans=eval(ans)
            mf=open("History","a")
            an=ans+"="+str(fans)
            mf.write(an+"\n")
            e.insert(0,fans)
            dj=str(fans)
            bk +=1
            ply=0
            while True:
                try:
                    aaa=dj[ply]
                    ply+=1
                except:
                    count=ply
                    break

        except:
            e.delete(first=0,last=1000)
            e.insert(0,"Bad Expression")
            cheek=False
    elif bk==mc:
        e.delete(first=0,last=1000)
        e.insert(0,ms)
        bk=0

def ndot():
    mn1(".")
    Label(root,text=count)
def bac():
    global cheek
    global count
    e.delete(first=0,last=1000)
    count=0
    cheek=True
def bc():
    global cheek
    global count
    if cheek==True:
        t=count-1
        tp=count
        e.delete(first=t,last=tp)
        if count>0:
            count-=1
        elif count<=0:
            pass
    elif cheek==False:
        e.delete(first=0,last=14)
        cheek=True
        count=0
e.place(x=2,y=20)
b1=Button(root,text="1",padx=20,pady=18,command=n1,bg=b,fg=g,activebackground=g,activeforeground=b,bd=0).place(x=0 ,y=40)
b2=Button(root,text="2",padx=20,pady=18,command=n2,bg=b,fg=g,activebackground=g,activeforeground=b,bd=0).place(x=57 ,y=40)
b3=Button(root,text="3",padx=20,pady=18,command=n3,bg=b,fg=g,activebackground=g,activeforeground=b,bd=0).place(x=114 ,y=40)
b4=Button(root,text="4",padx=20,pady=18,command=n4,bg=b,fg=g,activebackground=g,activeforeground=b,bd=0).place(x=0 ,y=101)
b5=Button(root,text="5",padx=20,pady=18,command=n5,bg=b,fg=g,activebackground=g,activeforeground=b,bd=0).place(x=57,y=101)
b6=Button(root,text="6",padx=20,pady=18,command=n6,bg=b,fg=g,activebackground=g,activeforeground=b,bd=0).place(x=114 ,y=101)
b7=Button(root,text="7",padx=20,pady=18,command=n7,bg=b,fg=g,activebackground=g,activeforeground=b,bd=0).place(x=0 ,y=162)
b8=Button(root,text="8",padx=20,pady=18,command=n8,bg=b,fg=g,activebackground=g,activeforeground=b,bd=0).place(x=57 ,y=162)
b9=Button(root,text="9",padx=20,pady=18,command=n9,bg=b,fg=g,activebackground=g,activeforeground=b,bd=0).place(x=114 ,y=162)
b0=Button(root,text="0",padx=49,pady=15,command=n0,bg=b,fg=g,activebackground=g,activeforeground=b,bd=0).place(x=0 ,y=224)
bdot=Button(root,text=".",padx=21,pady=15,command=ndot,bg=b,fg=g,activebackground=g,activeforeground=b,bd=0).place(x=115 ,y=224)
bad=Button(root,text="+",padx=18.7,pady=18,command=nad,bg=b,fg=g,activebackground=g,activeforeground=b,bd=0).place(x= 170,y=40)
bsb=Button(root,text="-",padx=20,pady=18,command=nsb,bg=b,fg=g,activebackground=g,activeforeground=b,bd=0).place(x= 170,y=101)
bml=Button(root,text="*",padx=20,pady=18,command=nml,bg=b,fg=g,activebackground=g,activeforeground=b,bd=0).place(x= 170,y=162)
bdi=Button(root,text="/",padx=20,pady=15,command=ndv,bg=b,fg=g,activebackground=g,activeforeground=b,bd=0).place(x= 170,y=224)
bac=Button(root,text="AC",padx=16,pady=18,command=bac,bg=b,fg=g,activebackground=g,activeforeground=b,bd=0).place(x= 226,y=101)
beq=Button(root,text="=",padx=20,pady=45.5,command=neq,bg=b,fg=g,activebackground=g,activeforeground=b,bd=0).place(x= 226,y=162)
bc=Button(root,text="C",padx=20,pady=18,command=bc,bg=b,fg=g,activebackground=g,activeforeground=b,bd=0).place(x= 226,y=40)
Label(root,text=count).place(x=0,y=500)
root.geometry("285x280+300+300")
root.resizable(0,0)
root.mainloop()