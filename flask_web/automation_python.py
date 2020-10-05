import pyautogui as pa
import time as t                                                                                                                                                  
import numpy as np
import PIL as pl
def ss():
                                                                                                                                                       
    while True:
        a=pl.ImageGrab.grab().convert('L')
        img=a.load()
        t1=t.time()
        for x in range(100,250):
            for y in range(370,470):                                                                                                                   
                if img[x,y]<55:            
                    pa.keyDown('space')
                    break
            if img[x,y]<300:        
                break                                                                                                                                                                
        t2=t.time()
                                                                                                     
    print(t2-t1)                   
ss()                                                                  