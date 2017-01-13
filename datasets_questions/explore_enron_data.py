#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))

print("\nNo of items in dataset : %d" % len(enron_data))

for key in enron_data:
    features = len(enron_data[key])
    print("Features count : %d" % features)
    break

count_poi = 0
count_sal = 0
count_email = 0
count_pay = 0
count_poi_pay = 0

for key in enron_data:
    if enron_data[key]['poi']:
        count_poi += 1
        # print(key)

    # if key == 'SKILLING JEFFREY K' or key == 'LAY KENNETH L' or key == 'FASTOW ANDREW S':
    #     print(key +" : "+ str(enron_data[key]['total_payments']))

    if type(enron_data[key]['salary']) is int:
        count_sal += 1

    if enron_data[key]['email_address'] != 'NaN':
        count_email += 1

    if type(enron_data[key]['total_payments']) is not int:
        # print(enron_data[key]['total_payments'])
        count_pay += 1

    if type(enron_data[key]['total_payments']) is not int and enron_data[key]['poi']:
        # print(enron_data[key]['total_payments'])
        count_poi_pay += 1


print("POI in dataset : %d" % count_poi)
print("Quantified salary in dataset : %d" % count_sal)
print("Known email addresses in dataset : %d" % count_email)
print("total payments as NaN in dataset : %d" % count_pay)
print("POI with total payments as NaN in dataset : %d" % count_poi_pay)
