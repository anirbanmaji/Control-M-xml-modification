import xml.etree.ElementTree as ET
import re
import commands as cm

xmlfile ="new.xml"
tree = ET.parse(xmlfile)
root = tree.getroot()
for item in root.findall('./FOLDER/JOB'):
    jobName = item.attrib['JOBNAME']
    print(jobName)
    action = re.findall(r'(AR|FW|DLT|CP|RG|LD|TV|DV)$', jobName)#change
    fileExt = re.findall(r'(?<=(^BIHJP_T2_EWMDAZ_EPS_RS_))(.*?)(?=(_(AR|FW|DLT|CP|RG|LD|TV|DV))$)', jobName)#change
    #   (?<=(JOBNAME="BIHJP_T2_EWMDAZ_EPS_RS_))(.*?)(?=(_(AR|FW|DLT|CP|RG|LD|TV|DV)" JUL))
    print(action)
    if len(action)!=0 and len(fileExt)!=0:
        action = action[0]
        fileExt = fileExt[0][1]
        #print(action,", ",fileExt)

    #change if-else block
    if action == 'FW':
        sameActionCommand = cm.FW
    elif action == 'DLT':
        sameActionCommand = cm.DLT
    elif action == 'CP':
        sameActionCommand = cm.CP
    elif action =='RG':
        sameActionCommand = cm.RG
    elif action =='LD':
        sameActionCommand = cm.LD
    elif action =='TV':
        sameActionCommand = cm.TV
    elif action =='DV':
        sameActionCommand = cm.DV
    elif action =='AR':
        sameActionCommand = cm.AR
    else:
        sameActionCommand = ['']


    commandline = 'hostname'
    for cmd in sameActionCommand:
        if str(fileExt) in cmd:
            commandline = cmd
            #print(fileExt,', ', action)
    #print(commandline)
            
    item.set('CMDLINE', commandline)

tree.write('out.xml')
