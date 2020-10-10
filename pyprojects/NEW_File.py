from tkinter import *
root=Tk()
root.config(bg="grey10")
l =Label(root,text='enter the file name',fg="grey70",bg="grey10")
l.pack()
e=Entry(root)
e.pack()
def submit():
    p=e.get()
    f=open(p,w)
b=Button(root,text="submit",command=submit)
b.pack()
root.mainloop()