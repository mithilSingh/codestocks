import pygame as pg
from pygame import mouse

run = True
width, height = 800 , 800
origin = (width/2, height/2)
scale = 1
bg=(0,0,0)
fg=(255,255,255)
point_to_scale=0.1
dis = pg.display.set_mode((width, height))
eq = "x^6-9x^4"  # "
eq = eq.replace(" ", "")
wanted = list("1234567890(){}[]")
show_value=False
points=[]
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
def main():
        global points
        dis.fill(bg)
        q, w = None, None
        pg.draw.line(dis, fg, (0, origin[1]), (width, origin[1]))  # X'X
        pg.draw.line(dis, fg,
                 (origin[0], 0), (origin[0], height)) 
        points=[]
        for i in range(width):
            x = ((20*scale)/width)*(i-origin[0])
            y = value(eq, x)
            y2 = ((-y/(20*scale))*height)+origin[1]
        
            points.append((i,y2))
        
            if i % 50 == 0:
                pg.draw.line(dis, fg,
                            (i, origin[1]-2), (i, origin[1]+2))

                textsurface = myfont.render(
                    str(float(round(x, 1))), False, (128,128,128))
                dis.blit(textsurface, (i-5, origin[1]+3))
        pg.draw.polygon(dis,(255,0,0),points,2)
        for i in range(height):
            if i%50==0 and i!=height//2:
                y=(((height*20/width)*scale)/height)*(i-origin[1])
                pg.draw.line(dis, (fg),
                            ( origin[0]-2,i), ( origin[0]+2,i))
                textsurface = myfont.render(
                    str(float(round(-y, 1))), False, (128,128,128))
                dis.blit(textsurface, ( origin[0]+3,i-5))

            show_value=True
        pg.display.flip()
        
pg.font.init()  
myfont = pg.font.SysFont('arial', 15)
main()
while run:
    for eve in pg.event.get():
        if eve.type == pg.QUIT:
            run = False
        if eve.type == pg.MOUSEBUTTONDOWN:
            if eve.button == 4 :
                scale -= point_to_scale
                main()
            if eve.button == 5:
                scale += point_to_scale
                main()
            if scale<point_to_scale*2:
                point_to_scale/=10
                

        # if pg.mouse.get_pressed()[0] and show_value==True:

        #     print(name)
        #     pg.draw.circle(dis,(255,0,255),name,6)
            
        # elif pg.mouse.get_pressed()[0]==False  :
        #     show_value=False
        
     # X'X
    
    # name=None
    # dist=width+1
    # for x in range (width):
    #     for y in range(height):
    #         if pg.Surface.get_at(dis,(x,y))==(255,0,0,255):
    #             distance=(x-pg.mouse.get_pos()[0])**2+(y-pg.mouse.get_pos()[1])**2
    #             if distance<dist :
    #                 dist=distance
    #                 name=(x,y)
    
    
    


pg.quit()