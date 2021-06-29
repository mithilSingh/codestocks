from math import*
import pygame as pg
from random import randint
clk=pg.time.Clock()

fps=40
w,h=700,700
dis=pg.display.set_mode((w,h))

run=True

G=0.000001

class Mass:
    def __init__(self,mass,color,coordinates,v):
        self.mass=mass
        self.color=color
        self.x,self.y=coordinates
        self.x_component,self.y_component=0,0
        self.x_vel,self.y_vel=0,v
        self.radius=(self.mass)**(1/3)
    def update(self):
        self.x_acc=self.x_component
        self.y_acc=self.y_component
        self.y_vel+=self.y_acc
        self.x_vel+=self.x_acc
        self.x+=self.x_vel
        self.y+=self.y_vel
        print(self.mass)
        pg.draw.circle(dis,self.color,(self.x,self.y),(self.radius))


    def forces(self):
        try:
            self.x_component, self.y_component = 0, 0
            self.y_acc, self.x_acc = 0, 0
            for i in l:
                if i!=self:
                    y=self.y-i.y
                    x=self.x-i.x
                    r= sqrt((y)**2+(x)**2)
                    theta=asin(y/r)
                    F=(G*i.mass)/r*r


                    if x>0:

                        self.x_component+=-F*cos(theta)
                        self.y_component+=-F*sin(theta)
                    elif x<0:
                        self.x_component += F * cos(theta)
                        self.y_component += -F * sin(theta)
                    pg.draw.line(dis,(200,0,0),(i.x,i.y),(self.x,self.y))


        except:
            self.x_component, self.y_component = 0, 0


l=[    Mass(20000,(255,255,255),(400,400),0)

]

while run:

    for eve in pg.event.get() :

        if eve.type == pg.QUIT:

            run=False
        if pg.mouse.get_pressed()[0]:
            l.append(Mass(30,(255,255,255),pg.mouse.get_pos(),2))
    clk.tick(fps)
    for i in l:
        i.forces()
        i.update()
    pg.display.flip()
    dis.fill((0,0,0))

pg.quit()
    
