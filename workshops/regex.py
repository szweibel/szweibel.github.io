import re
import sys

def csv_import(which):
    # Open a CSV
    lines = [line.strip() for line in open(which)]
    for x in lines:
        searchObj = re.search( r'(a*) (b.*) (.*)', x)

        if searchObj:
           print "searchObj.group() :\n", searchObj.group()
           print "searchObj.group(0) : \n", searchObj.group(0)
           print "searchObj.group(1) : \n", searchObj.group(1)
           print "searchObj.group(2) : \n", searchObj.group(2)
        else:
           print "Nothing found!!"

csv_import(sys.argv[1])

