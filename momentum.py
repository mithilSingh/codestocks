import pygame as pg 
from math import sin ,cos,sqrt,radians
pg.init()
dis=pg.display.set_mode((700,500))
run=True
a=100
st_len=150
st_pos=(350,250)
x,y=0,0
angle=0
clk=pg.time.Clock()
sina=0
while run:
    for eve in pg.event.get():
        if eve.type ==pg.QUIT:
            run=False
    dis.fill((0,0,0))
    pg.draw.circle(dis,(255,255,255),(x+5,y+5),6)
    pg.draw.line(dis,(255,200,200),(st_pos[0],st_pos[1]),(x+5,y+5))
    
    
    pg.draw.rect(dis,(255,255,255),pg.Rect(st_pos[0],st_pos[1],2,2))
    

    sina+=0.64
    angle+=sin(radians(sina))
    if (angle%360)<180:
        opp=sin(radians(angle))*st_len
        adj=sqrt((st_len)**2-(opp)**2)
    else:
        opp=sin(radians(180-angle))*st_len*-1
        adj=sqrt((st_len)**2-(opp)**2)
    if (angle%360)>90:
        x=(adj)+st_pos[0]
        
    if (angle%360)<90 and (angle%360)<180 :
        x=(adj*-1)+st_pos[0]
    if (angle%360)>270:
        x=(adj*-1)+st_pos[0]
        
    y=(opp)+st_pos[1]
    
    pg.display.flip()
    clk.tick(120)
    
pg.quit()
