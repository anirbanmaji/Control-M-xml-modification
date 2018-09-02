import xml.etree.ElementTree as ET


xmlfile ="test.xml"
tree = ET.parse(xmlfile)
root = tree.getroot()

outcondAdd = []
outcondSub = []

for item in root.findall('./FOLDER/JOB/OUTCOND'):
    if(item.attrib['SIGN'] == '+'):
        outcondAdd.append(item.attrib['NAME'])
    if(item.attrib['SIGN'] == '-'):
        outcondSub.append(item.attrib['NAME'])

balancedCond = set(outcondAdd) and set(outcondSub)
extraAddedCond =  set(outcondSub) - set(outcondAdd)

print(len(outcondAdd))
print(len(set(outcondAdd)))
print()
print(len(outcondSub))
print(len(set(outcondSub)))
print()
print(len(balancedCond))
print(len(set(balancedCond)))
print()
print(len(extraAddedCond))
print(len(set(extraAddedCond)))
print()
    
