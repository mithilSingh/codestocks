# # import pygame as pg
# # from math import dist,cos,sin,tan,pi,sqrt
# # from time import sleep
# # from random import randint
# # run= True
# # height,width=800,800
# # diag=dist((0,0),(height,width))
# # screen=pg.display.set_mode((width,height))
# # class circle:
# #     def __init__(self,radius,pos):
# #         self.radius=radius
# #         self.pos=pos
# #     def distance(self,pos,i):
# #         return dist(pos,self.pos)-self.radius
# #     def draw(self):
# #         pg.draw.circle(screen,(200,0,200),self.pos,self.radius,width=1)
# # class line:
# #     def __init__(self,p1,p2,):
# #         self.p1=p1
# #         self.p2=p2
# #         self.slope=(self.p2[1]-self.p1[1])/(self.p2[0]-self.p1[0])
# # #         print(self.slope,p1[0])

# # #     def distance(self,pos,i):
# # #         slope=tan(i.angle)
# # #         c=self.p1[1]-self.p1[0]*self.slope
# # #         nc=pos[1]-pos[0]*slope
# # #         if (self.p1[1]-self.p1[0]*slope-nc)*(self.p2[1]-self.p2[0]*slope-nc)<0:
# # #             # print(abs((pos[1]-pos[0]*self.slope-c)/sqrt(self.slope**2+1)),self.p1[0],"hit")
# # #             return abs((pos[1]-pos[0]*self.slope-c)/sqrt(self.slope**2+1))
# # #         else:
# # #             return 3300
# # #     def draw(self):
# # #         pg.draw.line(screen,(200,200,0),self.p1,self.p2)
# # # class ray:
# # #     def __init__(self,origin,angle) :
# # #         self.pos=origin
# # #         self.angle=angle
# # #         self.endpoint=(4000,4000)
# # #     def update(self):
# # #         self.pos=pg.mouse.get_pos()
# # #         self.endpoint=(4000,4000)
# # #         opt=0
# # #         for i in elements:
# # #             startpoint=self.pos

# # #             while True:
# # #                 r=i.distance(startpoint,self)
# # #                 startpoint=(startpoint[0]+r*cos(self.angle),startpoint[1]+r*sin(self.angle))
# # #                 if r<1 or r>diag:
# # #                     endpoint=startpoint
# # #                     break 
# # #             if dist(self.endpoint,self.pos)>dist(endpoint,self.pos):
# # #                 self.endpoint=endpoint
# # #             opt+=1
        
                
                    
                 

            
# # #     def draw(self):
# # #         pg.draw.circle(screen,(230,230,230),self.pos,5)
# # #         pg.draw.line(screen,(255,255,255),self.pos,self.endpoint,1)

# # # elements=[line((200,200),(300,100)),
# # #           line((400,200),(300,100)),
# # #           line((400,200),(300,300)),
# # #           line((200,200),(300,300)),
          
          
# # #           ]
          
# # # for i in range(2):
# # #     elements.append(circle(randint(20,100),(randint(0,width),randint(0,height))))


# # # rays=[ray((100,100),pi*4/3)]
# # # ang=0.00001
# # # sepangle=0.005
# # # itt=round(pi,2)*2/sepangle
# # # for i in range(0,int(itt)):
# # #     rays.append(ray((100,100),ang))
# # #     ang+=sepangle
# # # while run:
    
# # #     screen.fill((0,0,0))
    
    
# # #     for r in rays:
# # #         r.update()
# # #         r.draw()
# # #     for el in elements:
# # #         el.draw()
# # #     pg.display.flip()
# # #     for e in pg.event.get():
# # #         if e.type==pg.QUIT:
# # #             run=False
    

# # # pg.quit()
# # import pygame as pg
# # from math import dist,cos,sin,tan,pi,sqrt,atan
# # from random import randint
# # run= True
# # height,width=800,600
# # diag=dist((0,0),(height,width))
# # screen=pg.display.set_mode((1200,height))
# # platesize=20
# # class circle:
# #     def __init__(self,radius,pos):
# #         self.radius=radius
# #         self.pos=pos
# #     def distance(self,pos,i):
# #         return dist(pos,self.pos)-self.radius
# #     def draw(self):
# #         pg.draw.circle(screen,(65, 146, 232),self.pos,self.radius,)
# # class line:
# #     def __init__(self,p1,p2,):
# #         self.p1=p1
# #         self.p2=p2
# #         self.slope=(self.p2[1]-self.p1[1])/(self.p2[0]-self.p1[0])
# #         print(self.slope,p1[0])

# #     def distance(self,pos,i):
# #         slope=tan(i.angle)
# #         c=self.p1[1]-self.p1[0]*self.slope
# #         nc=pos[1]-pos[0]*slope
# #         if (self.p1[1]-self.p1[0]*slope-nc)*(self.p2[1]-self.p2[0]*slope-nc)<0:
# #             # print(abs((pos[1]-pos[0]*self.slope-c)/sqrt(self.slope**2+1)),self.p1[0],"hit")
# #             return abs((pos[1]-pos[0]*self.slope-c)/sqrt(self.slope**2+1))
# #         else:
# #             return 3300
# #     def draw(self):
# #         pg.draw.line(screen,(65, 146, 232),self.p1,self.p2)
# # class ray:
# #     def __init__(self,origin,angle) :
# #         self.pos=origin
# #         self.angle=angle
# #         self.endpoint=(4000,4000)
# #     def update(self):
# #         self.pos=pg.mouse.get_pos()
# #         self.endpoint=(4000,4000)
# #         opt=0
# #         for i in elements:
# #             startpoint=self.pos

# #             while True:
# #                 r=i.distance(startpoint,self)
# #                 startpoint=(startpoint[0]+r*cos(self.angle),startpoint[1]+r*sin(self.angle))
# #                 if r<1 or r>diag:
# #                     endpoint=startpoint
# #                     break 
# #             if dist(self.endpoint,self.pos)>dist(endpoint,self.pos):
# #                 self.endpoint=endpoint
# #             opt+=1
# #         plates.append(dist(self.endpoint,self.pos))

# #     def draw(self):
# #         pg.draw.circle(screen,(200,200,200),self.pos,10)
# #         pg.draw.line(screen,(255,255,255),self.pos,self.endpoint,1)

# # elements=[line((500,600),(300,100)),
# #           line((400,200),(100,100)),
# #           line((100,100),(300,300)),
# #           line((200,200),(400,900)),
# #           line((width,0),(width+1,height)),
          
          
# #           ]
          
# # for i in range(2):
# #     elements.append(circle(randint(20,100),(randint(0,width),randint(0,height))))
# # fdist=width/(2*tan(30*pi/180))
# # refdist=height/tan(45*pi/180)
# # rays=[]
# # ang=0
# # sepangle=0.5*pi/180
# # maxview=pi/3
# # itt=round(maxview,2)/sepangle

# # for i in range(0,int(itt)):
# #     rays.append(ray((100,100),ang))
# #     ang+=sepangle
# # while run:
    
# #     screen.fill((0,0,0))
# #     plates=[]
# #     for r in rays:
# #         r.update()
# #         r.draw()


# #     for el in elements:
# #         el.draw()
# #     cont=-maxview/2
    
# #     pg.draw.rect(screen,(135, 206, 235),(width,0,width,height/2))
# #     pg.draw.rect(screen,(79,58,43),(width,height/2,width,height))
# #     for pl in plates:
# #         try:
# #             rat=(platesize/pl)
# #             pg.draw.rect(screen,(200,250,100),(tan(cont)*fdist+1.5*width,height/2-refdist*rat,abs(tan(cont+sepangle)*fdist-tan(cont)*fdist),refdist*rat*2),)
# #             pg.draw.rect(screen,(70,70,70),(tan(cont)*fdist+1.5*width,height/2-refdist*rat,abs(tan(cont+sepangle)*fdist-tan(cont)*fdist)+1,refdist*rat*2),width=1)

# #             cont+=sepangle
# #         except ZeroDivisionError:
# #             pass
# #     print (len(plates))
# #     pg.display.flip()
# #     for e in pg.event.get():
# #         if e.type==pg.QUIT:
# #             run=False
    

# # pg.quit()


# import pygame as pg
# from math import dist,cos,sin,tan,pi,sqrt,atan
# from random import randint

# run= True
# height,width=800,600
# diag=dist((0,0),(height,width))
# screen=pg.display.set_mode((1200,height))
# platesize=20
# class circle:
#     def __init__(self,radius,pos):
#         self.radius=radius
#         self.pos=pos
#     def distance(self,pos,i):
#         return dist(pos,self.pos)-self.radius
#     def draw(self):
#         pg.draw.circle(screen,(65, 146, 232),self.pos,self.radius,)
# class line:
#     def __init__(self,p1,p2,):
#         self.p1=p1
#         self.p2=p2
#         self.slope=(self.p2[1]-self.p1[1])/(self.p2[0]-self.p1[0])
#         print(self.slope,p1[0])

#     def distance(self,pos,i):
#         slope=tan(i.angle)
#         c=self.p1[1]-self.p1[0]*self.slope
#         nc=pos[1]-pos[0]*slope
#         if (self.p1[1]-self.p1[0]*slope-nc)*(self.p2[1]-self.p2[0]*slope-nc)<0:
#             # print(abs((pos[1]-pos[0]*self.slope-c)/sqrt(self.slope**2+1)),self.p1[0],"hit")
#             return abs((pos[1]-pos[0]*self.slope-c)/sqrt(self.slope**2+1))
#         else:
#             return 3300
#     def draw(self):
#         pg.draw.line(screen,(65, 146, 232),self.p1,self.p2)
# class ray:
#     def __init__(self,origin,angle) :
#         self.pos=origin
#         self.angle=angle
#         self.endpoint=(4000,4000)
#     def update(self):
#         self.pos=pg.mouse.get_pos()
#         self.endpoint=(4000,4000)
#         opt=0
#         for i in elements:
#             startpoint=self.pos

#             while True:
#                 r=i.distance(startpoint,self)
#                 startpoint=(startpoint[0]+r*cos(self.angle),startpoint[1]+r*sin(self.angle))
#                 if r<1 or r>diag:
#                     endpoint=startpoint
#                     break 
#             if dist(self.endpoint,self.pos)>dist(endpoint,self.pos):
#                 self.endpoint=endpoint
#             opt+=1
#         plates.append(dist(self.endpoint,self.pos))

#     def draw(self):
#         pg.draw.circle(screen,(200,200,200),self.pos,10)
#         pg.draw.line(screen,(255,255,255),self.pos,self.endpoint,1)

# elements=[line((200,200),(400,250)),
#           line((200,50),(100,400)),
#           line((100,500),(300,550)),
#           line((200,200),(400,500)),
#           line((width,0),(width+1,height)),
          
          
#           ]
          
# for i in range(2):
#     elements.append(circle(randint(20,100),(randint(0,width),randint(0,height))))
# fdist=width/(2*tan(30*pi/180))
# refdist=height/tan(45*pi/180)
# rays=[]
# ang=0
# sepangle=0.5*pi/180
# maxview=pi/3
# itt=round(maxview-ang,2)/sepangle

# for i in range(ang,int(itt)):
#     rays.append(ray((100,100),ang))
#     ang+=sepangle
# while run:
    
#     screen.fill((0,0,0))
#     plates=[]
#     for r in rays:
#         r.update()
#         r.draw()


#     for el in elements:
#         el.draw()
#     cont=-maxview/2
    
#     pg.draw.rect(screen,(135, 206, 235),(width,0,width,height/2))
#     pg.draw.rect(screen,(79,58,43),(width,height/2,width,height))
#     for pl in plates:
#         try:
#             rat=(platesize/pl)
#             pg.draw.rect(screen,(200,250,100),(tan(cont)*fdist+1.5*width,height/2-refdist*rat,abs(tan(cont+sepangle)*fdist-tan(cont)*fdist),refdist*rat*2),)
#             pg.draw.rect(screen,(70,70,70),(tan(cont)*fdist+1.5*width,height/2-refdist*rat,abs(tan(cont+sepangle)*fdist-tan(cont)*fdist)+1,refdist*rat*2),width=1)

#             cont+=sepangle
#         except ZeroDivisionError:
#             pass
#     pg.display.flip()
#     if pg.key.get_pressed()[pg.K_RIGHT]:
        
        
#         for i in rays:
#             i.angle+=1*pi/180
#     if pg.key.get_pressed()[pg.K_LEFT]:
#         for i in rays:
#             i.angle-=1*pi/180
#     # if pg.key.get_pressed()[pg.K_UP]:
        
        
#     #     mid=rays[len(rays)//2].angle
        
#     # if pg.key.get_pressed()[pg.K_DOWN]:
#     #     for i in rays:
#     #         i.angle-=1*pi/180

#     for e in pg.event.get():
#         if e.type==pg.QUIT:
#             run=False
    


# pg.quit()

import pygame as pg
from math import dist,cos,sin,tan,pi,sqrt,atan
from random import randint

run= True
height,width=800,600
diag=dist((0,0),(height,width))
screen=pg.display.set_mode((1200,height))
platesize=20
class circle:
    def __init__(self,radius,pos):
        self.radius=radius
        self.pos=pos
    def distance(self,pos,i):
        return dist(pos,self.pos)-self.radius
    def draw(self):
        pg.draw.circle(screen,(65, 146, 232),self.pos,self.radius,)
class line:
    def __init__(self,p1,p2,):
        self.p1=p1
        self.p2=p2
        self.slope=(self.p2[1]-self.p1[1])/(self.p2[0]-self.p1[0])
        print(self.slope,p1[0])

    def distance(self,pos,i):
        slope=tan(i.angle)
        c=self.p1[1]-self.p1[0]*self.slope
        nc=pos[1]-pos[0]*slope
        if (self.p1[1]-self.p1[0]*slope-nc)*(self.p2[1]-self.p2[0]*slope-nc)<0:
            # print(abs((pos[1]-pos[0]*self.slope-c)/sqrt(self.slope**2+1)),self.p1[0],"hit")
            return abs((pos[1]-pos[0]*self.slope-c)/sqrt(self.slope**2+1))
        else:
            return 3300
    def draw(self):
        pg.draw.line(screen,(65, 146, 232),self.p1,self.p2)
class ray:
    def __init__(self,origin,angle) :
        self.pos=origin
        self.angle=angle
        self.endpoint=(4000,4000)
    def update(self,pos):
        self.pos=pos
        self.endpoint=(4000,4000)
        opt=0
        for i in elements:
            startpoint=self.pos

            while True:
                r=i.distance(startpoint,self)
                startpoint=(startpoint[0]+r*cos(self.angle),startpoint[1]+r*sin(self.angle))
                if r<1 or r>diag:
                    endpoint=startpoint
                    break 
            if dist(self.endpoint,self.pos)>dist(endpoint,self.pos):
                self.endpoint=endpoint
            opt+=1
        plates.append(dist(self.endpoint,self.pos))

    def draw(self):
        pg.draw.circle(screen,(200,200,200),self.pos,10)
        pg.draw.line(screen,(255,255,255),self.pos,self.endpoint,1)

elements=[line((200,200),(400,250)),
          line((200,50),(100,400)),
          line((100,500),(300,550)),
          line((200,200),(400,500)),
          line((width,0),(width+1,height)),
          
          
          ]
          
for i in range(2):
    elements.append(circle(randint(20,50),(randint(0,width),randint(0,height))))
fdist=width/(2*tan(30*pi/180))
refdist=height/tan(45*pi/180)
rays=[]
ang=0
sepangle=0.5*pi/180
maxview=pi/3
itt=round(maxview-ang,2)/sepangle
postion=[100,100]
for i in range(ang,int(itt)):
    rays.append(ray((100,100),ang))
    ang+=sepangle
while run:
    
    screen.fill((0,0,0))
    plates=[]
    for r in rays:
        r.update(postion)
        r.draw()


    for el in elements:
        el.draw()
    cont=-maxview/2
    
    pg.draw.rect(screen,(135, 206, 235),(width,0,width,height/2))
    pg.draw.rect(screen,(79,58,43),(width,height/2,width,height))
    for pl in plates:
        try:
            rat=(platesize/pl)
            pg.draw.rect(screen,(200,250,100),(tan(cont)*fdist+1.5*width,height/2-refdist*rat,abs(tan(cont+sepangle)*fdist-tan(cont)*fdist),refdist*rat*2),)
            pg.draw.rect(screen,(70,70,70),(tan(cont)*fdist+1.5*width,height/2-refdist*rat,abs(tan(cont+sepangle)*fdist-tan(cont)*fdist)+1,refdist*rat*2),width=1)

            cont+=sepangle
        except ZeroDivisionError:
            pass
    pg.display.flip()
    if pg.key.get_pressed()[pg.K_RIGHT]:
        
        
        for i in rays:
            i.angle+=1*pi/180
    if pg.key.get_pressed()[pg.K_LEFT]:
        for i in rays:
            i.angle-=1*pi/180
    if pg.key.get_pressed()[pg.K_UP]:
        
        
        mid=rays[len(rays)//2].angle
        postion[0]+=cos(mid)
        postion[1]+=sin(mid)
        
        
        
    if pg.key.get_pressed()[pg.K_DOWN]:
        mid=rays[len(rays)//2].angle
        postion[0]-=cos(mid)
        postion[1]-=sin(mid)

    for e in pg.event.get():
        if e.type==pg.QUIT:
            run=False
    


pg.quit()