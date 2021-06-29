
from math import *
import pygame as pg

s_w,s_h=300,300

dis=pg.display.set_mode((s_w,s_h))
clk=pg.time.Clock()
center=(s_w/2,s_h/2)
run=True

class rotate:
    def __init__(self,angle):
        self.angle=angle
        self.radius=2
        self.distance_from_center=20
    def draw(self):
        x=self.distance_from_center*cos(radians(self.angle))
        y = self.distance_from_center * sin(radians(self.angle))
        pg.draw.circle(dis,(255,255,255),(center[0]+x,center[1]+y),self.radius)




l=[rotate(i) for i in range(0,96,24)]
k=1
while run:

    for eve in pg.event.get() :

        if eve.type == pg.QUIT:

            run=False


    for i in l:
        i.angle+=k
        i.draw()
    clk.tick(40)
    pg.draw.line(dis,(255,0,0),center,(center[0]+1,center[1]+1))
    pg.display.flip()
    dis.fill((0,0,0))
    k+=0.5
    if k>13:
        k=0




pg.quit()
    
