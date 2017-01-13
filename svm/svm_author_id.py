#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time

from sklearn.metrics import accuracy_score
from sklearn.svm import SVC

sys.path.append("../tools/")
from email_preprocess import preprocess

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#########################################################
### your code goes here ###

# reducing test dataset to 1%
# features_train = features_train[:int(len(features_train) / 100)]
# labels_train = labels_train[:int(len(labels_train) / 100)]

# print("\n# svm linear")
# initial_time = time.time()
# clf = SVC(kernel='linear')
# clf.fit(features_train, labels_train)
# pred = clf.predict(features_test)
# total_time_svm = time.time() - initial_time
# accuracy = accuracy_score(labels_test, pred)
#
# print('Accuracy = ' + str(accuracy) + "\nTime taken = ")
# print(total_time_svm)

print("\n# svm (kernel='rbf',C=10000)")

t0 = time()
clf = SVC(kernel='rbf', C=10000)
clf.fit(features_train, labels_train)
print("training time:", round(time() - t0, 3), "s")

t0 = time()
pred = clf.predict(features_test)
print("prediction time:", round(time() - t0, 3), "s")
print('Accuracy : ', accuracy_score(labels_test, pred))

exit()

count = 0
pred = clf.predict(features_test)
for i in range(len(pred)):
    if pred[i] == 1:
        count += 1
print(count)
#########################################################
