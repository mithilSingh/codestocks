import cv2
from time import sleep 
import numpy as np
import pyfirmata2 as pyf
from math import atan,pi,sqrt,cos,sin,tan
run=True
vid = cv2.VideoCapture(0) 
data=open("constants.txt","r")
vals=data.read()[1:-1].split(",")

print(vals[0].split(":")[1][1:-1].split("|"))
xoffset=63#(round(float(vals[0].split(":")[1][2:-1].split("|")[0]))+round(float(vals[1].split(":")[1][2:-1].split("|")[0])))/2
yoffset=68#(round(float(vals[1].split(":")[1][2:-1].split("|")[1]))+round(float(vals[2].split(":")[1][2:-1].split("|")[1])))/2
xmax=140#(round(float(vals[2].split(":")[1][2:-1].split("|")[0]))+round(float(vals[3].split(":")[1][2:-1].split("|")[0])))/2
ymax=116#(round(float(vals[3].split(":")[1][2:-1].split("|")[1]))+round(float(vals[0].split(":")[1][2:-1].split("|")[1])))/2

# h,v=90,90
port='/dev/cu.usbmodem14101'
height=600
width=602
topx,topy=None,None
run=True
sidelen=10
upper_bound=np.array([80, 40, 250])
lower_bound=np.array([0, 0, 190])
# matrix=np.zeros((width//sidelen,height//sidelen))
coordinaes=[]
board=pyf.Arduino(port)

board.digital[9].mode=pyf.SERVO
board.digital[10].mode=pyf.SERVO
board.digital[9].write(0)
board.digital[10].write(0)
board.digital[9].write(90)
board.digital[10].write(90)

board.digital[9].write(90)
board.digital[10].write(90)
sleep(2)
vid = cv2.VideoCapture(0) 
face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


def angle(x,y,):
    
    hrange=xmax-xoffset
    vrange=ymax-yoffset
    xdis,ydis=640/tan(hrange*pi/360),360/tan(vrange*pi/360)
    x,y=(x-640),y-360
    print("--->",atan(x/xdis)*180/pi)
    return (((hrange)/2-atan(x/xdis)*180/pi+xoffset),((ymax+yoffset)/2-atan(y/ydis)*180/pi))




def calibrate(manual=True):
    h,v=90,90

    if manual:
        area=[
            [(i,j) for i in range(3) for j in range(3)],
            [(i,j) for i in range(47,50,1) for j in range(3)],
            [(i,j) for i in range(47,50,1) for j in range(87,90,1)],
            [(i,j) for i in range(3) for j in range(87,90,1)],
        ]
        recod={}
        cont=0
        run=True
        print(area)
        while run:
            red,frame=vid.read()
            frame=cv2.flip(frame,180)

            hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
            mask=cv2.inRange(hsv,lower_bound,upper_bound)
            # bw=cv2.bitwise_and(frame,frame,mask=mask)
            mask=cv2.resize(mask,(0,0),fx=0.07,fy=0.07)
            for i in range(mask.shape[0]):
                for j in range(mask.shape[1]):
                    if mask[i][j]==255 :
                        if (i,j) in area[cont]:
                            recod[cont]=(str(h)+"|"+str(v))
                            cont+=1
                            h,v=90,90
                            print("------>",cont)
            if cont>3:
                break
            cv2.imshow("frame",mask)


            if cv2.waitKey(1) & 0xFF == ord('q'): 
                break
            elif cv2.waitKey(1) ==2:
                h-=1
            elif cv2.waitKey(1) ==3:
                h+=1
            elif cv2.waitKey(1) ==1:
                v-=1
            elif cv2.waitKey(1) ==0:
                v+=1 
            board.digital[9].write(v)
            board.digital[10].write(h) 
    else:
        #algorithm 1
        # area=[
        #     [(i,j) for i in range(3) for j in range(3)],
        #     [(i,j) for i in range(47,50,1) for j in range(3)],
        #     [(i,j) for i in range(47,50,1) for j in range(87,90,1)],
        #     [(i,j) for i in range(3) for j in range(87,90,1)],
        # ]
        # recod={}
        # cont=0
        # run=True
        # print(area)
        # for v in range(67,150,1):
        #     for h in range(50,150,1):
        #         red,frame=vid.read()
        #         frame=cv2.flip(frame,180)

        #         hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        #         mask=cv2.inRange(hsv,lower_bound,upper_bound)
        #         # bw=cv2.bitwise_and(frame,frame,mask=mask)
        #         mask=cv2.resize(mask,(0,0),fx=0.07,fy=0.07)
        #         for i in range(mask.shape[0]):
        #             for j in range(mask.shape[1]):
        #                 if mask[i][j]==255 :
        #                     if (i,j) in area[0]:
        #                         recod["upperleft"]=(h,v)
        #                         print("ul")
        #                     elif (i,j) in area[1]:
        #                         recod["bottomleft"]=(h,v)
        #                         print("bl")
        #                     elif (i,j) in area[2]:
        #                         recod["bottomright"]=(h,v)
        #                         print("br")
        #                     elif (i,j) in area[3]:
        #                         recod["upperright"]=(h,v)
        #                         print("ur")
                
        #         cv2.imshow("frame",mask)


        #         if cv2.waitKey(1) & 0xFF == ord('q'): 
        #             break
                
        #         board.digital[9].write(v)
        #         board.digital[10].write(h) 

        #algorithm 2
        points=[
            (2,2),
            (47,2),
            (48,88),
            (2,88),

        ]
        recod={}
        cont=0
        run=True
        while run:
            red,frame=vid.read()
            frame=cv2.flip(frame,180)

            hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
            mask=cv2.inRange(hsv,lower_bound,upper_bound)
            mask=cv2.resize(mask,(0,0),fx=0.07,fy=0.07)
            for i in range(mask.shape[0]):
                if not run:
                    break
                for j in range(mask.shape[1]):
                    if mask[i][j]==255 :
                        cu=False
                        sy=points[0][0]-i
                        sx=j-points[0][1]
                        if -2<=sy<=2 and -2<=sx<=2:
                            points.pop(0)
                            cont+=1
                            recod[cont]=(h,v)
                            h,v=90,90
                            print("recod")
                            if cont>=4:
                                run=False
                                break
                            break
                            
                        
                        try:
                            theta=abs(atan(sy/sx))
                            if sx>0:
                                h-=1*cos(theta)
                            elif sx<0:
                                h+=1*cos(theta)

                            if sy>0:
                                v-=1*sin(theta)
                            elif sy<0:
                                v+=1*sin(theta)
                        except ZeroDivisionError:
                            pass
            cv2.imshow("frame",mask)


            if cv2.waitKey(1) & 0xFF == ord('q'): 
                break
            
            board.digital[9].write(v)
            board.digital[10].write(h) 
            sleep(0.035)
                    
                    


    file=open("constants.txt","w")
    file.write(str(recod))
    file.close()

    
# calibrate(manual=False)
while(True): 
    ret, frame = vid.read() 

    
    greys=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(greys,1.25,5)

    try:
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),2)
        xp,yp=angle(faces[0][0]+faces[0][2]/2,faces[0][1]+faces[0][3]/2)
        print(xp,yp)
        
        board.digital[9].write(yp)
        board.digital[10].write(xp)
        sleep(0.015)
    except:
        print("po")
    # if cv2.waitKey(1) & 0xFF == ord('q'): 
    #     break
    # elif cv2.waitKey(1) ==2:
    #     h-=1
    # elif cv2.waitKey(1) ==3:
    #     h+=1
    # elif cv2.waitKey(1) ==1:
    #     v-=1
    # elif cv2.waitKey(1) ==0:
    #     v+=1
    # board.digital[9].write(v)
    # board.digital[10].write(h) 
    frame=cv2.flip(frame,180)

    cv2.imshow('frame', frame)
    # if h>180:
    #     h=180
    # elif h<0:
    #     h=0
    # if v>180:
    #     v=180
    # elif v>180:
    #     v=180  
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break 
vid.release() 
cv2.destroyAllWindows() 

#v 50.4
# h 90
