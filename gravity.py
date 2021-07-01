import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from math import *
import pygame as pg
from random import randint
from tkinter import *
from threading import Thread

clk = pg.time.Clock()

fps = 40
w, h = 1000, 700
dis = pg.display.set_mode((w, h))

run = True

G = 0.00001
continue_ = 0
lines = 1


class Mass:
    def __init__(self, mass, color, coordinates, v, radius=3):
        self.mass = mass
        self.color = color
        self.x, self.y = coordinates
        self.x_component, self.y_component = 0, 0
        self.x_vel, self.y_vel = v
        self.radius = (self.mass) ** (1 / radius)

    def update(self):
        if continue_ % 2 == 0:
            self.x_acc = self.x_component
            self.y_acc = self.y_component
            self.y_vel += self.y_acc
            self.x_vel += self.x_acc
            self.x += self.x_vel
            self.y += self.y_vel

        pg.draw.circle(dis, self.color, (self.x, self.y), (self.radius))

    def forces(self):
        try:
            self.x_component, self.y_component = 0, 0
            self.y_acc, self.x_acc = 0, 0
            for i in l:
                if i != self:
                    y = self.y - i.y
                    x = self.x - i.x
                    r = sqrt((y) ** 2 + (x) ** 2)
                    theta = asin(y / r)
                    F = (G * i.mass) / r * r

                    if x > 0:

                        self.x_component += -F * cos(theta)
                        self.y_component += -F * sin(theta)
                    elif x < 0:
                        self.x_component += F * cos(theta)
                        self.y_component += -F * sin(theta)
                    if lines % 2 == 0:
                        pg.draw.line(dis, (200, 0, 0), (i.x, i.y), (self.x, self.y))


        except:
            self.x_component, self.y_component = 0, 0


def specifications():
    global e1, e2, e3, continue_, e4,l,root,k,t2

    def add_():
        global continue_, lines
        continue_ += 1

    def line():
        global lines
        lines += 1
    def clear():
        global l
        l=[]
    def kill_it():
        while 1:
            if not k:
                root.destroy()
                break
    k=True
    root = Tk()
    Label(root, text="mass").pack()
    e1 = Entry(root)
    e1.pack()
    velocity_frame=Frame(root)
    velocity_frame.pack()
    Label(velocity_frame, text="x velocity").grid(column=0,row=0)
    e2 = Entry(velocity_frame)
    e2.grid(column=0,row=1)
    Label(velocity_frame, text="y velocity").grid(column=1,row=0)
    e3 = Entry(velocity_frame)
    e3.grid(column=1,row=1)

    Label(root, text="ratio of radius to mass").pack()

    e4 = Entry(root)

    e4.pack()
    lin=Canvas(root,height=1,width=200,bg="grey")
    lin.pack()
    state_frame=Frame(root)
    state_frame.pack()
    Checkbutton(state_frame, text="pause", command=add_).grid(column=0,row=0)
    Checkbutton(state_frame, text="lines", command=line).grid(column=1,row=0)
    Button(root,text="clear enviourment",command=clear,padx=30).pack()
    t2=Thread(target=kill_it)
    t2.start()
    root.mainloop()
    print("llll")

    print("yo")
t = Thread(target=specifications)
t.daemon=True
t.start()
l = []

while run:

    for eve in pg.event.get():

        if eve.type == pg.QUIT:
            run = False
        if pg.mouse.get_pressed()[0]:

            try:
                m=int(e1.get())

            except:
                m=100
            try:
                rm=int(e4.get())

            except:
                rm=2
            try:
                xvel=-int(e2.get())

            except:
                xvel=0
            try:
                yvel= -int(e3.get())
            except:
                yvel=0
            l.append(Mass(m, (255, 255, 255), pg.mouse.get_pos(), (xvel,yvel) ,rm))


            # l.append(Mass(30, (255, 255, 255), pg.mouse.get_pos(), (0,0)))

    clk.tick(fps)
    for i in l:
        i.forces()
        i.update()
    pg.display.flip()
    dis.fill((0, 0, 0))

pg.quit()
k=False

