import xml.etree.ElementTree as ET

def correctFileName(xmlfile):
    tree = ET.parse(xmlfile)
    root = tree.getroot()
    numOfChanges = 0
    for item in root.findall('./FOLDER/JOB'):
        try:
            if(item.attrib['MEMNAME'] != item.attrib['JOBNAME']):
                item.attrib['MEMNAME'] = item.attrib['JOBNAME']
                numOfChanges += 1
        except:
            item.set('MEMNAME', item.attrib['JOBNAME'])

    print("number of changes: "+str(numOfChanges))
    #modifiedFile = xmlfile+"FileNameCorrected.xml"
    #tree.write(modifiedFile)
    return tree

#correctFileName("test.xml")
