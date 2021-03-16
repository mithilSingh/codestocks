from socket import *
from threading import Thread
from random import choice
s=socket()
s.bind(("localhost",55557))

s.listen(3)
print("server ready")
def sen(ar,cl):
    global l
    ar.send(bytes(str(o),"utf-8"))
    while True:
        rm=ar.recv(1024).decode()
        if rm=='''>>>>>>>>>>>>>>
                        REPLAY      
                    <<<<<<<<<<<<<<''':
            
            for i in l:
                i.send(bytes(rm,"utf-8"))
        elif rm!="":
            print(rm)
            po=l.pop(l.index(ar))
            for i in l:
                i.send(bytes(rm,"utf-8"))
            l.append(po)
l=[]
k=choice([0,1])
o=1
while True:
    adr,clint=s.accept()
    l.append(adr)
    print(adr,">>>>>",clint)
    t=Thread(target=sen,args=(adr,clint))
    o+=1


    t.start()


    