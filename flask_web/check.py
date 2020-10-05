from threading import Thread as th
from tkinter import*
cd={'leng':0,'charno':0,'chc':0}
def ch():
    global ch
    while True:#checks for the right password everytime
        eg=e.get()
        r.update()
        #<===============8 chracter check============>
        if eg=="exit":
            r.destroy()
            break
        if len(eg)<8 and eg!="" and cd['leng']==0:
            l=Label(r,text="enter password with atleast 8 characters",fg="red")
            l.pack()
            cd['leng']=1
        elif len(eg)>7:
            try:
                l.destroy()
                cd['leng']=0
            except UnboundLocalError:
                pass
        #<======================atleast 3 number check=================>
        cd['charno']=0
        for a in range(len(eg)):
            try :
                
                cd['charno']+=int(eg[a])/int(eg[a])
            except ValueError:
                pass
        if cd['charno']<3 and cd['chc']==0 and eg!="":
            l2=Label(r,text="enter atleast 3 numbers",fg="red")
            l2.pack()
            cd['chc']=1
        

        elif cd['charno']>2:
            try:
                l2.destroy()
                cd['chc']=0
                
            except UnboundLocalError:
                pass

## window catogries
               
r=Tk()
e=Entry(r)
e.pack()
the=th(target=ch)
the.start()
r.geometry("300x100")
r.mainloop()