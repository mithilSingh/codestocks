import pygame as pg
from math import acos ,sin ,cos,sqrt,radians
from random import randint,choice
pg.init()
widt=300
lent=300
dis =pg.display.set_mode((widt,lent))
run =True
class particle(pg.Rect):
    def __init__(self):
        self.x=randint(0,widt)
        self.y=randint(0,lent)
        self.color=(255,255,255)
        super().__init__(self.x,self.y,2,2)
        
        
        #pg.draw.circle(dis,(255,255,255),(self.x,self.y),1)
        
    def change(self):
        if self.x>=widt:
            self.x+=-1
        elif self.x<=0:
            self.x+=1
        else:
            self.x+=choice([-1,1])
        if self.y>=lent:
            self.y+=-1
        elif self.y<=0:
            self.y+=1
        else:
            self.y+=choice([-1,1])
        self.y+=choice([-1,1])
        
        pg.draw.circle(dis,self.color,(self.x,self.y),1)
    def color3(self,col):
        self.color=col
clk=pg.time.Clock()
mainlist=[particle() for i in range(700)]
oddlist=[particle()]

while run:
    for eve in pg.event.get():
        if eve.type ==pg.QUIT:
            run=False
        
    for i in mainlist:
        i.change()
        if pg.Rect.collidelist(i,oddlist)!=-1:
            i.color3((255,0,0))
            oddlist.append(mainlist.pop(mainlist.index(i)))
    for i2 in oddlist:
        i2.change()
    clk.tick(2000)
    
    pg.display.update()
    dis.fill((0,0,0))
