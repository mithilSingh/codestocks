l=['h','a','p','y']
li=[]
lop=''
for i in tqdm(range(1)):
    for a in l:
	    lop=a
	    print(lop)
	    li.append(lop)
	    for b in l:
		    lop=a+b
		    print(lop)
		    li.append(lop)
		    for c in l:
			    lop=a+b+c
			    print(lop)
			    li.append(lop)
			    for d in l:
				    lop=a+b+c+d
				    print(lop)
				    li.append(lop)
				    for e in l:
					    lop=a+b+c+d+e
					    print(lop)
					    li.append(lop)
					    for f in l:
						    lop=a+b+c+d+e+f
						    print(lop)

print(li)