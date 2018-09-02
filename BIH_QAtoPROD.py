'''works fine'''
import xml.etree.ElementTree as ET
from correctFileName import correctFileName

def migrateBIH_QAtoPROD(qaXML):
    filedata = None
    with open(qaXML, 'r') as file:
        filedata = file.read()

    filedata = filedata.replace('DCMAU01','PCMAU01')
    filedata = filedata.replace('dsadm','pdsadmin')
    filedata = filedata.replace('BIHPD02D','BIHPD01P')

    finalFilename = qaXML[0:-4]+".PROD.xml"
    
    modFile = open(finalFilename,"w")
    newfile = modFile.write(filedata)
    file.close()
    modFile.close()

    tree = ET.parse(finalFilename)
    root = tree.getroot()
    for item in root.findall('./FOLDER'):
        item.set('FOLDER_ORDER_METHOD', "UD_0705")
    for item in root.findall('./FOLDER/JOB'):
        item.attrib['APPLICATION'].replace('_P', '_P1')
        if (item.attrib['JOBNAME'][-2:] == ('FW' or 'AR')):
            item.attrib['NODEID'] = 'aup4094l.unix.anz'
        else:
            item.attrib['NODEID'] = 'aup4094l.unix.anz'
            
    correctFileName(finalFilename).write(finalFilename)
    print('Add schedule and calender')
    

migrateBIH_QAtoPROD('test.xml')
