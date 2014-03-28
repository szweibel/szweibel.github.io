import re
import sys

def csv_import(which):
    # Open a CSV
    lines = [line.strip() for line in open(which)]
    re1='.*?' # Non-greedy match on filler
    re2='(\\s+)'  # White Space 1

    rg = re.compile(re1+re2,re.IGNORECASE|re.DOTALL)
    for x in lines:
        # searchObj = re.search( r'(a*) (b.*) (.*)', x)
        searchObj = rg.search(x)

        if searchObj:
           print "searchObj.group() :\n", searchObj.group()
           # print "searchObj.group(0) : \n", searchObj.group(0)
           # print "searchObj.group(1) : \n", searchObj.group(1)
           # print "searchObj.group(2) : \n", searchObj.group(2)
        else:
           print "Nothing found!!"


csv_import(sys.argv[1])

