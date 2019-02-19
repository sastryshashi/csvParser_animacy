'''
Author: Sastry, Shashidhar
Date created: February 16, 2019
Last change made: February 17, 2019
Version: Python 3.4.4
'''

import csv
from ast import literal_eval
import pprint

pp = pprint.PrettyPrinter(indent=4)

'''
Retrieve un-scored items
'''
print ("*"*75)
print ("\tThis program displays items that could not be scored".upper())
print ("*"*75)
remainder_dict = dict()

with open ('unscored.csv') as csv_file:
    csv_reader = csv.reader (csv_file, delimiter=';')
    for row in csv_reader:
        remainder_dict [int(row[0])] = literal_eval(row[1])

while (True):
    id_number = input ("Enter id: ")
    try:
        pp.pprint (remainder_dict[int(id_number)])
    except:
        print ("Incorrect id or id not found")
    print('\n')
