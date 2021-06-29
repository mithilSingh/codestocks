from time import sleep,time
x=1
y=0
t=time()
while True:
    
    y+=1/x
    x+=2
    y-=1/x
    x+=2
    print(y*4)
    if round(y*4,6)==3.14159:
        print(y,x,time()-t)
        break
'''
1,
32

x=2y+4

x=by + c

6=b1+c
8=b2+c

b+c+6=2b+c+8

6=b+8
b=-2

6,1
8,2
4-1/64-36
3
'''