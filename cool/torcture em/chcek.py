# import cv2
# import numpy as np
# vid=cv2.VideoCapture(0)
# upper_bound=np.array([80, 40, 250])
# lower_bound=np.array([0, 0, 190])
# while True:
#     red,frame=vid.read()
#     frame=cv2.flip(frame,180)

#     hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
#     mask=cv2.inRange(hsv,lower_bound,upper_bound)
#     bw=cv2.bitwise_and(frame,frame,mask=mask)
#     mask=cv2.resize(mask,(0,0),fx=0.07,fy=0.07)
#     print(mask.shape)
#     for i in range(mask.shape[0]):
#         for j in range(mask.shape[1]):
#             if mask[i][j]==255:
#                 print(i,j)

#     cv2.imshow("frame",bw)

#     if cv2.waitKey(1) & 0xFF == ord('q'): 
#         break 
# vid.release() 
# cv2.destroyAllWindows() 
# a={"q":2,
#    "e":3,
#    "r":4}
# text=open("constants.txt","w")
# text.write(str(a))
# text.close()
# text=open("constants.txt","r")


# print(text.read().split(":"))
# text.close()
a="[100,100]"
pr)
