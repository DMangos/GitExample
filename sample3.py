import xmltodict
#get the XML file data
stream = open('sample.xml','r')

#parse the data into an 'OrderedDict'
xml = xmltodict.parse(stream.read())



for e in xml:  
    print(e)