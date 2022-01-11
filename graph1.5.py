import pygame as pg
from pygame import mouse

run = True
width, height = 800 , 800
origin = (width/2, height/2)
scale = 1
bg=(0,0,0)
fg=(255,255,255)
dis = pg.display.set_mode((width, height))
eq = "x^6-9x^4"  # "
eq = eq.replace(" ", "")
wanted = list("1234567890(){}[]")
show_value=False

def value(eq, replacement):
    k = list(eq)
    for i in range(len(k)):
        if k[i] == "x":
            try:
                if k[i-1] in wanted and i != 0:
                    k.insert(i, "*")
            except IndexError:
                pass
            try:
                if k[i+1] in wanted:
                    k.insert(i+1, "*")
            except IndexError:
                pass
        elif k[i] == "^":

            k[i] = "**"
    eq = "".join(k)
    eq = eq.replace("x", "("+str(replacement)+")")
    # print(eq)
    return eval(eq)


pg.font.init()  
myfont = pg.font.SysFont('arial', 15)
while run:
    for eve in pg.event.get():
        if eve.type == pg.QUIT:
            run = False
        if eve.type == pg.MOUSEBUTTONDOWN:
            if eve.button == 4 and scale > 0.5:
                scale -= 0.5
                
            if eve.button == 5:
                scale += 0.5
        if pg.mouse.get_pressed()[0] and show_value==True:
            print(round(((20*scale)/width)*(pg.mouse.get_pos()[0]-origin[0]),3),round(((20*(height/width)*scale)/height)*(pg.mouse.get_pos()[1]-origin[1]),3))

        elif pg.mouse.get_pressed()[0]==False  :
            show_value=False
        if eve.type == pg.KEYDOWN:

            if eve.key == pg.K_UP:
                scale += 0.1
            if eve.key == pg.K_DOWN and scale > 0.2:
                scale -= 0.1
    
    # if round((origin[1]-pg.mouse.get_pos()[1])*scale/(40))==round(value(eq,((20*scale)/width)*(pg.mouse.get_pos()[0]-origin[0]))):
    #     pg.draw.circle(dis,(255,0,0),pg.mouse.get_pos,5)


    # # print(pg.mouse.get_pos()[1])
    # print(round((origin[1]-pg.mouse.get_pos()[1])*scale/(40)),round(value(eq,((20*scale)/width)*(pg.mouse.get_pos()[0]-origin[0]))))#,,,,value(eq,((20*scale)/width)*(pg.mouse.get_pos()[0]-origin[0])))
    
    q, w = None, None
    pg.draw.line(dis, fg, (0, origin[1]), (width, origin[1]))  # X'X
    pg.draw.line(dis, fg,
                 (origin[0], 0), (origin[0], height))  # X'X

    
    for i in range(width):
        x = ((20*scale)/width)*(i-origin[0])
        y = value(eq, x)
        y2 = ((-y/(20*scale))*height)+origin[1]
        # print(x,y,y2)
        # pg.draw.circle(dis,(255,255,255),(i,y2),1,)
        if q == None:
            pg.draw.line(dis, (255, 0 , 0), (i, y2), (i, y2),2)
            q, w = i, y2
        else:
            pg.draw.line(dis, (255, 0, 0), (q, w), (i, y2),2)
            q, w = i, y2
        if i % 50 == 0:
            pg.draw.line(dis, fg,
                         (i, origin[1]-2), (i, origin[1]+2))

            textsurface = myfont.render(
                str(float(round(x, 1))), False, (128,128,128))
            dis.blit(textsurface, (i-5, origin[1]+3))
    for i in range(height):
        if i%50==0 and i!=height//2:
            y=(((height*20/width)*scale)/height)*(i-origin[1])
            pg.draw.line(dis, (fg),
                         ( origin[0]-2,i), ( origin[0]+2,i))
            textsurface = myfont.render(
                str(float(round(y, 1))), False, (128,128,128))
            dis.blit(textsurface, ( origin[0]+3,i-5))

    if pg.Surface.get_at(dis,pg.mouse.get_pos())==(255,0,0,255):
        pg.draw.circle(dis,(255,0,0),pg.mouse.get_pos(),5)
        # print(round(((20*scale)/width)*(pg.mouse.get_pos()[0]-origin[0]),3),round(((20*(height/width)*scale)/height)*(pg.mouse.get_pos()[1]-origin[1]),3))
        show_value=True
    pg.display.flip()
    dis.fill(bg)

pg.quit()

