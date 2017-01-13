#!/usr/bin/python

import matplotlib.pyplot as plt
from class_vis import prettyPicture
from prep_terrain_data import makeTerrainData

features_train, labels_train, features_test, labels_test = makeTerrainData()

### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii] == 0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii] == 0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii] == 1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii] == 1]

#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color="b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color="r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary


from sklearn import ensemble, neighbors

clf = neighbors.KNeighborsClassifier(n_neighbors=15,
                                     weights='distance')
clf.fit(features_train, labels_train)
prettyPicture(clf, features_test, labels_test, "K Nearest Neighbour")


clf = ensemble.RandomForestClassifier(n_estimators=15,
                                      criterion='entropy',
                                      max_features='auto',
                                      min_samples_split=25)
clf.fit(features_train, labels_train)
prettyPicture(clf, features_test, labels_test, "Random Forest")


clf = ensemble.AdaBoostClassifier(n_estimators=45,
                                  learning_rate=0.7,
                                  algorithm="SAMME.R")
clf.fit(features_train, labels_train)
prettyPicture(clf, features_test, labels_test, "Ada boost")
