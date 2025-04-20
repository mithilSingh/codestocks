import pygame as pg 
pg.init()
dis=pg.display.set_mode((1000,500))
run=True
u=0
a=1
t=0
x=10
F=1
mass=1
a=F/mass
clk=pg.time.Clock()
k=0
while run:
    for e in pg.event.get():
        if e.type==pg.QUIT:
            run=False
            
    poi=t
    clk.tick(24)
    t=pg.time.get_ticks()
    k+=a
    x+=k
    a=F/mass
    dis.fill((0,0,0))
    re=pg.Rect(x,100,10,10)
    
    pg.draw.rect(dis,(255,255,255),re)
    pg.display.flip()
    if x>200:
        F=-3
    if x<0:
        F=()
    pg.display.flip()


pg.quit()
