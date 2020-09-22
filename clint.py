import socket
from tkinter import*
from threading import *

name="kartike"
cs=socket.socket()
cs.connect(("192.168.0.105",5555))
cs.send(bytes(name,'utf-8'))
root=Tk()
while True:
    
    def rec():
        while True:
            ap=cs.recv(1024).decode()
            Label(root,text=ap).pack()

    def send():
        eg=e.get()
        cs.send(bytes(eg,"utf-8"))
        if eg!="":
            Label(root,text=(f"you:{eg}")).pack()
    try:

        b=Button(root,text="send",command=send)
        b.pack(side="bottom")
        e=Entry(root)
        e.pack(side="bottom")
        t=Thread(target=rec)
        t.start()
        root.geometry("200x500+100+700")
        root.mainloop() 
        cs.close()
    except:
        break  
    
