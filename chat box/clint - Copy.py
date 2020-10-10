import socket
from tkinter import*
from threading import *

name="thor"
cs=socket.socket()
try:
    cs.connect(("192.168.0.105",5555))
    cs.send(bytes(name,'utf-8'))
    root=Tk()
    root.title("chat box")
    root.config(bg="grey10")
    scrollbar = Scrollbar(root,bg="grey10",activebackground="grey10")
    scrollbar.pack( side = RIGHT, fill = Y )
    ml=Listbox(root, yscrollcommand = scrollbar.set,height=28,width=30,bg="grey10",fg="grey80",bd=0,highlightthickness=0 )
    ml.place(x=0,y=0)
    scrollbar.config( command = ml.yview ,bg="grey10",activebackground="grey10")
  

except:
    ro=Tk()
    Label(ro,text="The server is not active").pack()
    Button(ro,text="OK",command=(lambda : ro.destroy())).pack()
    ro.mainloop()
while True:
    
    def rec():
        try:
            while True:
                ap=cs.recv(1024).decode()
                k=""
            
                if len(ap)>25:
                    for i in range(0,len(ap),25):
                        k+=ap[i:i+25]+"\n"
                    ap=k[0:len(k)-1]
                ml.insert(END, ap)
                ml.yview_moveto('1.0')
        except:
            print("disconnected from the server")
    def nw():
        rt=Tk()
        b3=Button(rt,text="change name")
        rt.mainloop()
    def sendt():
        eg=e.get()
        cs.send(bytes(eg,"utf-8"))
        k=""
        
        if len(eg)>25:
            for i in range(0,len(eg),25):
                k+=eg[i:i+25]+"\n"
            eg=k[0:len(k)-1]
        if eg[0:12]=="change_name:":
            ml.insert(END, f"you changed name to {eg[12:len(eg)]}")
            ml.yview_moveto('1.0')
            e.delete(0,1025)
        elif eg!="":
            ml.insert(END, f"you:{eg}")
            ml.yview_moveto('1.0')
            e.delete(0,1025)
    try:

        b=Button(root,text="send",command=sendt,bd=0,bg="grey10",fg="grey80")
        b.pack(side="bottom")
        #b=Button(root,text="...",command=nw,bd=0,bg="grey10",fg="grey80")
        #b.pack(side="bottom")
        e=Entry(root,bg="grey15",bd=0,fg="grey80",width=30,justify="center",insertbackground="grey80")
        e.pack(side="bottom")
        t=Thread(target=rec)
        t.start()
        root.bind("<Return>",(lambda event:sendt()))
        root.geometry("200x500+100+100")
        root.resizable(0,0)
        root.mainloop()
        
        cs.close()
    except:
        break  
    