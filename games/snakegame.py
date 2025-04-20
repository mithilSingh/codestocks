import  pygame as pg 
from random import randint
pg.init()
unit=10
window_width=400
window_height=400
dis=pg.display.set_mode((window_width,window_height))
run=True
clk=pg.time.Clock()
no="down"
s_c=False
blocks=3
score=2
toto=False
food=False
x,y=0,blocks*unit
fps=10
level="easy"
l=[]
font = pg.font.SysFont("comicsansms", 20)
ghy=True
pg.draw.rect(dis ,(255,255,255),pg.Rect(blocks*unit,blocks*unit,unit,unit))
sscore=2
h=False
def lost():
    global ghy,fps
    text = font.render("you lost", True, (0, 128, 0))
    pg.draw.rect(dis ,(255,0,0),food_box)
    dis.blit(text,
        (   200,200))
    fps=0
    ghy=False
while run:
    for eve in pg.event.get():
        if eve.type ==pg.QUIT:
            run=False
        
        if eve.type == pg.KEYDOWN:
            if eve.key==pg.K_RETURN and ghy==False:
                no="down"
                s_c=False
                blocks=3
                score=0 
                sscore=0 
                toto=False
                food=False
                x,y=0,blocks*unit
                fps=10
                level="easy"
                l=[]
                ghy=True
            if eve.key==pg.K_LEFT and no!="right":
                no="left"
            elif eve.key==pg.K_RIGHT and no!="left": 
                no="right"
            elif eve.key==pg.K_DOWN and no!="up":
                no="down"
            elif eve.key==pg.K_UP and no!="down":
                no="up"
    if x>window_width:
        no="right"
        x=0
    if x<0:
        no="left"
        x=window_width
    
    if y>window_height:
        no="down"
        y=0
    if y<0:
        no="up"
        y=window_height
    if ghy:
        if no=="up" :
            y+=-unit
        elif no=="down":
            y+=unit
        elif no=="right":
            x+=unit
        elif no=="left":
            x-=unit
    kia=[]
    for i in l[::-1]:
        bp=pg.Rect(i[0],i[1],unit,unit)
        kia.append(bp)
        pg.draw.rect(dis ,(255,255,255),bp)
    pg.display.flip()    
    pg.display.flip()
    l.append([x,y])
    clk.tick(fps)
    dis.fill((0,0,0))
    
    if len(l)>blocks:
        l=l[-blocks:]
    
    if food==False:
        fpx=randint(0,window_height/unit-1)*unit
        fpy=randint(0,window_height/unit-1)*unit
        food_box=pg.Rect(fpx,fpy,unit,unit)
        
        food=True
    
    try:
        if pg.Rect.contains(food_box,kia[0]):
            sscore+=1 
            print(pg.Rect.contains(food_box,kia[0]))
            food=False
            blocks+=1
            score+=1
            
    except IndexError:
        pass
    if ghy:
        for i in kia:
            pg.draw.rect(dis,(255,255,255),i)
            print("t")
        pg.display.flip()
    try:
        if pg.Rect.collidelist(kia[0],kia[1:])!=-1:
            lost()
            
                 
    except IndexError:
        pass
    def falseit():
        global h
        h=False
    text = font.render("score:"+str(int(score)), True, (0, 128, 0))
    pg.draw.rect(dis ,(0,0,0),food_box)
    dop=pg.draw.circle(dis,(255,255,0),(fpx+((unit**2)/2)**0.5-2,fpy+(((unit)**2)/2)**0.5-2),(unit)/2,width=0)
    
    if level=="easy"  and s_c!=score:
        if sscore%3==0 and toto:#shows
            timen=pg.time.get_ticks()/1000
            fps+=0
            s_c=score
            sscore=0
            fx=randint(0,window_width/unit)*unit
            fy=randint(0,window_height/unit)*unit
            food_box_mega=pg.Rect(fx,fy,unit*2,unit*2)
            h=True
    if sscore!=0:
        toto=True
               
    try:
        if pg.Rect.contains(food_box_mega,kia[0]):
            
            h=False 
            blocks+=5
            score+=2.5
            print(f"score:{score}")
                    
            toto=False
    
    except :
        pass
        #print(pg.Rect.contains(kia[0],food_box_mega,))
    try:
        if h:
            pg.draw.circle(dis,(225,0,0),(fx+unit,fy+unit),unit)
        #print("llll",pg.Rect.contains(kia[0],food_box_mega,))
        
    except NameError:
        pass
    try:
        if pg.time.get_ticks()/1000-timen>5 and h:
            h=False
            
            food_box_mega=None
    
            
            
    except:
        pass

    pg.display.flip()
    dis.blit(text,
        (300,0))
    pg.display.flip()
    
    
    
    if h:
        lati=100-(pg.time.get_ticks()/1000-timen)*20
        print((pg.time.get_ticks()/1000-timen)*20)
        pg.draw.rect(dis,(255,0,0),pg.Rect(280,30,lati,10))

        
#pg.quit()
