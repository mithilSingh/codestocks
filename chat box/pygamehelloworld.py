import pygame  as pg
pg.init()
ww,wh=900,700  
win=pg.display.set_mode((ww,wh))
pg.display.set_caption(("hi"))
loo=True
x,y=430,330
w,h=5,5
j=True
jc=10
while loo:
    pg.time.delay(40)
    for event in pg.event.get():
        if event.type==pg.QUIT:
            loo=False
    ky=pg.key.get_pressed()
    if ky[pg.K_LEFT]and x>0:
        x-=10
    if ky[pg.K_RIGHT] and x<ww-w:
        x+=10
    if j==True:
        if ky[pg.K_UP] and y>0:
            y-=10

        if ky[pg.K_DOWN]and y<wh-h:
            y+=10
        if ky[pg.K_SPACE]:
            j=False
    else:
        if jc>=-10:
            m=1
            if jc<0:
                m=-1
            y-=jc**2*0.5*m
            jc-=1
         
        else:
            jc=10
            j=True
   
    win.fill((0,0,0))
    pg.draw.rect(win,(255,255,255),(x,y,w,h))
    
    
    pg.display.update()
pg.quit()

        