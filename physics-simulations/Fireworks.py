from random import randint
import pygame as pg
from math import*
height,width=1200,700
pg.init()
dis = pg.display.set_mode((width,height))
n=90
g=0.2
clk = pg.time.Clock()

class rocket:
	def __init__(self,color,x=0,y=0,xvel=0,yvel=0,part=False):
		if not part:
			self.x=randint(0,width)
			self.y=height

			self.yvel=randint(-19,-7)
			self.color=color
			self.destroyed=False
			self.parts=[]
			self.xvel=xvel
			self.ts=0
		else:
			self.x=x
			self.y=y
			self.yvel=yvel
			self.xvel=xvel
			self.color=color
			self.destroyed=False
			
		
	def draw(self):
		pg.draw.circle(dis,self.color,(self.x,self.y),2)
	def update(self):
		self.yvel+=g
		self.y+=self.yvel
		
		self.x+=self.xvel
		
	def check(self):
		if self.yvel>=0 and self.destroyed==False:
			self.destroyed=True

l=[]

run=True
while run:
    for ev in pg.event.get():
    	if ev.type==pg.QUIT:
    		run=False
    if randint(0,20)==7:
    	l.append(rocket((randint(150,255),randint(150,255),randint(150,255))))
    for i in l:
    	if not i.destroyed:
    		i.draw()
    		i.update()
    	else:
    		i.ts+=1
    		#l.pop(l.index(i))
    		if len( i.parts)==0:
    			for i2 in range(n+1):
    				i.parts.append(rocket(i.color,i.x,i.y,randint(1,5)*cos(radians(i2*360/100)),randint(1,5)*sin(radians(i2*360/100)),True))
    		for j in i.parts:
    			j.draw()
    			j.update()
    			
    		if i.ts>50:
    			l.pop(l.index(i))
    			
    			
    			
    	i.check()
    pg.display.flip()
    dis.fill((0,0,0,))
    clk.tick(35)
pg.quit()
