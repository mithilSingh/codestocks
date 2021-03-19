import  pygame as pg 
pg.init()
unit=10
dis=pg.display.set_mode((400,400))
run=True
clk=pg.time.Clock()
def change_direction(dir):
    print (dir)
x,y=0,0
no=None
class body:
    def __init__(self,pre):
        self.pre=pre
    def update(self):
        pass
pos=[0,0]
l=[]
blocks=1
pg.draw.rect(dis ,(255,255,255),pg.Rect(0,0,unit,unit))
while run:
    for eve in pg.event.get():
        if eve.type ==pg.QUIT:
            run=False
        if eve.type == pg.KEYDOWN:
            if eve.key==pg.K_LEFT:
                no="left"
            if eve.key==pg.K_RIGHT :
                no="right"
            if eve.key==pg.K_DOWN :
                no="down"
            if eve.key==pg.K_UP :
                no="up"

    if no=="up":
        y+=-unit
    if no=="down":
        y+=unit
    if no=="right":
        x+=unit
    if no=="left":
        x-=unit
    for i in l[::-1]:
        pg.draw.rect(dis ,(255,255,255),pg.Rect(i[0],i[1],unit,unit))
        pg.display.flip()
        
    pg.display.flip()
    pos.append([x,y])
    clk.tick(2)
    dis.fill((0,0,0))
pg.quit()
print(pos)