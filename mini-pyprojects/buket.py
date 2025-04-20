from sklearn import tree
a=[["apple"],["orange"],["aaple"],["orrange"],["applee"],["orangge"]]
b=[0,1,0,1,0,1]#0 is for apple and #1 is for orange
c=tree.DecisionTreeClassifier()
c.fit(a,b)
print(c.predict([["orange"]]))
