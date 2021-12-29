import cv2
from numpy import *
import time
path = "/Users/admin/Documents/2.jpg"
mainevent=False
r=50

img= cv2.imread(path)
cv2.imshow("image", img)
k=img.copy()

def print_cords(eve,x,y,flags,prams):
    global mainevent,k
    if eve==cv2.EVENT_LBUTTONDOWN:
        mainevent=True
    elif eve==cv2.EVENT_LBUTTONUP:
        mainevent=False
    if mainevent==True:
        l=array([
            k[y-1][x-1],
            k[y-1][x],
            k[y-1][x+1],
            k[y][x-1],
            k[y][x],
            k[y][x+1],
            k[y+1][x-1],
            k[y+1][x],
            k[y+1][x+1],
        ])
        p=average(l, axis=0)
        
        # for i in (y-r,y+r+1):
        #     for j in (x-r,x+r+1) :
        #         k[y][x]=p

        cv2.imshow("image",k)
        print("ho raha hai",time.time())
    print(mainevent)
        
        
        

print(cv2.EVENT_LBUTTONDOWN)

cv2.setMouseCallback('image', print_cords)
cv2.waitKey(0)
cv2.destroyAllWindows()
