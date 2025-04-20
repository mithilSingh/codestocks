a=int(input("enter the number: "))
l=""
if a==1:
    l=1
b=2
while a!=1:
    if a%b==0:
        l=l+str(b)+('x')
        a=a/b
    
    elif  a%b!=0:
        b=b+1

print(l)