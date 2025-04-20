from tkinter import*
import random as r
root=Tk()
c=Canvas(root,height=600,width=1000,bg='white')
c.pack()
l=[]
k=3
dcol='black'
for i in range(400):
	l.append((r.randint(0,1000),r.randint(0,600)))
for ri in l:
	c.create_oval(ri[0]-k,ri[1]-k,ri[0]+k,ri[1]+k,fill=dcol)	

last=(0,0)
slast=(0,0)
#user defined variables
connections=9
mode=2
generated_connections='auto_generated'#('auto_generated'/'self_generated')
def main():
	global l
	
	if mode==2:
	   	c.delete('all')
	   	for ri in l:
	   		c.create_oval(ri[0]-k,ri[1]-k,ri[0]+k,ri[1]+k,fill=dcol)
	print(l)
	ll=l[-1]
	ki=[]
	pl=0.0
	pl2=0
	er={}
	for i in l[:-1]:
		igot=[i[0]-ll[0],i[1]-ll[1]]
		
		dis=(((igot[0])**2)+((igot[1])**2))**0.5
		ki.append(dis)
		er[dis]=[i,ll]
	ki.sort()
	le=[]
	try:
		for i in range(connections):
			le.append(er[ki[i]])
	
	except:
		pass
	try:
		for i in range(len(le))	:
			if i==0:
				dg=2
			else:
				dg=0
			c.create_line(ll[0],ll[1],le[i][0],le[i][1],fill=('blue' if i==0 else 'black') ,width=dg)  
	except:
		pass
	print('-+++',le,er)
	#c.create_text((pl[0][0]+pl[1][0])/2+20,(pl[0][1]+pl[1][1])/2,text=str(round(ki[-1],4)))
def draw(e):
	global l,last,slast
	c.create_oval(e.x-k,e.y-k,e.x+k,e.y+k,fill=dcol)
	x=e.x
	y=e.y
	l.append((x,y))
	if generated_connections=='auto_generated':
		
		main()
def ch():
	global connections
	connections=int(e.get())
e=Entry(root)
e.pack()
b3=Button(root,text='change mode',command=ch)
b3.pack()
b=Button(root,text='compare',command=main)
b.place(x=670,y=680)
c.bind('<Button-1>',draw)
root.geometry('1000x1000')
root.mainloop()