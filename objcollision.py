import pygame as pg
from math import tan,radians,atan,degrees,cos,sin

dis=pg.display.set_mode((400,400))
run=True
mass=10
G=1
mas_coordinates=(200,200)

vel=10
def xy(vel,ix,iy,fx,fy):
    opp=fx-ix
    adj=fy-iy
    theta=degrees(atan((opp/adj)))
    print(theta)

    if opp<0 and adj<0:
        y = sin(radians(theta)) * -vel
        x = cos(radians(theta)) * -vel
        print("-","-")
    elif opp>0 and adj>0:
        y = sin(radians(theta)) * vel
        x = cos(radians(theta)) * vel
        print("+", "+")
    elif opp<0 and adj>0:
        y = sin(radians(theta)) * vel
        x = cos(radians(theta)) * vel
        print("-", "+")


    elif opp>0 and adj <0:
        y = sin(radians(theta)) * -vel
        x = cos(radians(theta)) * -vel
        print("+", "-")
    return (x,y)
xvel,yvel=0,0
xpos,ypos=200,200
clk=pg.time.Clock()
x_p,y_p=0,0
while run:
    for i in pg.event.get():
        if i.type==pg.QUIT:
            run=False
        if pg.mouse.get_pressed()[0]==True:

            x_p=pg.mouse.get_pos()[0]
            y_p=pg.mouse.get_pos()[1]
            c=xy(vel,xpos,ypos,x_p,y_p)
            xvel,yvel=c[0],c[1]
    clk.tick(24)
    pg.draw.circle(dis,(255,255,255),(xpos,ypos),10)
    xpos+=yvel
    ypos += xvel
    pg.display.flip()
    dis.fill((0,0,0))
    if xvel>0 and yvel>0 and (xpos>x_p or ypos>x_p):
        xvel,yvel=0,0
    elif xvel<0 and yvel<0 and (xpos<x_p or ypos<x_p):
        xvel,yvel=0,0
    elif xvel>0 and yvel<0 and (xpos<x_p and ypos>x_p):
        xvel,yvel=0,0
    elif xvel<0 and yvel>0 and (xpos>x_p and ypos<x_p):
        xvel,yvel=0,0

pg.quit()