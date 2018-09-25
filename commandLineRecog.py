import openpyxl
from getValuesFromHeader import getDataofHeader
from RSDS_Flow import createSingleFlowTemplate

xlFile = 'C:/Users/AnirbanMaji/Desktop/Control M RSDS jobs/RSDS_SITControl M_requirement_sheet_MYTELL.xlsm'
cmdHeader = 'Command Line'
jbNameHeader = 'Job Name'
sheet = 'MYTELL_AU'

allCommands = [x for x in getDataofHeader(xlFile, sheet, cmdHeader) if x!=None] #this odd looking code for removing none values
allJobNames = [y for y in getDataofHeader(xlFile, sheet, jbNameHeader) if y!=None]




extension = ('ac','cc','sc','eac','ss','pc','fp')
extSbt_and_Ebt = ('ac','cc','sc','eac','ss','pc')
flow = [[{'AR':extension}],[{'SBT':extSbt_and_Ebt}],[{'FW':extension}],[{'DLT':extension}],[{'CP':extension}],[{'LD':extension}],[{'TV':extension},{'DV':extension},{'EBT':extSbt_and_Ebt}]]
modifiedFile = "RSDS_SITControl M_requirement_sheet_MYTELL.xml"
server = "PCMAU01"
'''createSingleFlowTemplate(appCode, countryCode, effectiveAppCode, srcSys, projectCode, filePattern, server, flow)'''
createSingleFlowTemplate(['BIH'],['AU'],['EW'],[''],['MYTRELL'],['EJTABLE1','PINPADLOG', 'SECURITY'],server, flow).write(modifiedFile)
'''pass the xmlTree and all the commandlines to a function that will modify the tree by adding the correct command lines'''
##for i in allCommands:
##    print(i)
##    print()
##
##for j in allJobNames:
##    print(j)
##    print()
