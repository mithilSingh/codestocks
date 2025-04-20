import random
l={}
con=0
cp=0
ask=int(input('enter no of round of tosses u want to have'))
for i in range(ask):
	a=''
	v='z'
	t='b'
	c=1
	while True:
		r =random .choice(['Heads','Tails'])
		t=v
		v=a
		a=r	
		if a==v and v==t:
			print(c)
			l[c]=c
			break
		else:
			c=c+1
	cp+=1
	con=con+c
	print(cp,")",v,a,t)
print (l)
num=ask
while num!=3:
	if num in l:
		print ('the higest number of tosses in this case were',num)
		break
	else :
		num=num-1
print ('avrege tosses required are',con/ask,', aprox=',round(con/ask))

