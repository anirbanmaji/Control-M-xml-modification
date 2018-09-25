import xml.etree.ElementTree as ET
from createJob import createJob
from createConnection import buildSimpleConnection



def createSingleFlowTemplate(appCode, countryCode, serverCode, effectiveAppCode, srcSys, projectCode, filePattern, flow): #add 'effectiveAppCode' and 'srcSys'
    
    '''define 'folderName' variable here and then pass it while creating jobs and folder'''
    ''''BIHZZ_P_EWPSGL_APRA_ABC'''
    
    jobNameList = []
    jobBufferBeforeTree = []
    for layer in flow:
        #list
        for node in layer:
            sameLevelJobs = []
            #dictionary
            for actExt in node:
                #string
                #print(node[actExt])
                extList = node[actExt]


                '''The following part is used only for job name'''
                for ac in appCode:
                    for cc in countryCode:
                        for sc in serverCode:
                            for eac in effectiveAppCode:
                                for ss in srcSys:
                                    for pc in projectCode:
                                        for fp in filePattern:
                                            jobName = (ac if ('ac' in extList) else '')+(cc if 'cc' in extList else '')+('_'+sc if 'sc' in extList else '')+('_'+eac if 'eac' in extList else '')+(ss if 'ss' in extList else '')+('_'+pc if 'pc' in extList else '')+('_'+fp if 'fp' in extList else '')+'_'+actExt
                                            jobNameWithoutAct = (ac if ('ac' in extList) else '')+(cc if 'cc' in extList else '')+('_'+sc if 'sc' in extList else '')+('_'+eac if 'eac' in extList else '')+(ss if 'ss' in extList else '')+('_'+pc if 'pc' in extList else '')+('_'+fp if 'fp' in extList else '')
                                            currentJob = createJob(JOBNAME=jobName)


                                            
                                            currentJobName = currentJob.attrib['JOBNAME']
                                            sameLevelJobsNames = []
                                            for element in sameLevelJobs:
                                                sameLevelJobsNames.append(element.attrib['JOBNAME'])
                                            if currentJobName not in sameLevelJobsNames:
                                                sameLevelJobs.append(currentJob)
                                                try:
                                                    spread = True
                                                    for prevJob in jobNameList[-1]:#to connect to the same extesion jobs, one-to-one and many-to-one connection 
                                                        if jobNameWithoutAct in prevJob.attrib['JOBNAME']:#check if previous jobs extension is matching with the current jobs
                                                            spread = False
                                                            indexOfPreviousJob = jobBufferBeforeTree.index(prevJob)
                                                            jobBufferBeforeTree[indexOfPreviousJob],currentJob = buildSimpleConnection(prevJob, currentJob)
                                                    if spread:#one-to-many connection
                                                        prevJob = jobNameList[-1][0]
                                                        indexOfPreviousJob = jobBufferBeforeTree.index(prevJob)
                                                        jobBufferBeforeTree[indexOfPreviousJob],currentJob = buildSimpleConnection(prevJob, currentJob)

                                                except:
                                                    pass
                                                print(currentJob.attrib['JOBNAME'])
                                                jobBufferBeforeTree.append(currentJob)
            jobNameList.append(sameLevelJobs)
            #print(jobNameList)
            print()
    root = ET.Element('DEFTABLE')       
    folderName = jobBufferBeforeTree[0].attrib['PARENT_FOLDER']
    folder = ET.Element('FOLDER', DATACENTER="PCMAU01", PARENT_FOLDER=folderName)
    root.append(folder)
    tree = ET.ElementTree(root)
    for job in jobBufferBeforeTree:
        folder.append(job)
    return tree


if __name__ == "__main__":
    extension = ('ac','cc','sc','eac','ss','pc','fp')
    extSbt = ('ac','cc','sc','eac','ss','pc')
    flow = [[{'AR':extension}],[{'SBT':extSbt}],[{'FW':extension}],[{'DLT':extension}],[{'CP':extension}],[{'LD':extension}],[{'TV':extension},{'DV':extension},{'EBT':extSbt}]]
    modifiedFile = "new.xml"
    createSingleFlowTemplate(['BIH'],['ZZ'],['P'],['EW'],['PSGL'],['APRA'],['ABC','DEF'], flow).write(modifiedFile)

