# codestocks
from sklearn import svm,datasets
import numpy as np 
import matplotlib.pyplot as plt 
import random as r
di=datasets.load_digits()
x,y=di.data[0:len(di.data)*8//10],di.target[0:len(di.target)*8//10]
c=svm.SVC()
c.fit(x,y)


e=-356
#e1=lambda : (r.randint(1,360))
#e=e1()
plt.imshow(di.images[e])
plt.xlabel((f"it looks like {str(c.predict([di.data[e]]))[1:-1]} to me"))
plt.show()
#print(f"I am {c.score(x,y)*100} % accurate ")
