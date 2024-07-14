import cv2 
import numpy as np
import pyfirmata2 as pyf
from math import atan,pi,sqrt
from time import sleep
run=True
vid = cv2.VideoCapture(0) 
face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

port='/dev/cu.usbmodem14101'
height=600
width=600
topx,topy=None,None
run=True
sidelen=10
# matrix=np.zeros((width//sidelen,height//sidelen))
coordinaes=[]
board=pyf.Arduino(port)

board.digital[9].mode=pyf.SERVO
board.digital[10].mode=pyf.SERVO
board.digital[9].write(0)
board.digital[10].write(0)
board.digital[9].write(90)
board.digital[10].write(90)


def angle(x,y):
    distan=5
    x,y=x-30,y-30
    d=sqrt(distan**2+x**2)
    return (atan(x/distan)*180/pi,atan(y/d)*180/pi)

alp=0
lis=[(0,0),(0,120),(120,120),(120,0)]
while(True): 

    ret, frame = vid.read() 
    frame=cv2.flip(frame,180)

    greys=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(greys,1.25,5)
    
    print(frame.shape)
    try:
        xp,yp=angle(faces[0][0]+faces[0][2]/2,faces[0][1]+faces[0][3]/2)
        # board.digital[9].write(int(yp)+80)
        # board.digital[10].write(int(xp)+80)
        # print(xp,yp)
        # print(faces[0][0]+faces[0][2]/2,faces[0][1]+faces[0][3]/2)
    
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),2)
    except:
        print("yo")
    
    
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('a'):
        alp=alp%4
        board.digital[9].write(lis[alp][1])
        board.digital[10].write(lis[alp][0])
        alp+=1
        print("ko")

    
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break

vid.release() 
cv2.destroyAllWindows() 

