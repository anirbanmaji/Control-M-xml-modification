import xml.etree.ElementTree as ET
import re
import commands as cm

def putCommand(src,dest):
    xmlfile ="new.xml"
    tree = ET.parse(xmlfile)
    root = tree.getroot()
    for item in root.findall('./FOLDER/JOB'):
        jobName = item.attrib['JOBNAME']
        action = re.findall(r'(FW|GBT|MSEQ|CD|EBT)$', jobName)#change
        regex = r"(?<=(^BIHAU_T2_BH"+src+"_"+dest+"_))(.*?)(?=(_(FW|GBT|MSEQ|CD|EBT))$)"
        fileExt = re.findall(regex, jobName)#change
        if len(action)!=0 and len(fileExt)!=0:
            action = action[0]
            fileExt = fileExt[0][1]

        #change if-else block
        if action == 'FW':
            sameActionCommand = cm.FW
        elif action == 'GBT':
            sameActionCommand = cm.GBT
        elif action == 'MSEQ':
            sameActionCommand = cm.MSEQ
        elif action == 'CD':
            sameActionCommand = cm.CD
        elif action == 'EBT':
            sameActionCommand = cm.EBT
        else:
            sameActionCommand = ['']


        commandline = 'hostname'
        for i in cm.FW:
            #check the index of the FW command for the current job file and use the same index for this job
            if fileExt in i.upper():
                cmdIndex = cm.FW.index(i)
                print(fileExt," ",cmdIndex)
                commandline = sameActionCommand[cmdIndex]
                
        item.set('CMDLINE', commandline)

    tree.write(src+"_"+dest+".xml")

if __name__ == "__main__":
    putCommand("GADEN","TALLYMAN")
