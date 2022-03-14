import xml.etree.ElementTree as ET
#get the XML file data
stream = open('sample.xml','r')

#parse the data into an ElementTree object
xml = ET.parse(stream)

#get the 'root' Element object from the ElementTree
root = xml.getroot()

#Iterate through each child of the root Element
for e in root:
    #print the stringified version of the element
    print(ET.tostring(e))
    print("")

    #print the 'Id' attribute of the Element object
    print(e.get("Id"))

