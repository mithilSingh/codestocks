import socket
from tkinter import*
from threading import*
s=socket.socket()
s.bind(("192.168.0.105",5555))
s.listen(2)
print("waiting for connections....")
#r=Tk()
l=[]
def send_it(li,c,msg,name):
    p=li.pop(li.index(c))
    for sk in li:
        sk.send(bytes((f"{name}:{msg}"),"utf-8"))
    li.append(p)
def getit(c,arr,name):
    try:
        while True:
            kt=c.recv(1024).decode()
            if kt[0:12]=="change_name:":
                v=kt[12:len(kt)]
                send_it(l,c,f"changed name to\'{v}\'",name)
                name=v
                
            else:
                print(name,kt)
          
                send_it(l,c,kt,name)
    except:
        print(f"disconnected from {name}")
        l.pop(l.index(c))
        
        if len(l)==0:
            
            s.close()
           
        
        
while True:
    try:
        rk=Tk()
        
        c,addr=s.accept()
        namec=c.recv(2048).decode()
        l.append(c)
        
        
        print("connected with",namec)
        t=Thread(target=getit,args=(c,addr,namec))
        t.start()
    except:
        break
    
    
    