import numpy as np
import pygame as pg
cell_size=20
width=1400
height=700
x_cells=width//cell_size
y_cells=height//cell_size

dis = pg.display.set_mode((x_cells*cell_size,y_cells*cell_size))
run=True
clk=pg.time.Clock()

l=np.zeros((x_cells,y_cells))
l[1][1]=1
l[2][2]=1
l[2][3]=1
l[3][1]=1
l[3][2]=1

l2=l.copy()
start=False
while run:
    for eve in pg.event.get():
        if eve.type==pg.QUIT:
            run=False
        if eve.type==pg.KEYDOWN:
            if eve.key==pg.K_RETURN:
                start=True
                print("po")

    if pg.mouse.get_pressed()[0]==1:
        x,y=pg.mouse.get_pos()
        l[y//cell_size][y//cell_size]=1
    if pg.mouse.get_pressed()[0]==1:
        x,y=pg.mouse.get_pos()
        l[y//cell_size][y//cell_size]=0
    for i in range(x_cells) :
        pg.draw.line(dis,(255,255,255),(i*cell_size+cell_size,0),(i*cell_size+cell_size,height))
    for i in range(y_cells) :
        pg.draw.line(dis,(255,255,255),(0,i*cell_size+cell_size),(width,i*cell_size+cell_size))
    
    for i in range(len(l)):
        for j in range(len(l[i])):
                if l[i][j]==1:
                    pg.draw.rect(dis,(255,255,255),pg.Rect(j*cell_size,i*cell_size,cell_size,cell_size))
                    n=0
                    for x in range(j-1,j+2):
                        for y in range(i-1,i+2):
                            try :
                                if l[y][x]==1 and (i,j)!=(y,x):
                                    n+=1
                            except IndexError:
                                pass

                    if n>3 or n<2:
                        l2[i][j]=0
                        
                if l[i][j]==0:
                    n=0
                    for x in range(j-1,j+2):
                        for y in range(i-1,i+2):
                            try:
                                if l[y][x]==1 and (i,j)!=(y,x):
                                    n+=1
                            except IndexError:
                                pass
                    if n==3:
                        l2[i][j]=1
        
    l=l2.copy()
    pg.display.flip()
    dis.fill((0,0,0))
    clk.tick(8)
pg.quit()
