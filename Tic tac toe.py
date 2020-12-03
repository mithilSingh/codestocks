from tkinter import *
from time import sleep 
from threading import Thread
count=0
l='_________'
class bu(Button):
	occupied=True
	def __init__(self,x_,y_):
		self._x=x_
		self._y=y_
		self.pos=(((x_/xv)+1)+((y_/yv)*3))
		super().__init__()
		self.b=Button(root,height=3,width=3,command=self.cval,text='  ')
		self.b.place(x=x_,y=y_)
	def check(self):
		if self.cc('x',l)==True:
			Label(root,text=' player with x wins').place(x=0*xv,y=yv*3)
			root.geometry(f'{xv*3}x{yv*3+30}')
		if self.cc('o',l)==True:
			Label(root,text=' player with o wins').place(x=0*xv,y=yv*3)
			root.geometry(f'{xv*3}x{yv*3+30}')	
		elif '_' not in list(l):
			Label(root,text='Draw').place(x=0*xv,y=yv*3)
			root.geometry(f'{xv*3}x{yv*3+30}')
	def  cc(self,s,lis):
		if (lis[0]==s and lis[1]==s and lis[2]==s)or(lis[3]==s and lis[4]==s and lis[5]==s)or(lis[8]==s and lis[7]==s and lis[6]==s)or(lis[0]==s and lis[3]==s and lis[6]==s)or(lis[1]==s and lis[4]==s and lis[7]==s)or(lis[2]==s and lis[5]==s and lis[8]==s)or(lis[0]==s and lis[4]==s and lis[8]==s)or(lis[2]==s and lis[4]==s and lis[6]==s):
				return True					
	def cval(self,):
		global count,l,tlp
		if self.occupied:
			
			if count%2==0:
				self.b.config(text='x')
				l=l[0:(int(self.pos)-1)]+'x'+l[(int(self.pos)):9]
			else:
				self.b.config(text='o')		
				l=l[0:(int(self.pos)-1)]+'o'+l[(int(self.pos)):9]		
			self.occupied=False
			count+=1
			print(l)
			self.b.config(state=DISABLED)
			if mode==2:
				#self.thre=Thread(target=self.compute)
				#self.thre.start()
				self.compute()
	def compute(self):
			global count,tlp,l
			if True:
				root.after(500)
				count+=1
				for i in range(len(l)):
					if l[i]=='_':
							if self.cc('o',l[0:i]+'o'+l[i+1:len(l)])==True:		
								
								vwi[i].b.config(text='o')
								vwi[i].b.config(state=DISABLED)
								l=(l[0:i]+'o'+l[i+1:len(l)])
								vwi[i].occupied=False
								
								tlp=False
								break
							elif self.cc('x',l[0:i]+'x'+l[i+1:len(l)])==True:		
								vwi[i].b.config(text='o')
								l=(l[0:i]+'o'+l[i+1:len(l)])
								vwi[i].occupied=False
								vwi[i].b.config(state=DISABLED)
								print(vwi)
								tlp=False
								break
				if tlp:
					if l[4]=='_' and b5.occupied==True:
									b5.b.config(text='o')
									l=(l[0:4]+'o'+l[5:len(l)])
									b5.occopied=False
									b5.b.config(state=DISABLED)
					elif l[0]=='_' :
						b1.b.config(text='o')
						l=('o'+l[1:len(l)])
						b1.occopied=False
						b1.b.config(state=DISABLED)
					elif l[2]=='_' :
						b3.b.config(text='o')
						l=(l[0:2]+'o'+l[3:len(l)])
						b3.occopied=False
						b3.b.config(state=DISABLED)
					elif l[6]=='_' :
						b7.b.config(text='o')
						l=(l[0:6]+'o'+l[7:len(l)])
						b7.occopied=False
						b7.b.config(state=DISABLED)
					elif l[8]=='_' :
						b9.b.config(text='o')
						l=(l[0:8]+'o')
						b9.occopied=False
						b9.b.config(state=DISABLED)
					elif l[1]=='_' :
						b2.b.config(text='o')
						l=(l[0]+'o'+l[2:len(l)])
						b2.occopied=False
						b2.b.config(state=DISABLED)
					elif l[3]=='_' :
						b4.b.config(text='o')
						l=(l[0:3]+'o'+l[4:len(l)])
						b4.occopied=False
						b4.b.config(state=DISABLED)
					elif l[5]=='_' :
						b6.b.config(text='o')
						l=(l[0]+'o'+l[2:len(l)])
						b6.occopied=False
						b6.b.config(state=DISABLED)
					elif l[7]=='_' :
						b8.b.config(text='o')
						l=(l[0:7]+'o'+l[8:len(l)])
						b8.b.config(state=DISABLED)
				tlp=True
			self.check()					
mode=1
print(l[0:7])
xv=71
yv=77
tlp=True
root=Tk()
b1=bu(xv*0,yv*0)
b2=bu(xv*1,yv*0)
b3=bu(xv*2,yv*0)
b4=bu(xv*0,yv*1)
b5=bu(xv*1,yv*1)
b6=bu(xv*2,yv*1)
b7=bu(xv*0,yv*2)
b8=bu(xv*1,yv*2)
b9=bu(xv*2,yv*2)
vwi={0:b1,1:b2,2:b3,3:b4,4:b5,5:b6,6:b7,7:b8,8:b9}
root.geometry(f'{xv*3}x{(yv*3)}')
def d(a):
	global mode,l,count
	count=0
	mode=a
	l='_________'
	b1.b.config(text='  ',state=NORMAL)
	b2.b.config(text='  ',state=NORMAL)
	b3.b.config(text='  ',state=NORMAL)
	b4.b.config(text='  ',state=NORMAL)
	b5.b.config(text='  ',state=NORMAL)
	b6.b.config(text='  ',state=NORMAL)
	b7.b.config(text='  ',state=NORMAL)
	b8.b.config(text='  ',state=NORMAL)
	b9.b.config(text='  ',state=NORMAL)
	b1.occupied,b2.occupied,b3.occupied,b4.occupied,b5.occupied,b6.occupied,b7.occupied,b8.occupied,b9.occupied,=True,True,True,True,True,True,True,True,True,
from tkinter.ttk import *
menubar = Menu(root) 
file = Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='File', menu = file) 
file.add_command(label ='1 vs 1', command =lambda:d(1)  )
file.add_command(label ='payer vs bot', command =lambda:d(2)  )
file.add_command(label ='local game', command =lambda:d(3) )
root.config(menu=menubar)
root.mainloop()
