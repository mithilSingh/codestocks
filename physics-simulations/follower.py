
import pygame as pg
from math import tan,radians,atan,degrees,cos,sin,sqrt, trunc

from pygame.constants import DROPCOMPLETE
mas_coordinates=(1380,705)
dis=pg.display.set_mode((mas_coordinates[0],mas_coordinates[1]))
run=True
mass=10
G=1
b=False
rais=0
vel=10
color=(165,30,225)
def xy(vel,ix,iy,fx,fy):
    opp=fx-ix
    adj=fy-iy
    try:
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
    except ZeroDivisionError:
        return 0,0
ko=False
move=False
acc=5
xvel,yvel=0,0
xpos,ypos=mas_coordinates
clk=pg.time.Clock()
x_p,y_p=0,0
while run:
    for i in pg.event.get():
        if i.type==pg.QUIT:
            run=False
        a=pg.key.get_pressed()
        if  a[pg.K_RETURN]:
            if b==False:
                b=True
            else:
                b=False
        
        
        if pg.mouse.get_pressed()[0]==True or b:
            x_p=pg.mouse.get_pos()[0]
            y_p=pg.mouse.get_pos()[1]
            ko=True
            
            move=True
            
            
            vel=   sqrt((  2*acc*    sqrt((x_p-xpos)**2+(y_p-ypos)**2)    ))
            print(vel)
            c=xy(vel,xpos,ypos,x_p,y_p)
            xvel,yvel=c[0],c[1]
    
    clk.tick(24)
    pg.draw.circle(dis,color,(xpos,ypos),10,1)
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
    
    if xvel>0 and yvel>0 and round(xpos,-1)>=round(x_p,-1) and round(ypos,-1)>=round(x_p,-1):
        xvel,yvel=0,0
        xpos,ypos=x_p,y_p
        move=False
        
        ko=False
    elif xvel<0 and yvel<0 and round(xpos,-1)<=round(x_p,-1) and round(ypos,-1)<=round(x_p,-1):
        xvel,yvel=0,0
        xpos, ypos = x_p, y_p
        move=False
        ko=False
    elif xvel>0 and yvel<0 and round(xpos,-1)<=round(x_p,-1) and round(ypos,-1)>=round(x_p,-1):
        xvel,yvel=0,0
        xpos, ypos = x_p, y_p
        move=False
        ko=False
        
    elif xvel<0 and yvel>0 and round(xpos,-1)>=round(x_p,-1) and round(ypos,-1)<=round(x_p-1):
        xvel,yvel=0,0
        xpos, ypos = x_p, y_p
        move=False
        
        ko=False
    print(xpos,ypos,x_p,y_p)
    if ko:
        
        pg.draw.line(dis,(0,0,255),(x_p-2,y_p),(x_p+2,y_p),1)
        pg.draw.line(dis,(0,0,255),(x_p,y_p-2),(x_p,y_p+2),1)
        #print("yo")
pg.quit()