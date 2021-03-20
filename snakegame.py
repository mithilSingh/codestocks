import  pygame as pg 
from random import randint
pg.init()
unit=10
dis=pg.display.set_mode((400,400))
run=True
clk=pg.time.Clock()
no=None
l=[]
blocks=1
score=0
food=False
x,y=0,blocks*unit
pos=[blocks*unit,blocks*unit]
font = pg.font.SysFont("comicsansms", 20)
ghy=True
pg.draw.rect(dis ,(255,255,255),pg.Rect(blocks*unit,blocks*unit,unit,unit))
def lost():
    global ghy
    text = font.render("you lost", True, (0, 128, 0))
    pg.draw.rect(dis ,(255,0,0),food_box)
    dis.blit(text,
        (   200,200))
    
    ghy=False
while run:
    for eve in pg.event.get():
        if eve.type ==pg.QUIT:
            run=False

        if eve.type == pg.KEYDOWN:
            if eve.key==pg.K_LEFT and no!="right":
                no="left"
            if eve.key==pg.K_RIGHT and no!="left":
                no="right"
            if eve.key==pg.K_DOWN and no!="up":
                no="down"
            if eve.key==pg.K_UP and no!="down":
                no="up"
    
    if ghy:
        if no=="up" :
            y+=-unit
        if no=="down":
            y+=unit
        if no=="right":
            x+=unit
        if no=="left":
            x-=unit
    kia=[]
    for i in l[::-1]:
        bp=pg.Rect(i[0],i[1],unit,unit)
        kia.append(bp)
        pg.draw.rect(dis ,(255,255,255),bp)
    pg.display.flip()    
    pg.display.flip()
    l.append([x,y])
    clk.tick(10)
    dis.fill((0,0,0))
    if x>400:
        
        x=0
    if x<0:
        
        x=400
    if y>400:
        
        y=0
    if y<0:
       
        y=400
    if len(l)>blocks:
        l=l[-blocks:]
    if food==False:
        fpx=randint(0,39)*10
        fpy=randint(0,39)*10
        food_box=pg.Rect(fpx,fpy,unit,unit)
        
        food=True
    try:
        if pg.Rect.contains(food_box,kia[0]):
            print("collided")
            food=False
            blocks+=1
            score+=1
            
    except IndexError:
        print()
    try:
        if pg.Rect.collidelist(kia[0],kia[1:])!=-1:
            lost()
            print("collided with itself")
                 
    except IndexError:
        pass
    text = font.render("score:"+str(score), True, (0, 128, 0))
    pg.draw.rect(dis ,(255,0,0),food_box)
    dis.blit(text,
        (320,0))
    pg.display.flip()
#pg.quit()
print(pos)