import pygame as pg
from math import sqrt
from random import randint


height = 600
width = 1200
run = True
acc = 0.9
clk = pg.time.Clock()
number_of_circles = 100
dis = pg.display.set_mode((width, height))


class Circle:
    def __init__(self, center_cordinates, radius):
        self.x, self.y = center_cordinates
        self.radius = radius
        self.color = (255, 0, 255)
        self.lastUP = (0, 0)
        self.vx = 0
        self.vy = 0

    def update(self):


        self.y += self.vy
        self.x += self.vx
        self.vy -= self.vy * 0.05
        self.vx -= self.vx * 0.05
        '''print("new one",(self.x, self.y))
        print("old one",self.lastUP)
        print("####################################################",self.vy)'''
        #print(self.x, self.y)
        pg.draw.circle(dis, self.color, (self.x, self.y), self.radius, 2 )


    def color_c(self, col=(255, 255, 255)):
        self.color = col

    def check(self, main_list, pre_x, pre_y):

        for i in main_list:

            k = abs(sqrt((i.x - self.x) ** 2 + (i.y - self.y) ** 2))
            if i != self:

                if k < self.radius + i.radius:
                    try:
                        '''i.x+=(i.x-pre_x)*0.09
                        i.y+=(i.y-pre_y)*0.09
                        print((i.x-pre_x),(i.y-pre_y))
                        '''
                        self.vx = -(i.x - pre_x)*0.1
                        self.vy = -(i.y - pre_y)*0.1
                        print((i.x - i.lastUP[0]))
                    except:
                        print("error")


l = [Circle((randint(0,width),randint(0,height)), 20) for i in range( number_of_circles)]
mo = Circle((0, 0), 500)
mo.color_c((0, 255, 0))
l.append(mo)
while run:
    for eve in pg.event.get():
        if eve.type == pg.QUIT:
            run = False
    mo.x, mo.y = pg.mouse.get_pos()

    l2 = l.copy()
    l2.pop(l.index(mo))
    mo.update()
    '''mo.check(l, mo.lastUP[0], mo.lastUP[1])'''
    pg.draw.circle(dis, mo.color, (mo.x, mo.y), mo.radius, 5)
    mo.lastUP = (mo.x, mo.y)
    for i in l2:
        i.check(l, i.lastUP[0], i.lastUP[1])

        i.lastUP = (i.x, i.y)

        i.update()




    pg.display.flip()
    dis.fill((0, 0, 0))
    clk.tick(100)
pg.quit()
