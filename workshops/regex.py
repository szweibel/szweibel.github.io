import re
import sys

def csv_import(which):
    # Open a CSV
    lines = [line.strip() for line in open(which)]
    for x in lines:
        match=re.search(r'[a]',x)
        if match: print x


csv_import(sys.argv[1])

