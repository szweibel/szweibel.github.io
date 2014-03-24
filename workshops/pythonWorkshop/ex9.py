import pymarc

marc_file = file('/home/Zwounds/workshop/marcs.mrc')

loaded_file = pymarc.MARCReader(marc_file)

for record in loaded_file:
    for record in loaded_file:
        title = record['245']['a']
        print title
        break