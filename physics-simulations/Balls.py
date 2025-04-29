import pygame as pg

from random import randint

from time  import time

pg.init()

dis=pg.display.set_mode((600,800))

clk=pg.time.Clock()

run=True

#(randint(0,1200),randint(0,700))

#[ball(i*600/k,700-i*700/k)for i in range(k,0,-1)]+[ ball(1200-i*600/k,700-i*700/k)for i in range(k,0,-1)

#[ball(i*600/k,i*700/k)for i in range(k)]+[ ball(1200-i*600/k,-i*700/k)for i in range(k,0,-1)

class ball():

	def __init__(self,x,y):		
		self.x=x
		self.y=y
		self.sz=2
		self.p=0

		self.t=0

		self.vel=0  

		self.col=(randint(0,255),randint(0,255),randint(0,255))

	def draw(self):

		pg.draw.circle(dis,self.col,(self.x+self.sz/2,self.y+self.sz/2),self.sz)

		

k=100

l=[ball(i*600/k,i*700/k)for i in range(k)]+[ ball(1200-i*600/k,-i*700/k)for i in range(k,0,-1)]

fr=24

g=9.8/fr

floor=700

while run:

	for i in pg.event.get():

		if i.type==pg.QUIT:

			run=False

		if pg.mouse.get_pressed()[0]==True :

			l.append(ball(pg.mouse.get_pos()[0],pg.mouse.get_pos()[1]))

	

	for i in l:

		i.draw()

		

		if i.p==1 and time()-i.t>3:# and time()-i.t<5:

			

			l.pop(l.index(i))

		

				

			

		i.vel+=g

		i.y+=i.vel

		if i.y>floor:			

				

			i.vel*=-1

			i.vel+=3

			i.y=floor

			if i.vel>0 and i.vel<=10 and i.p==0:

			

				i.p=1

				i.t=time()

				

	clk.tick(fr)

	pg.display.flip()

	dis.fill((0,0,0))

pg.quit()
