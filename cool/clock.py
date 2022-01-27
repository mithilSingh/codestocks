import time 
from turtle import*
t=Turtle()

h=Turtle()
p=Turtle()
h.penup()
t.color('white')
h.color('white')
p.color('white')
bgcolor('black')

p.speed(50)
h.speed(50)
p.penup()
t.speed(50)
t.shapesize(0.00001,0.000001,1)
f=Turtle()
f.color('white')
f.shapesize(0.000001,0.000001,1)
f.penup()
f.goto(-30,-100)
t.circle(100)
t.color('red')
t.penup()
t.left(90)
t.fd(100)
f.pensize(200)
t.left(180)
t.shapesize(0.01,10,1)
h.shapesize(0.00001,0.000001,1)
p.shapesize(0.00001,0.000001,1)
h.left(90)
h.forward(100)
h.left(180)
h.shapesize(0.01,8,3)
p.left(90)
p.forward(100)
p.left(180)
p.shapesize(0.01,5,4)
t.pendown()
s=time.localtime()
sec=s.tm_sec
t.right(sec*6)
sp=sec
min=s.tm_min
mmin=min
h.right(mmin*6)
count=sec
spp=sp
hr=s.tm_hour
if hr>12:
    hrr=hr-12
elif hr<=12:
    hrr=hr
hrr=hr
count2=0
p.right(hrr*30+mmin*0.5)
while True :
    if spp==60:
        spp=0
    kio=str(hrr)+':'+str(mmin)+':'+str(spp)
    f.write(kio)
    t.left(-6)
    time.sleep(1)
    f.undo()
    spp+=1
    if count %60==0 and count!=0:
        h.left(-6)
        mmin+=1
        count2+=1
        p.right(0.5)
    count+=1  
screen=t.getscreen()
screen.title("Clock")
screen.mainloop()
