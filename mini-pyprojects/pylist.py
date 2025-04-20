def get(la):
	print(la)
	
def clist(a,l):	
	b=1
	c1=1
	if a[0]=='[':
		while True:
			try:
				if a[b]==',':
					try:
						l.append(int(a[c1:b]))
					except:
						l.append(a[c1:b])						
					b+=1
					c1=b
					print(a[c1:b-1])
				elif a[b]!=','and a[b]!=']':
					b+=1
				elif a[b]==']':
					try:
						l.append(int(a[c1:b]))
					except:
						l.append(a[c1:b])
					break
			except:					
					print('prob')
					break					
	elif a[0]!='[':
		print('listenteryerror')
	