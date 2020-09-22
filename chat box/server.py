import socket
from tkinter import*
from threading import*
s=socket.socket()
s.bind(("192.168.0.105",5555))
s.listen(2)
print("waiting for connections")
#r=Tk()
l=[]
def send_it(li,c,msg,name):
    p=li.pop(li.index(c))
    sk=l[0]
    sk.send(bytes((f"{name}:{msg}"),"utf-8"))
    li.append(p)
def getit(c,arr,name):
    while True:
        kt=c.recv(1024).decode()
        print(arr,kt)
        #Label(r,text=c.recv(128).decode()).pack()
        #print(c.recv(1024))
        #c.send(bytes("hi","utf-8"))
        send_it(l,c,kt,name)
        
while True:
    rk=Tk()
    print ("done")
    c,addr=s.accept()
    namec=c.recv(2048).decode()
    l.append(c)
    
    print(c)
    print("connected with",addr)
    t=Thread(target=getit,args=(c,addr,namec))
    t.start()
    #r.mainloop()
        
c.close()

