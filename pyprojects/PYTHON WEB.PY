from tkinter import *
root=Tk()
root.title('hello')
def my_Click():
    roof=Toplevel()
    gf=Button(roof,image=A).pack()
    roof.geometry("800x600+0+0")


def my_click():
    rook=Toplevel()
    gg=Button(rook,image=b3).pack()
    rook.geometry("800x600+0+0")

def My_Click():
    rooL=Toplevel()
    gad=Button(rooL,image=b7).pack()
    rooL.geometry("800x600+0+0")


def MY_click():
    rooN=Toplevel()
    asd=Button(rooN,image=b4).pack()
    rooN.geometry("800x600+0+0")

def my_CLick():
    rooM=Toplevel()
    x=Button(rooM,image=b5).pack()
    rooM.geometry("800x600+0+0")


def my_CLIck():
    rook=Toplevel()
    g=Button(rook,image=b6).pack()
    rook.geometry("800x600+0+0")
    
def tiger():
    roo12=Toplevel()
    x=Button(roo12,image=b8).pack()
    roo12.geometry("800x600+0+0")

def cycle():
    roo13=Toplevel()
    g=Button(roo13,image=b9).pack()
    roo13.geometry("800x600+0+0")    
    
b=Button(root,text="imagne" ,command=my_Click ).grid(row=1, column=0,)

b2=Button(root,text="nightsky",command=my_click).grid(row=1, column=1) 

BU=Button(root,text="LAUGH" ,command=My_Click ).grid(row=1, column=2)

BU2=Button(root,text="MILKIWAY",command=MY_click).grid(row=3, column=2) 

BU3=Button(root,text="BACK SCHOOL" ,command=my_CLick ).grid(row=3, column=0)

BU4=Button(root,text="SMILE",command=my_CLIck).grid(row=5, column=2) 

BU12=Button(root,text="cycle" ,command=tiger).grid(row=5, column=0)

BU13=Button(root,text="tiger",command=cycle).grid(row=5, column=1) 

#=========================================================================
A=PhotoImage(file='C:\\Users\\MANISH\\Desktop\\pictures\\draw.PNG')
Button(root, image=A,command=my_Click).grid(row=0, column=0)

LEARN=PhotoImage(file='C:\\Users\\MANISH\\Pictures\\LEARN.PNG')
Label(root, image=LEARN,pady=10).grid(row=2, column=1)

b3=PhotoImage(file='C:/Users/MANISH/Pictures/night.PNG')
Button(root, image=b3,command=my_click).grid(row=0, column=1)

b4=PhotoImage(file='C:/Users/MANISH/Pictures/milky way.PNG')
Button(root, image=b4,command=MY_click).grid(row=2, column=2)

b5=PhotoImage(file='C:/Users/MANISH/Pictures/school.PNG')
Button(root, image=b5 ,command=my_CLick).grid(row=2, column=0)

b6=PhotoImage(file='C:/Users/MANISH/Pictures/smile.PNG')
Button(root, image=b6,command=my_CLIck).grid(row=4, column=2)

b8=PhotoImage(file='C:/Users/MANISH/Pictures/CYCLE2.PNG')
Button(root, image=b8,command=tiger).grid(row=4, column=0)

b9=PhotoImage(file='C:/Users/MANISH/Pictures/tiger.PNG')
Button(root, image=b9,command=cycle).grid(row=4, column=1)

b7=PhotoImage(file='C:/Users/MANISH/Pictures/laugh.PNG')
Button(root, image=b7,command=My_Click).grid(row=0, column=2)

root.geometry("800x800+0+0")
root.mainloop()

