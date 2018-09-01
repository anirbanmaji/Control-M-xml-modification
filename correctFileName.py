import xml.etree.ElementTree as ET
xmlfile ="test.xml"
tree = ET.parse(xmlfile)
root = tree.getroot()
numOfChanges = 0
for item in root.findall('./FOLDER/JOB'):
    if(item.attrib['MEMNAME'] != item.attrib['JOBNAME']):
        item.attrib['MEMNAME'] = item.attrib['JOBNAME']
        numOfChanges += 1

print("number of changes: "+str(numOfChanges))
tree.write("test1.xml")
