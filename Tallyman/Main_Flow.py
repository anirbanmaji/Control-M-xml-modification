'''
Put all the commands in the same order,
first FW command has to be for the same
file as the fisr CD, or MSEQ command
'''

import xml.etree.ElementTree as ET
from createJob import createJob
from createConnection import buildSimpleConnection
from addCommand import putCommand

def createSingleFlowTemplate(folderName, subapp, application, appCode, countryCode, effectiveAppCode, srcSys, projectCode, filePattern, server, flow): #add 'effectiveAppCode' and 'srcSys'
    
    jobNameList = []
    levelwiseJobs = []
    levelwiseJobsExt = []
    
    jobBufferBeforeTree = []

    serverToCode = {'PCMAU01':'P', 'DCMAU02':'D', 'QCMAU01':'P'}#change dending on DEV or SIT
    serverToNode = {'PCMAU01':'aup4430l.unix.anz', 'DCMAU02':'aud4458l.unix.anz', 'QCMAU01':'auq4527l.unix.anz'}#change dending on DEV or SIT
    

    serverCode = []
    serverCode.append(serverToCode[server])
    
    for layer in flow:
        sameLevelJobs = []
        sameLevelJobsNames = []
        sameLevelJobsNamesWithoutAct = []
        
        for node in layer:
            for actExt in node:
                extList = node[actExt]

                '''The following part is used only for job name'''
                for ac in appCode:
                    for cc in countryCode:
                        for sc in serverCode:
                            for eac in effectiveAppCode:
                                for ss in srcSys:
                                    for pc in projectCode:
                                        for fp in filePattern:
                                            jobNameWithoutAct = (ac if ('ac' in extList) else '')+(cc if 'cc' in extList else '')+('_'+sc if 'sc' in extList else '')+('_'+eac if 'eac' in extList else '')+(ss if 'ss' in extList else '')+('_'+pc if 'pc' in extList else '')+('_'+fp if 'fp' in extList else '')
                                            jobName = jobNameWithoutAct+'_'+actExt
                                            currentJob = createJob(JOBNAME=jobName, NODEID=serverToNode[server], SUB_APPLICATION=subapp, APPLICATION=application)
                                            if jobName in sameLevelJobsNames:
                                                pass
                                            else:
                                                sameLevelJobs.append(currentJob)
                                                sameLevelJobsNames.append(jobName)
                                                sameLevelJobsNamesWithoutAct.append(jobNameWithoutAct)

        levelwiseJobs.append(sameLevelJobs)
        levelwiseJobsExt.append(sameLevelJobsNamesWithoutAct)

    for p in levelwiseJobs:
        for q in p:
            print(q.attrib["JOBNAME"])
        print()
    print('________________________________________')

    
    for i in range(1, len(levelwiseJobs)):
        for j in range(0,len(levelwiseJobs[i])):
            currentJobExt = levelwiseJobsExt[i][j]
            try:
                indexOfPrevJob = levelwiseJobsExt[i-1].index(currentJobExt)
                prevJob = levelwiseJobs[i-1][indexOfPrevJob]
                currentJob = levelwiseJobs[i][j]
                levelwiseJobs[i-1][indexOfPrevJob],levelwiseJobs[i][j] = buildSimpleConnection(prevJob, currentJob)
            except:
                print('Branching or marging')
                for k in range(0,len(levelwiseJobs[i-1])):
                    prevJob = levelwiseJobs[i-1][k]
                    currentJob = levelwiseJobs[i][j]
                    levelwiseJobs[i-1][k],levelwiseJobs[i][j] = buildSimpleConnection(prevJob, currentJob)

    for p in levelwiseJobs:
        for q in p:
            jobBufferBeforeTree.append(q)
         
    root = ET.Element('DEFTABLE')
    folder = ET.Element('FOLDER', DATACENTER=server, FOLDER_NAME=folderName)
    root.append(folder)
    tree = ET.ElementTree(root)
    for job in jobBufferBeforeTree:
        folder.append(job)
    return tree


def flow_details():
    '''
    ac in appCode:
    cc in countryCode:
    sc in serverCode:
    eac in effectiveAppCode:
    ss in srcSys:
    pc in projectCode:
    fp in filePattern:
    '''
    extension = ('ac','cc','sc','eac','ss','pc','fp')#change
    extSbt = ('ac','cc','eac','sc','ss','pc')#change
    flow = [[{'FW':extension}],[{'GBT':extension}],[{'MSEQ':extension}],[{'CD':extension}],[{'EBT':extension}]]
    modifiedFile = "new.xml"
    server = "DCMAU02"
    short_file_names = ["SECURITYACTIONS",
                        "CUSTOMERFLAGS",
                        "ACCOUNTFLAGS",
                        "SECURITYFLAGS"]#change
    
    #createSingleFlowTemplate(folderName, subapp, application, appCode, countryCode, effectiveAppCode, srcSys, projectCode, filePattern, server, flow)
    createSingleFlowTemplate('BIHAU_D_BHTALLYMAN_CRDH','BIHAU_D_TALLYMAN_CRDH','BIHAU_D',['BIH'],['AU'],['BH'],['TALLYMAN'],['CRDH'],short_file_names, server, flow).write(modifiedFile)


if __name__=="__main__":
    flow_details()
    putCommand()
