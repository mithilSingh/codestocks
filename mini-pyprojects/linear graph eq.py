x1=float(input("first x cordinate"))
y1=float(input("first y cordinate"))
x2=float(input("second x cordinate"))
y2=float(input("second y cordinate"))

m=(x2-x1)/(y2-y1)
m1=(x2-x1)
m2=(y2-y1)
z=x1-y1*(m)
z2=str(z.as_integer_ratio()[0])+"/"+str(z.as_integer_ratio()[1])
if z==0.0 and m==1.0:
    print(f"x=y")
elif z==0.0:
    print(f"x=({m})y")
elif m==1:
    print(f"x=1y+({z2})")
else:
    print(f"x=({m1}/{m2})y+({z2})")


