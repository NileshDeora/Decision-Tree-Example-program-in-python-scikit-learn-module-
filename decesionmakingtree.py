from sklearn import tree
#hight weight and shoe size
x  = [ [143,54,65] ,[166,56,33],[236,54,75],[245,34,65],[234,66,77],[144,45,76],[344,56,33],[343,34,76],[123,56,33],[345,65,23],
    [463,35,56]  ]
y=['male','female','male','female','female',',male','male','female','female','male','male']
clf = tree.DecisionTreeClassifier()
clf =clf.fit(x,y)
prediction=clf.predict([[123,43,65]])
print(prediction)
