from tkinter import*
root=Tk()
cou=1
che1=0
che2=0
che3=0
che4=0
che5=0
che6=0
che7=0
che8=0
che9=0
def cheek():
	if che1==1 and che2==1 and che3==1:
		t=Tk()  
		root.destroy()
		t.geometry('250x240+400+300')
		l=Label(t,text='player2 won').pack()
	if che4==1 and che5==1 and che6==1:
		t=Tk()  
		root.destroy()
		t.geometry('250x240+400+300')
		l=Label(t,text='player2 won').pack()
	if che7==1 and che8==1 and che9==1:
		t=Tk()  
		root.destroy()
		t.geometry('250x240+400+300')
		l=Label(t,text='player2 won').pack()
	if che1==1 and che4==1 and che7==1:
		t=Tk()  
		root.destroy()
		t.geometry('250x240+400+300')
		l=Label(t,text='player2 won').pack()
	if che2==1 and che5==1 and che8==1:
		t=Tk()  
		root.destroy()
		t.geometry('250x240+400+300')
		l=Label(t,text='player2 won').pack()
	if che3==1 and che6==1 and che9==1:
		t=Tk()  
		root.destroy()
		t.geometry('250x240+400+300')
		l=Label(t,text='player2 won').pack()
	if che1==1 and che5==1 and che9==1:
		t=Tk()  
		root.destroy()
		t.geometry('250x240+400+300')
		l=Label(t,text='player2 won').pack()
	if che3==1 and che5==1 and che7==1:
		t=Tk()  
		root.destroy()
		t.geometry('250x240+400+300')
		l=Label(t,text='player2 won').pack()
	#----------------------
	if che1==2 and che2==2 and che3==2:
		t=Tk()  
		root.destroy()
		t.geometry('250x240+400+300')
		l=Label(t,text='player1 won').pack()
	if che4==2 and che5==2 and che6==2:
		t=Tk()  
		root.destroy()
		t.geometry('250x240+400+300')
		l=Label(t,text='player1 won').pack()
	if che7==2 and che8==2 and che9==2:
		t=Tk()  
		root.destroy()
		t.geometry('250x240+400+300')
		l=Label(t,text='player1 won').pack()
	if che1==2 and che4==2 and che7==2:
		t=Tk()  
		root.destroy()
		t.geometry('250x240+400+300')
		l=Label(t,text='player1 won').pack()
	if che2==2 and che5==2 and che8==2:
		t=Tk()  
		root.destroy()
		t.geometry('250x240+400+300')
		l=Label(t,text='player1 won').pack()
	if che3==2 and che6==2 and che9==2:
		t=Tk()  
		root.destroy()
		t.geometry('250x240+400+300')
		l=Label(t,text='player1 won').pack()
	if che1==2 and che5==2 and che9==2:
		t=Tk() 
		root.destroy()
		t.geometry('250x240+400+300')
		l=Label(t,text='player1 won').pack()
	if che3==2 and che5==2 and che7==2:
		t=Tk()  
		root.destroy()
		t.geometry('250x240+400+300')
		l=Label(t,text='player1 won').pack()
	if che1!=0 and che2!=0 and che3!=0 and che4!=0 and che5!=0 and che6!=0 and che7!=0 and che8!=0 and che9!=0:
		t=Tk()  
		root.destroy()
		t.geometry('250x240+400+300')
		l=Label(t,text='Match Draw').pack()
	
	
def c1():
	global cou
	global che1
	if cou==1:
		b1=Label(root,image=x,bd=0).place(x=1,y=1)
		cou=2
		che1=1
	elif cou==2:
		Label(root,text='player 1 ').place(x=100,y=240)
		b1=Label(root,image=o,bd=0).place(x=1,y=1)
		cou=1
		che1=2
	cheek()
	
	
def c2():
	global cou
	global che2
	if cou==1:
		b2=Label(root,image=x,bd=0).place(x=76,y=0)
		cou=2
		che2=1
	elif cou==2:
		Label(root,text='player 1 ').place(x=100,y=240)
		b2=Label(root,image=o,bd=0).place(x=76,y=0)
		cou=1
		che2=2
	cheek()

	
def c3():
	global cou
	global che3
	if cou==1:
		b3=Label(root,image=x).place(x=148,y=0)
		cou=2
		che3=1
	elif cou==2:
		Label(root,text='player 1 ').place(x=100,y=240)
		b3=Label(root,image=o).place(x=148,y=0)
		cou=1
		che3=2
	cheek()

def c4():
	global che4
	global cou
	if cou==1:
		b4=Label(root,image=x).place(x=0,y=71)
		cou=2
		che4=1
	elif cou==2:
		Label(root,text='player 1 ').place(x=100,y=240)
		b4=Label(root,image=o).place(x=0,y=71)
		cou=1
		che4=2
	cheek()
	
def c5():
	global cou
	global che5
	if cou==1:
		b5=Label(root,image=x).place(x=74,y=71)
		cou=2
		che5=1
	elif cou==2:
		Label(root,text='player 1 ').place(x=100,y=240)
		b5=Label(root,image=o).place(x=74,y=71)
		cou=1
		che5=2
		
	cheek()
def c6():
	global cou
	global che6
	if cou==1:
		b6=Label(root,image=x,bd=0).place(x=148,y=71)
		cou=2
		che6=1
	elif cou==2:
		Label(root,text='player 1 ').place(x=100,y=240)
		b6=Label(root,image=o,bd=0).place(x=148,y=71)
		cou=1
		che6=2
	cheek()
def c7():
	global cou
	global che7
	if cou==1:
		b7=Label(root,image=x,bd=0).place(x=0,y=142)
		cou=2
		che7=1
	elif cou==2:
		Label(root,text='player 1 ').place(x=100,y=240)
		b7=Label(root,image=o,bd=0).place(x=0,y=142)
		cou=1
		che7=2
	cheek()

def c8():
	global cou
	global che8
	if cou==1:
		b8=Label(root,image=x,bd=0).place(x=74,y=142)
		cou=2
		che8=1
	elif cou==2:
		Label(root,text='player 1 ').place(x=100,y=240)
		b8=Label(root,image=o,bd=0).place(x=74,y=142)
		cou=1
		che8=2
	cheek()

		
	
def c9():
	global che9
	global cou
	if cou==1:
		b9=Label(root,image=x).place(x=148,y=142)
		cou=2
		che9=1
	elif cou==2:
		Label(root,text='player 1 ').place(x=100,y=240)
		b9=Label(root,image=o).place(x=148,y=142)
		cou=1
		che9=2
	cheek()
x=PhotoImage(file="C:/Users/MANISH/Desktop/tic tac toe/x.png")
o=PhotoImage(file="C:/Users/MANISH/Desktop/tic tac toe/o.png")
		
b1=Button(root,text='' , command=c1,padx=33,pady=24,).place(x=0,y=0)
b2=Button(root,text='',command=c2,padx=33,pady=24).place(x=74,y=0)
b3=Button(root,text='',command=c3,padx=33,pady=24).place(x=148,y=0)
b4=Button(root,text='' , command=c4,padx=33,pady=24).place(x=0,y=71)
b5=Button(root,text='',command=c5,padx=33,pady=24).place(x=74,y=71)
b6=Button(root,text='',command=c6,padx=33,pady=24).place(x=148,y=71)
b7=Button(root,text='' , command=c7,padx=33,pady=24).place(x=0,y=142)
b8=Button(root,text='',command=c8,padx=33,pady=24).place(x=74,y=142)
b9=Button(root,text="",command=c9,padx=33,pady=24).place(x=148,y=142)

root.geometry('225x215+400+300')
root.resizable(0,0)
root.mainloop()