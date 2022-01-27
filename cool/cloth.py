from math import dist

import pygame as pg

width,height=1400,700
dis = pg.display.set_mode((width,height))
run=True
clk=pg.time.Clock()
fps=200
gravity=9.8/fps
bounse_constant=0.1
friction=1
dig=dist((height,width),(0,0))
class Dot:
    def __init__(self, x,y,oldx,oldy,static=False):

        self.x=x
        self.y=y
        self.oldx=oldx
        self.oldy=oldy
        self.radius=1
        self.static=static
    def update(self):
        if  self.static==False:
            xv=(self.x-self.oldx)
            yv=(self.y-self.oldy)+gravity
            self.oldx,self.oldy=self.x,self.y
            self.x+=xv*friction
            self.y+=yv*friction
            if self.x>width:
                self.x=width-1
                self.oldx=width+bounse_constant*xv
            if self.y>height:
                self.y=height-1
                self.oldy=height+bounse_constant*yv
            if self.x<0:
                self.x=1
                self.oldx=self.x+bounse_constant*xv
            if self.y<0:
                self.y=1
                self.oldy=self.y+bounse_constant*yv
            
        elif self.static=="move":
            self.x,self.y=pg.mouse.get_pos()
        
    def draw(self):
        pg.draw.circle(dis,(255,255,255),(self.x,self.y),self.radius)
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
        pg.draw.line(dis,(255*(dist((0,0),(self.p1.x,self.p1.y))/dig),255*(dist((0,height),(self.p1.x,self.p1.y))/dig),255*(dist((width,0),(self.p1.x,self.p1.y))/dig)),(self.p1.x,self.p1.y),(self.p2.x,self.p2.y))
def break_it():
    for i in range(len(sticks)):
        if dist((sticks[i].p1.x,sticks[i].p1.y),pg.mouse.get_pos())<15:# or (sticks[i].p2.x,sticks[i].p2.y)==pg.mouse.get_pos():
            sticks.pop(i)
            break
        

# dots=[
#     Dot(100,200,100,100),
#     Dot(200,200,100,100),
    
#     Dot(300,200,100,200,"l"),
# ]
# sticks=[
    
#     Stick(dots[0],dots[1]),
#     Stick(dots[1],dots[2]),

# ]





dots=[]
sticks=[]
n=25
de=20
for i in range(n):
    for j in range(n):
        dots.append(Dot(j*de+300,i*de,j*de+300,i*de))
for i in range(n-1):
    for j in range(n-1):
        sticks.append(Stick(dots[i+j*n],dots[i+1+j*n] ))
        sticks.append(Stick(dots[i+j*n],dots[i+(j+1)*n] ))
       
        if i==n-2:
            sticks.append(Stick(dots[i+1+j*n],dots[i+1+(j+1)*n] ))
        if j==n-2:
            sticks.append(Stick(dots[i+(j+1)*n],dots[i+1+(j+1)*n] ))

dots[0].static=True
dots[n-1].static=True
dots[n*n-n].static=True
dots[n*n-1].static="move"

        
while run:
    for eve in pg.event.get():
        if eve.type==pg.QUIT:
            run=False
        if pg.mouse.get_pressed()[0]:
            break_it()
        if pg.mouse.get_pressed()[2]:
            print("hi")
    
    for i in dots:
        i.update()
        i.draw()
    for i in sticks:
        for ik in range(5):
            i.update()
        i.draw()
    clk.tick(fps)
    pg.display.flip()
    dis.fill(
