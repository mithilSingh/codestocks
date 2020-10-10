from tkinter import*
import random
t=Tk()
bscore=0
uscore=0
acol="white"
def start():
	root=Toplevel(bg=acol)
	root.configure()
	root.title("STONE PAPER SISSORS")
	

	def paper():                                             
		Label(root,text="                                                                                 ",bg=acol).place(x=200,y=140)
		uslb=Label(root,text='              ',bg=acol).place(x=500,y=130)
		uslb=Label(root,image=img6).place(x=460,y=130)
		
		cover=Label(root,text='             ').place(x=90,y=130)	
		l=[img1,img2,img3]
		r=random.choice(l)
		clab=Label(root,image=r).place(x=90,y=130)
		global uscore
		global bscore
		if r==img2:
			uscore+=1
			
		elif  r==img1:
			bscore+=1
		slfu=Label(root,text=uscore,bg=acol).place(x=480,y=300)
		slfb=Label(root,text=bscore,bg=acol).place(x=110,y=300)
	def stone():
		Label(root,text="                         														           ",bg=acol).place(x=200,y=140)
		
		uslb=Label(root,image=img5).place(x=460,y=130)
		
		cover=Label(root,text='             ',bg=acol).place(x=90,y=130)	
		l=[img1,img2,img3]
		r=random.choice(l)
		clab=Label(root,image=r).place(x=90,y=130)
		global uscore
		global bscore
		if r==img1:
			uscore+= 1
		elif  r==img3:
			bscore+=1
				
		slfb=Label(root,text=bscore,bg=acol).place(x=110,y=300)
		slfu=Label(root,text=uscore,bg=acol).place(x=480,y=300)
	def sisors():
		Label(root,text="                  																				                  ",bg=acol).place(x=200,y=140)
		
		uslb=Label(root,image=img4).place(x=460,y=130)
		
		cover=Label(root,text='             ',bg=acol).place(x=90,y=130)	
		l=[img1,img2,img3]
		r=random.choice(l)
		clab=Label(root,image=r).place(x=90,y=130)
		global uscore
		global bscore
		if r==img2:
			bscore+=1
			
		elif r==img3:
			uscore+=1
				
		slfb=Label(root,text=bscore,bg=acol)
		slfb.place(x=110,y=300)
		slfu=Label(root,text=uscore,bg=acol)
		slfu.place(x=480,y=300)
	cl=Label(root,text='click on any one of the button below',font="fdh",bg=acol).place(x=200,y=140)
	img1=PhotoImage(file='C:/Users/MANISH/Desktop/New folder/1.PNG')
	img2=PhotoImage(file='C:/Users/MANISH/Desktop/New folder/2.PNG')
	img3=PhotoImage(file='C:/Users/MANISH/Desktop/New folder/3.PNG')
	img4=PhotoImage(file='C:/Users/MANISH/Desktop/New folder/4.PNG')
	img5=PhotoImage(file='C:/Users/MANISH/Desktop/New folder/5.PNG')
	img6=PhotoImage(file='C:/Users/MANISH/Desktop/New folder/6.PNG')
	usisor=PhotoImage(file='C:/Users/MANISH/Desktop/New folder/usissor.PNG')
	ustone=PhotoImage(file='C:/Users/MANISH/Desktop/New folder/ustone.PNG')
	upaper=PhotoImage(file='C:/Users/MANISH/Desktop/New folder/upaper.PNG')
	Label(root,text='SCORE',bg=acol).place(x=275,y=230)
	Label(root,text='Stone Paper Sisors...',font="udhdhhb",bg=acol).pack(side='top')
	l=Label(root,text='BOT',bg=acol).place(x=100,y=100)

	l2=Label(root,text='YOU',bg=acol).place(x=480,y=100)
	br=Button(root,image=ustone,command=stone,pady=100).place(x=170,y=350)
	br=Button(root,image=upaper,command=paper,pady=1).place(x=250,y=350)
	br=Button(root,image=usisor,command=sisors,pady=1,padx=2).place(x=330,y=350)
	root.geometry('600x420+200+150')
	root.mainloop()	
label2=Label(t,text="Press on PLAY to start the game ").place(x=70,y=30)
but=Button(t,text="PLAY",command=start).place(x=130,y=50)
qbut=Button(t,text="QUIT",command=t.quit).place(x=130,y=80)
t.geometry("300x130+370+290")
t.mainloop()