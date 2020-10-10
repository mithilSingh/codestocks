from tkinter import *

import random
import time
score=0

def createendwindow():
	global score
	

	#creates the  window which you see after u loose

	
	def back():#gets control from 'b' button and starts the game again
	
		createmainwindow()

	
	eroot=Frame(root4,width=200,height=200,bg="grey10").place(x=0,y=0)

	Label(eroot,text='sorry u lost ',bg= "grey10",fg="grey70").place(x=63,y=10)
	Label(eroot,text='your score '+str(score),bg= "grey10",fg="grey70").place(x=60,y=30)
	if p-s >5:
		Label(eroot,text='times Up!! you only have 3 secs',bg= "grey10",fg="grey70").place(x=13,y=50)
	else:
		Label(eroot,text='you were wrong',bg= "grey10",fg="grey70").place(x=50,y=50)

	b=Button(eroot,text='RETRY',command=back,bg= "grey10",fg="grey70",bd=0.5).place(x=75,y=80)
	score=0
	

	
	
def createmainwindow():#from here the main game begains
	global cheek
	global s
	global mtime 	
	def check(side):#cheecks weather the random direction created by computer is same as the button clicked by user and takes desicion accordingly
		global score
		global p

		p=time.time()
		if (r==side and p-s<3) or (r=="Not RIGHT" and side=="   LEFT  " and  p-s<3) or (r=="Not  LEFT" and side=='  RIGHT  ' and  p-s<3) :
			score+=1
			global cheek
			cheek=False
			#destroys the last window so that there is no mess for the  user hav to deal with when he looses#
			createmainwindow()	
			#creates the window again as a loop	
		else:
			#destroys the last window so that there is no mess for the  user hav to deal with when he looses
			createendwindow()#creates end window and ends the game
	
	root=Frame(root4,width=200,height=200)
	root.configure(bg="grey10")
	root.place(x=0,y=0)
	r=random.choice(['  RIGHT  ',"   LEFT  ","Not  LEFT","Not RIGHT"])
	s=time.time()
	mtime=3
	cheek=True


	def start():

		global mtime
		fr=Frame(root,bg= "grey10")
		fr.place(x=170,y=10,height=30,width=20)
		if mtime !=-1 and cheek==True :
			ltyu=Label(fr,text=mtime ,bg= "grey10",fg="grey70" )
			ltyu.place(x=0,y=0)
			mtime-=1
			root4.after(1000,start)
		elif mtime==-1:
			mtime=3
#2^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


	def lefttry(event):#sets the 'side' arrgument (in the check function avobe) to left and pass the control
		check('   LEFT  ')

	def righttry(event):#sets the 'side' arrgument (in the check function avobe) to left and pass the control
		check('  RIGHT  ')
	def lefttry1():#sets the 'side' arrgument (in the check function avobe) to left and pass the control
		lefttry("<Left>")
	def righttry1():#sets the 'side' arrgument (in the check function avobe) to left and pass the control
		righttry("<Right>")
	#sets the various widgets of the main game window such as left and right buttons
	l=Label(root,text=r,bg= "grey10",fg="grey70").place(x=72,y=10)
	l2=Label(root,text=score,bg= "grey10",fg="grey70").place(x=90,y=40)
	left=Button(root,text='Left',command=lefttry1,bg= "grey10",fg="grey70",bd=0)
	left.place(x=10,y=70)
	right=Button(root,text='Right',command=righttry1,bg= "grey10",fg="grey70",bd=0)
	right.place(x=145,y=70)

	start()
	root4.bind("<Right>",righttry)
	root4.bind("<Left>",lefttry)

#creates the window with play button#and sends control to main window

def createmainwindow1(event):
	createmainwindow()

	
root4=Tk()
root4.resizable(0,0)
root4.title("1 Direction")
play=Button(root4,text='PLAY',command=createmainwindow,bg="grey10",bd=0,fg="grey70",font="df")
play.place(x=70,y=40)
root4.bind("<Return>",createmainwindow1)
root4.configure(bg="grey10")
root4.geometry('190x110+550+300')
root4.mainloop()
#hope u enjoy it#
#############################################################################
###
# '''^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^