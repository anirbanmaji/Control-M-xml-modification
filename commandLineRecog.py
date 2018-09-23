import openpyxl
from getValuesFromHeader import getDataofHeader

xlFile = 'C:/Users/AnirbanMaji/Desktop/Control M RSDS jobs/RSDS_SITControl M_requirement_sheet_MYTELL.xlsm'
cmdHeader = 'Command Line'
jbNameHeader = 'Job Name'
sheet = 'MYTELL_AU'

allCommands = [x for x in getDataofHeader(xlFile, sheet, cmdHeader) if x!=None] #this odd looking code for removing none values
allJobNames = [y for y in getDataofHeader(xlFile, sheet, jbNameHeader) if y!=None]

for i in allCommands:
    print(i)
    print()

for j in allJobNames:
    print(j)
    print()
