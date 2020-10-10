from tkinter import*
root=Tk()
def u(b):
    b.config(text="c")

b=Button(root,text="",command=(lambda : u(b)))
b.pack()
b1=Button(root,text="",command=u)
b1.pack()

root.geometry("400x400")
root.mainloop()