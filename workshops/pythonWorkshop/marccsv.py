#!/usr/bin/env python

import csv
from pymarc import MARCReader
from os import listdir
from re import search

# change this line to match your folder structure
SRC_DIR = '/home/Zwounds/workshop'

# get a list of all .mrc files in source directory
file_list = filter(lambda x: search('.mrc', x), listdir(SRC_DIR))

csv_out = csv.writer(open('marc_records.csv', 'w'), delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)

for item in file_list:
  fd = file(SRC_DIR + '/' + item, 'r')
  reader = MARCReader(fd)
  for record in reader:
    title = author = date = subject = oclc = publisher = ''

    # title
    if record['245'] is not None:
      title = record['245']['a']
      if record['245']['b'] is not None:
        title = title + " " + record['245']['b']

    # determine author
    if record['100'] is not None:
      author = record['100']['a']
    elif record['110'] is not None:
      author = record['110']['a']
    elif record['700'] is not None:
      author = record['700']['a']
    elif record['710'] is not None:
      author = record['710']['a']

    # date
    if record['260'] is not None:
      date = record['260']['c']

    # subject
    if record['650'] is not None:
      subject = record['650']['a']

    # oclc number
    if record['035'] is not None:
      if len(record.get_fields('035')[0].get_subfields('a')) > 0:
        oclc = record['035']['a'].replace('(OCoLC)', '')

    # publisher
    if record['260'] is not None:
      publisher = record['260']['b']

    csv_out.writerow([title, author, date, subject, oclc, publisher])
  fd.close()