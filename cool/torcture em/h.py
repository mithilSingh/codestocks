import cv2 
import numpy as np
import pygame as pg

run=True
vid = cv2.VideoCapture(0) 
face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
while(True): 
	
	ret, frame = vid.read() 
	frame=cv2.flip(frame,180)

	greys=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	faces=face_cascade.detectMultiScale(greys,1.25,5)
	try:
		for (x,y,w,h) in faces:
			cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),2)
	except:
		print("yo")
	cv2.imshow('frame', frame) 
	
	if cv2.waitKey(1) & 0xFF == ord('q'): 
		break

vid.release() 
cv2.destroyAllWindows() 

