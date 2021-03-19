from socket import *
from threading import Thread
from tkinter import *
end=True
c=socket()
c.connect(("192.168.1.12",55557))
luck=int(c.recv(1024).decode())
root2=Tk()
root=Frame(root2)
root.pack()
x_img=PhotoImage(file=r"c:/Users/Astha/OneDrive/Desktop/happy form/pyfiles/projects/socket server/x.png")
o_img=PhotoImage(file=r"c:/Users/Astha/OneDrive/Desktop/happy form/pyfiles/projects/socket server/o.png")
blk_img=PhotoImage(file=r"c:/Users/Astha/OneDrive/Desktop/happy form/pyfiles/projects/socket server/blank.png")
b1=Button(root,image=blk_img,command=lambda :mainsend(1))
b2=Button(root,image=blk_img,command=lambda :mainsend(2))
b3=Button(root,image=blk_img,command=lambda :mainsend(3))
b4=Button(root,image=blk_img,command=lambda :mainsend(4))
b5=Button(root,image=blk_img,command=lambda :mainsend(5))
b6=Button(root,image=blk_img,command=lambda :mainsend(6))
b7=Button(root,image=blk_img,command=lambda :mainsend(7))
b8=Button(root,image=blk_img,command=lambda :mainsend(8))
b9=Button(root,image=blk_img,command=lambda :mainsend(9))

b1.grid(column=0,row=0)
b2.grid(column=1,row=0)
b3.grid(column=2,row=0)
b4.grid(column=0,row=1)
b5.grid(column=1,row=1)
b6.grid(column=2,row=1)
b7.grid(column=0,row=2)
b8.grid(column=1,row=2)
b9.grid(column=2,row=2)
mg=[b1,b2,b3,b4,b5,b6,b7,b8,b9]
print(">>",len(b1["text"]))
def check(x,li):
    cl=[[0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
            [0,4,8],[2,4,6]]
    for i in cl:
        if li[i[0]]["text"]==x and li[i[1]]["text"]==x and li[i[2]]["text"]==x:
            return True
    if b1["text"]!="" and b2["text"]!="" and b3["text"]!="" and b4["text"]!="" and b5["text"]!="" and b6["text"]!="" and b7["text"]!="" and b8["text"]!="" and b9["text"]!="" :
        return "draw"
                
def req():
    c.send(bytes('''>>>>>>>>>>>>>>
                        REPLAY      
                    <<<<<<<<<<<<<<''',"utf-8"))
def con(w):
    f=Frame(root,height=320,width=320)
    f.place(x=0,y=0)  
    Label(f,text=f"you {w}").place(x=130,y=120)
    b=Button(f,text="restart",command=req)
    b.place(x=130,y=160)
def mainsend(w):
    
    c.send(bytes(str(w),"utf-8"))
    mg[w-1].config(text=cns)
    mg[w-1].config(image=cnsi)
    print(mg[0])
    if check("jj",mg)=="draw":
        con("draw")
    elif check(sn,mg):
        
        con("lost")
    elif check(cns,mg):
        con("won")
    root.update()
    for i in mg:
        i.config(state=DISABLED)
def REPLAY():
    print("replay")
def listen():
    global end
    while end:
        print("ui")
        rk=int(c.recv(1024).decode())-1
        root.update()
        mg[rk].config(text=sn)
        mg[rk].config(image=sni)
        if rk=='''>>>>>>>>>>>>>>
                        REPLAY      
                    <<<<<<<<<<<<<<''':
         
            REPLAY()
        if rk!="":
            for i in mg:
                if i["text"]=="":
                    
                    i.config(state=NORMAL)
            
    if check("ppppp",mg)=="draw":
        con("draw")
    elif check(sn,mg):
        
        con("lost")
    elif check(cns,mg):
        con("won")
           

t=Thread(target=listen)
t.start()
if luck%2==0:
    root.update()

    sn="x"
    cns="o"
    sni=x_img
    cnsi=o_img
else :
    sn="o"
    cns="x"
    for i in mg:
        i.config(state=DISABLED)
    print("listen")
    sni=o_img
    cnsi=x_img
print(b1["text"])
root2.mainloop()
print("lllllllllllllllllllllllllllllllllllllllllll")
end=False
