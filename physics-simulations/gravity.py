from licensing.models import *
from licensing.methods import Key, Helpers



import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from math import *
import pygame as pg
from random import randint
from tkinter import *
from tkinter import ttk
from threading import Thread
static=1
pg.init()
clk = pg.time.Clock()

fps = 400
w_, h_ = 1000, 700
dis = pg.display.set_mode((w_, h_))

run = True

G = 6.67*10**-7
continue_ = 0
lines = 1
trac_cou=1
music_count=1
font = pg.font.Font('freesansbold.ttf', 100)
font2 = pg.font.Font('freesansbold.ttf', 20)
text = font.render('GRAVITY', True, (0,0,255), (0,0,0))
simulate_text = font2.render('Start Simulating', True, (255,255,255), (0,0,0))

textRect = text.get_rect()
simulating_textRect = simulate_text.get_rect()
textRect.center = (w_ // 2, (h_ // 2)-50)
simulating_textRect.center=(w_ // 2, (h_ // 2)+50)
print(type(textRect))

class Mass:
    def __init__(self, mass, coordinates, v , radius=3,k=False):
        self.mass = mass
        self.color=(randint(0,255),randint(0,255),randint(0,255))
        self.x, self.y = coordinates
        self.x_component, self.y_component = 0, 0
        self.x_vel, self.y_vel = v
        self.radius = (self.mass) ** (1 / radius)
        self.track=[]
        self.previous=()
        self.k=k
    def update(self):

        if continue_ % 2 == 0:
            self.previous=[self.x,self.y]
            self.x_acc = self.x_component
            self.y_acc = self.y_component
            self.y_vel += self.y_acc
            self.x_vel += self.x_acc
            self.x += self.x_vel
            self.y += self.y_vel


        pg.draw.circle(dis, self.color, (self.x, self.y), (self.radius))

        if trac_cou%2==0:
            try:
                self.track.append(self.previous)
                pg.draw.lines(dis,self.color,False,self.track)

            except:
                pass
        else:
            self.track=[]
        if len(self.track)>1000:
            self.track.pop(0)



    def forces(self):
        if self.k==False:
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
                self.x_component, self.y_component = randint(-1,1),randint(-1,1)


def specifications():
    global e1, e2, e3, continue_, e4,l,root,k,t2,trac_cou,G,run
    def tracker():
        global  trac_cou
        trac_cou+=1
    def add_():
        global continue_, lines
        continue_ += 1
    def motion():
        global static
        static+=1
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
    def change_G(a):
        global G

        G=10**int(a)
        text_.config(text=f"10^{G}")

    k = True
    root2 = Tk()
    root2.config(bg="black")
    s = ttk.Style()
    tabControl = ttk.Notebook(root2)

    root = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    tab3 = ttk.Frame(tabControl)


    tabControl.add(root, text='Home')
    tabControl.add(tab2, text='Settings')
    tabControl.add(tab3, text='Help')
    tabControl.pack(expand=1, fill="both")

    #---------------------home---------------------------#

    Label(root, text="mass").pack()
    e1 = Entry(root)
    e1.pack()
    Canvas(root, height=1, width=150, bg="grey").pack()
    velocity_frame=Frame(root)
    velocity_frame.pack()

    Label(velocity_frame, text="x velocity").grid(column=0,row=0)
    e2 = Entry(velocity_frame)
    e2.grid(column=0,row=1)

    Label(velocity_frame, text="y velocity").grid(column=1,row=0)
    e3 = Entry(velocity_frame)
    e3.grid(column=1,row=1)
    Canvas(root, height=1, width=200, bg="grey").pack()
    Label(root, text="ratio of radius to mass").pack()

    e4 = Entry(root)

    e4.pack()

    Canvas(root, height=1, width=200, bg="grey").pack()
    state_frame=Frame(root)
    state_frame.pack()
    Checkbutton(state_frame, text="pause", command=add_).grid(column=0,row=0)
    Checkbutton(state_frame, text="lines", command=line).grid(column=1,row=0)
    Checkbutton(state_frame, text="tracker", command=tracker).grid(column=2, row=0)

    Checkbutton(state_frame, text="static", command=motion).grid(column=3, row=0)
    Canvas(root, height=1, width=200, bg="grey").pack()
    G_frame=Frame(root)
    G_frame.pack()
    w = Scale(G_frame, from_=-3, to=-11, orient=HORIZONTAL,command=change_G)
    w.grid(column=0,row=0)
    text_=Label(root,text="10^-3")
    text_.pack()
    Canvas(root, height=1, width=200, bg="grey").pack()
    Button(root,text="clear environment",command=clear,padx=30).pack()
    # ---------------------home---------------------------#
    # ---------------------Settings---------------------------#
    def music():
        global music_count
        music_count+=1
        if music_count%2==0:
            pg.mixer.music.stop()
        else:
            pg.mixer.music.load("alone.mp3")
            pg.mixer.music.play(-1)



    b=Checkbutton(tab2, text="Music", command=music)
    b.pack(anchor=NW)
    b.select()
    # ---------------------Settings---------------------------#
    # ---------------------help---------------------------#
    Label(tab3,text="Don't act like an idiot and figure everything out by yourself").pack()
    # ---------------------help---------------------------#
    t2=Thread(target=kill_it)
    t2.start()
    root2.mainloop()
    print("llll")

    print("yo")
    run=False
t = Thread(target=specifications)
t.daemon=True
pg.mixer.music.load("alone.mp3")
pg.mixer.music.play(-1)
l = [Mass(10000,(w_ // 2, (h_ // 2)-50),(0,0),(40),True),Mass(100,((w_ // 2)-200, (h_ // 2)-50),(-1,-1),(2))]
not_start=True
while run:

    for eve in pg.event.get():

        if eve.type == pg.QUIT:
            run = False
        if pg.mouse.get_pressed()[0]:
            if not_start:
                if simulating_textRect.collidepoint(pg.mouse.get_pos()):
                    l=[]#Mass(100,((i//10)*20+300,(i%10)*20+300),(0,0),) for i in range(0,200)]
                    dis.fill((0,0,0))
                    not_start=False
                    t.start()
                    G = 6.67 * 10 ** -5
            else:
                try:
                    m = int(e1.get())

                except:
                    m = 100
                try:
                    rm = int(e4.get())

                except:
                    rm = 2
                try:
                    xvel = -float(e2.get())

                except:
                    xvel = 0
                try:
                    yvel = -float(e3.get())
                except:
                    yvel = 0
                l.append(Mass(m, pg.mouse.get_pos(), (xvel, yvel), radius=rm,k=static%2==0))

            # l.append(Mass(30, (255, 255, 255), pg.mouse.get_pos(), (0,0)))
        if not not_start:


            if pg.mouse.get_pressed()[2] and continue_%2==1:
                x_,y_=pg.mouse.get_pos()
                for i in l :
                    if sqrt((i.x-x_)**2+(i.y-y_)**2)<i.radius:
                        l.pop(l.index(i))
                        break
    if not_start:
        dis.blit(text, textRect)
        dis.blit(simulate_text, simulating_textRect)

    clk.tick(fps)
    for i in l:
        i.forces()
        i.update()
    pg.display.flip()
    dis.fill((0, 0, 0))

pg.quit()
k=False
#! Copyright (c) 2021 Mithil Inc. All Rights Reserved. *#
