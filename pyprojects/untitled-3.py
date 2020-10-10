l=int(input("enter the length"))
b=int(input("enter the breath"))
a=b*l
li="the no of sqare which can be formed within the given rectangle are ->"
count=1
while True:
    while True:
        if a-count**2>=0:
            count+=1
        elif a-count**2<0:
            count=count-1
            li=li+str(count*count)+","
            rel=a-count**2
            break
    
    if rel>0:
        count=1
        a=rel
    elif rel<=0:
        
        break
    
print(li)   
