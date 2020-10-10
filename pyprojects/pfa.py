from tkinter import*
root=Tk()
w=10
q=25*8
can= Canvas(root,width=1000,height=1000)
can.pack()
a=list(list(1 for i in range(q))for r in range(q)) 
def c(color):
    can.create_rectangle(rown,coln,rown+w,coln+w)
global rown,coln
rown,coln=0,0
for ir in a:
    
    for re in ir:
        if re==1:
            rown+=w
            c("white")
    rown=0
    coln+=w
root.mainloop()
