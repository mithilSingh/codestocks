import pygame as pg
from math import acos ,sin ,cos,sqrt,radians,degrees

pg.init()
dis =pg.display.set_mode((1000,700))
acc=0.4

class bob :
    def __init__(self,x_pos,y_pos,org,str_len):
        self.x=x_pos
        self.y=y_pos
        self.org_x=org[0]
        self.org_y=org[1]
        self.strl=str_len
        pg.draw.line(dis,(50,50,50),(self.org_x,self.org_y),(self.x,self.y))
        pg.draw.circle(dis,(255,255,255),(self.x,self.y),10,)
        pg.display.update()
    def replace(self,x,y):
        self.strl=sqrt(((x-self.org_x)**2)+(y-self.org_y)**2)
        self.x=x
        self.y=y
        pg.draw.line(dis,(50,50,50),(self.org_x,self.org_y),(x,y))
        pg.draw.circle(dis,(255,255,255),(self.x,self.y),10,)
    def update(self,theta,x_,y_):
        self.x_=self.strl*cos(radians(theta))
        
        self.y_=sqrt(self.strl**2-self.x_**2)+y_
        self.x_+=x_
        '''
        
        
        
        '''
        pg.draw.line(dis,(250,250,250),(x_,y_),(self.x_,self.y_),)
        pg.draw.circle(dis,(255,255,255),(self.x_,self.y_),10,)
        ny=cos(radians(ang))*F*400
        nx=sqrt((F*400)**2-ny**2)
        
        if 90-ang>0:
            pg.draw.line(dis,(255,255,0),(self.x_,self.y_),((self.x_-nx),(self.y_+ny)),)
            pg.draw.circle(dis,(255,0,0),(self.x_-nx,self.y_+ny),3,)
            
            
        else:
            pg.draw.line(dis,(255,255,0),(self.x_,self.y_),(self.x_+nx,self.y_+ny),)
            pg.draw.circle(dis,(255,0,0),(self.x_+nx,self.y_+ny),3,)
            
        
run=True
a=bob(200,100,(500,40),400)
b=bob(500,1000,(7000,40),100)
clk=pg.time.Clock()
ang=0
vel=0

ang2=0
vel2=0
k2=0.992
k=0.993
mouse_key_not_pressed=True
while run:
    for eve in pg.event.get():
        if eve.type==pg.QUIT:
            run=False
        if eve.type == pg.KEYDOWN:
            if eve.key==pg.K_RETURN :
                ang=0
                vel=0

                ang2=0
                vel2=0
        if pg.mouse.get_pressed()[0]:
            mouse_key_not_pressed=False
            x_p=pg.mouse.get_pos()[0]
            y_p=pg.mouse.get_pos()[1]
            a.replace(x_p,y_p)
            vel=0
            
            hyp=sqrt(((x_p-a.org_x)**2)+(y_p-a.org_y)**2)
            
            #print(degrees(acos((y_p-a.org_y)/sqrt(((x_p-a.org_x)**2)+(y_p-a.org_y)**2))),ang)
            if x_p-a.org_x>0:
                ang=90-degrees(acos((y_p-a.org_y)/sqrt(((x_p-a.org_x)**2)+(y_p-a.org_y)**2)))
            else:
                ang=90+degrees(acos((y_p-a.org_y)/sqrt(((x_p-a.org_x)**2)+(y_p-a.org_y)**2)))
                print("kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
            print(y_p-a.org_y)
            #ang=60
            a.update(ang,500,40)
            b.update(ang2,100,1000)
            pg.display.update()
            dis.fill((0,0,0))
        else:
            mouse_key_not_pressed=True
    
    clk.tick(24)
    
    if mouse_key_not_pressed:
        F=cos(radians(ang))*acc
        R_acc=F
        vel+=R_acc
        ang+=vel
        vel*=k
        
        
        
        F2=cos(radians(ang2))*acc
        R_acc2=F2
        vel2+=R_acc2
        ang2+=vel2
        vel2*=k2
        a.update(ang,500,40)
        b.update(ang2,100,1000)
        
        
    else:
        F=cos(radians(ang))*acc
        a.update(ang,500,40)
        b.update(ang2,100,1000)
    #k-=0.00005
    
    pg.display.update()
    dis.fill((0,0,0))

pg.quit()



# %%
