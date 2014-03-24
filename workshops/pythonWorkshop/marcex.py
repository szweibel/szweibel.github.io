import pymarc

stats = {}

def tally(record):
    # counts how many records have each field
    for field in record.fields:
        stats[field.tag] = stats.get(field.tag, 0) + 1

records = 0
marc_file = file('/home/Zwounds/workshop/marcs.mrc')

for marc_record in pymarc.MARCReader(marc_file):
    records += 1
    tally(marc_record)

for item in stats:
    print item," : ", stats[item]

print records, " total records"