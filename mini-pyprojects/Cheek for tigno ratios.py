l=10

c=0

for h in range(l):

	for b in range(h):		for p in range(h):

			if (h**2)==(b**2)+(p**2):

				print(b,p,h)

				hl.append(h)

				pl.append(p)

				b.append(b)

				

				c+=1

			elif (h**2)<(b**2)+(p**2):

				break

print(c)

print(lb,lh,la)
