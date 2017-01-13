#!/usr/bin/python

import pickle
import sys

import matplotlib.pyplot

sys.path.append("../tools/")
from feature_format import featureFormat

# read in data dictionary, convert to numpy array
data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))
features = ["salary", "bonus"]

outliers = []
for key in data_dict:
    val = data_dict[key]['salary']
    if val == 'NaN':
        continue

    bon = data_dict[key]['bonus']
    if bon == 'NaN':
        continue

    outliers.append((key, int(val), int(bon)))

outliers_final = (sorted(outliers, key=lambda x: x[1], reverse=True)[:10])
for point in outliers_final:
    print(point, )
data_dict.pop(outliers_final[0][0], 0)

data = featureFormat(data_dict, features)

### your code below
from sklearn.linear_model import LinearRegression

reg = LinearRegression()

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter(salary, bonus)

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()
