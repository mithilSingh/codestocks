from math import dist
from mimetypes import init
from turtle import dot
import pygame as pg

width,height=1000,1000
dis = pg.display.set_mode((width,height))
run=True
clk=pg.time.Clock()
fps=60
gravity=9.8/fps
bounse_constant=0.9
friction=0.999

class Dot:
    def __init__(self, x,y,oldx,oldy,static=False):

        self.x=x
        self.y=y
        self.oldx=oldx
        self.oldy=oldy
        self.radius=3
        self.static=static
    def update(self):
        if not self.static:
            xv=(self.x-self.oldx)
            yv=(self.y-self.oldy)+gravity
            self.oldx,self.oldy=self.x,self.y
            self.x+=xv*friction
            self.y+=yv*friction
            if self.x>width:
                self.x=width
                self.oldx=width+bounse_constant*xv
            if self.y>height:
                self.y=height
                self.oldy=height+bounse_constant*yv
            if self.x<0:
                self.x=0
                self.oldx=self.x+bounse_constant*xv
            if self.y<0:
                self.y=0
                self.oldy=self.y+bounse_constant*yv
            

        
    def draw(self):
        pg.draw.circle(dis,(255,0,255),(self.x,self.y),self.radius)
class Stick:
    def __init__(self,p1,p2) :
        self.p1=p1
        self.p2=p2
        self.length=dist((p1.x,p1.y),(p2.x,p2.y))
    def update(self):
        k=dist((self.p1.x,self.p1.y),(self.p2.x,self.p2.y))
        d=self.length-k
        l=d/k
        xoffset=l*(self.p2.x-self.p1.x)
        yoffset=l*(self.p2.y-self.p1.y)
        if self.p1.static==False and self.p2.static==False:
            self.p1.x-=xoffset/2
            self.p1.y-=yoffset/2
            self.p2.x+=xoffset/2
            self.p2.y+=yoffset/2
        elif self.p1.static and self.p2.static==False:
            
            self.p2.x+=xoffset
            self.p2.y+=yoffset
        elif self.p2.static and self.p1.static==False:
            
            self.p1.x-=xoffset
            self.p1.y-=yoffset

    def draw(self):
        pg.draw.line(dis,(255,255,255),(self.p1.x,self.p1.y),(self.p2.x,self.p2.y))
dots=[
    Dot(100,100,120,95),
    Dot(200,100,200,200),
    Dot(200,200,200,200),
    Dot(100,200,100,200),

    Dot(210,200,230,200),

    Dot(260,200,260,200),

    Dot(310,200,290,200),

    Dot(350,100,100,200,True),


    
    
]
sticks=[
    Stick(dots[0],dots[1]),
    Stick(dots[1],dots[2]),

    Stick(dots[2],dots[3]),

    Stick(dots[3],dots[0]),
    Stick(dots[0],dots[2]),
    Stick(dots[1],dots[3]),
    Stick(dots[1],dots[-4]),
    Stick(dots[-4],dots[-3]),
    Stick(dots[-3],dots[-2]),

    Stick(dots[-2],dots[-1]),






]

while run:
    for eve in pg.event.get():
        if eve.type==pg.QUIT:
            run=False
    for i in dots:
        i.update()
        i.draw()
    for i in sticks:
        i.update()
        i.draw()
    clk.tick(fps)
    pg.display.flip()
    dis.fill((0,0,0))
    
