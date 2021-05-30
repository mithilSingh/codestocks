  
  
from tkinter.constants import S
import pygame as pg
from math import tan,radians,atan,degrees,cos,sin,sqrt, trunc

from pygame.constants import DROPCOMPLETE
mas_coordinates=(1000,700)
dis=pg.display.set_mode((mas_coordinates[0]*2,mas_coordinates[1]*2))
run=True
mass=10
G=1

rais=0
vel=10
def xy(vel,ix,iy,fx,fy):
    opp=fx-ix
    adj=fy-iy
    theta=degrees(atan((opp/adj)))

    if opp<0 and adj<0:
        y = sin(radians(theta)) * -vel
        x = cos(radians(theta)) * -vel
        
    elif opp>0 and adj>0:
        y = sin(radians(theta)) * vel
        x = cos(radians(theta)) * vel
        
    elif opp<0 and adj>0:
        y = sin(radians(theta)) * vel
        x = cos(radians(theta)) * vel
        


    elif opp>0 and adj <0:
        y = sin(radians(theta)) * -vel
        x = cos(radians(theta)) * -vel
        
    else:
        x,y=0,0
    return (x,y)
ko=False
move=False
acc=0.1
xvel,yvel=0,0
xpos,ypos=mas_coordinates
clk=pg.time.Clock()
x_p,y_p=0,0
while run:
    for i in pg.event.get():
        if i.type==pg.QUIT:
            run=False
        if pg.mouse.get_pressed()[0]==True:
            x_p=pg.mouse.get_pos()[0]
            y_p=pg.mouse.get_pos()[1]
            ko=True
            
            move=True
            
            
            vel=   sqrt((  2*acc*    sqrt((x_p-xpos)**2+(y_p-ypos)**2)    ))
            print(vel)
            c=xy(vel,xpos,ypos,x_p,y_p)
            xvel,yvel=c[0],c[1]
    
    clk.tick(24)
    pg.draw.circle(dis,(255,255,255),(xpos,ypos),10)
    xpos+=yvel
    ypos += xvel
    pg.display.flip()
    dis.fill((0,0,0))
    if move:
        vel-=acc
        c=xy(vel,xpos,ypos,x_p,y_p)
        xvel,yvel=c[0],c[1]
        #print("stoped",rais)
        rais+=1
    
    if xvel>0 and yvel>0 and round(xpos)>=x_p and round(ypos)>=x_p:
        xvel,yvel=0,0
        move=False
        
        ko=False
    elif xvel<0 and yvel<0 and round(xpos)<=x_p and round(ypos)<=x_p:
        xvel,yvel=0,0
        move=False
        ko=False
    elif xvel>0 and yvel<0 and round(xpos)<=x_p and round(ypos)>=x_p:
        xvel,yvel=0,0
        move=False
        ko=False
        
    elif xvel<0 and yvel>0 and round(xpos)>=x_p and round(ypos)<=x_p:
        xvel,yvel=0,0
        move=False
        
        ko=False
    print(xpos,ypos,x_p,y_p)
    if ko:
        
        pg.draw.line(dis,(0,0,255),(x_p-2,y_p),(x_p+2,y_p),1)
        pg.draw.line(dis,(0,0,255),(x_p,y_p-2),(x_p,y_p+2),1)
        #print("yo")
pg.quit()
