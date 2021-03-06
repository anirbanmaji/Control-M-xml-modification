'''works fine'''
import xml.etree.ElementTree as ET
from correctFileName import correctFileName

def migrateBIH_SITtoQA(sitXML):
    filedata = None
    with open(sitXML, 'r') as file:
        filedata = file.read()

    filedata = filedata.replace('DCMAU02','DCMAU01')
    filedata = filedata.replace('_T2','_P')
    filedata = filedata.replace('BIHPD01S','BIHPD02D')

    finalFilename = sitXML[0:-4]+".QA.xml"
    
    modFile = open(finalFilename,"w")
    newfile = modFile.write(filedata)
    file.close()
    modFile.close()

    tree = ET.parse(finalFilename)
    root = tree.getroot()
    for item in root.findall('./FOLDER/JOB'):
        item.attrib['APPLICATION'].replace('_P', '_P1')
        if (item.attrib['JOBNAME'][-2:] == ('FW' or 'AR')):
            item.attrib['NODEID'] = 'auq4094l.unix.anz'
        else:
            item.attrib['NODEID'] = 'auq4094l.unix.anz'
    
    correctFileName(finalFilename).write(finalFilename)
    

migrateBIH_SITtoQA('test.SIT.xml')
