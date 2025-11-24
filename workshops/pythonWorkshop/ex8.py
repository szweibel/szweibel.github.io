import pymarc

marc_file = file('/home/Zwounds/workshop/marcs.mrc')

loaded_file = pymarc.MARCReader(marc_file)

for record in loaded_file:
    title = record['245']['a']
    print title


#for record in loaded_file:
#    if record['650'] is not None:
#        subject_location = record['650']['z']
#        print subject_location