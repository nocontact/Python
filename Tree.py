# from sklearn import tree
# features = [[140,1],[130,1],[150,0],[170,0]]
# labels = [0,0,1,1]
# clf = tree.DecisionTreeClassifier()
# clf = clf.fit(features,labels)
# print (clf.predict([[160,0]]))

from sklearn.datasets import load_iris
iris = load_iris()
print (iris.feature_names)
print (iris.target_names)
