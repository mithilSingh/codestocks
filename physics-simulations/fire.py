import pygame as pg

from random import randint,choice
pg.init()
widt=700
lent=600
swit=0
slen=400
dis =pg.display.set_mode((widt,lent))
run =True
class particle():
    def __init__(self):
        self.x=randint(swit,widt)
        self.y=lent-10
        self.color=choice([(255,0,0)for i in range(80)]+[(255,255,0)for i in range(20)])
        #print(choice([ (255,0,0) for i in range(90) ,(255,255,0) for i in range (10) ]))
        
        
        
        #pg.draw.circle(dis,(255,255,255),(self.x,self.y),1)
        
    def change(self):
        if self.x>=widt:
            self.x+=-1
        elif self.x<=swit:
            self.x+=1
        else:
            self.x+=randint(-3,3)
        if self.y>=lent:
            self.y+=-1
        elif self.y<=slen:
            self.y+=1
        else:
            self.y+=randint(-9,10)
        
        
        pg.draw.circle(dis,self.color,(self.x,self.y),1)
    
clk=pg.time.Clock()
mainlist=[particle() for i in range(10000)]


while run:
    for eve in pg.event.get():
        if eve.type ==pg.QUIT:
            run=False
        
    for i in mainlist:
        i.change()
     
    
    clk.tick(2000)
    
    pg.display.update()
    dis.fill((0,0,0))