import tablib
import csv
import sys
import re

def csv_import(which):
    # Open a CSV
    try:
        csvReader = csv.reader(open(which, 'rU'), delimiter=',')
    except Exception, e:
        raise e
    headline = []
    # Get the CSV's headers
    for row in csvReader:
        header = str(row).rsplit(',')
        for word in header:
            newstr = word.replace("[", "")
            newstr = newstr.replace("]", "")
            newstr = newstr.replace("\\", "")
            newstr = newstr.replace("'", "")
            newstr = newstr.strip()
            headline.append(newstr)
        break
    # create a tablib dataset to put my data into
    data = tablib.Dataset()
    # assign my headers
    data.headers = headline
    # If there are rows without data in a cell, add 'None'
    for row in csvReader:
        if len(row) != len(data.headers):
            difference = len(data.headers) - len(row)
            a = 0
            while a < difference:
                row.append('None')
                a += 1
        data.append(row)




csv_import(sys.argv[1])