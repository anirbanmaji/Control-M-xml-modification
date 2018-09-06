import xml.etree.ElementTree as ET
from createJob import createJob
from createConnection import buildSimpleConnection

extension = ('ac','cc','sc','pc','fp')
extSbt = ('ac','cc','sc','pc')
flow = [[{'AR':extension}],[{'SBT':extSbt}],[{'FW':extension}],[{'DLT':extension}],[{'CP':extension}],[{'LD':extension}],[{'TV':extension},{'DV':extension},{'EBT':extSbt}]]


def createSingleFlowTemplate(appCode, countryCode, serverCode, projectCode, filePattern, flow): #add 'effectiveAppCode' and 'srcSys'
    
    '''define 'folderName' variable here and then pass it while creating jobs and folder'''
    
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
                for ac in appCode:
                    for cc in countryCode:
                        for sc in serverCode:
                            for pc in projectCode:
                                for fp in filePattern:
                                    jobName = (ac if ('ac' in extList) else '')+(cc if 'cc' in extList else '')+('_'+sc if 'sc' in extList else '')+('_'+pc if 'pc' in extList else '')+('_'+fp if 'fp' in extList else '')+'_'+actExt
                                    jobNameWithoutAct = (ac if ('ac' in extList) else '')+(cc if 'cc' in extList else '')+('_'+sc if 'sc' in extList else '')+('_'+pc if 'pc' in extList else '')+('_'+fp if 'fp' in extList else '')
                                    currentJob = createJob(JOBNAME=jobName)
                                    currentJobName = currentJob.attrib['JOBNAME']
                                    sameLevelJobsNames = []
                                    for element in sameLevelJobs:
                                        sameLevelJobsNames.append(element.attrib['JOBNAME'])
                                    if currentJobName not in sameLevelJobsNames:
                                        sameLevelJobs.append(currentJob)
                                        try:
                                            #print(jobNameList[-1])
                                            spread = True
                                            for prevJob in jobNameList[-1]:#to connect to the same extesion jobs, one-to-one and many-to-one connection 
                                                if jobNameWithoutAct in prevJob.attrib['JOBNAME']:#check if previous jobs extension is matching with the current jobs
                                                    #print('True')
                                                    #print('pre '+prevJob.attrib['JOBNAME'])
                                                    spread = False
                                                    indexOfPreviousJob = jobBufferBeforeTree.index(prevJob)
                                                    jobBufferBeforeTree[indexOfPreviousJob],currentJob = buildSimpleConnection(prevJob, currentJob)#make a function like buildConnection(predessor, succesor), more details in Sublimetext
                                            if spread:#one-to-many connection
                                                #print('spread')
                                                prevJob = jobNameList[-1][0]
                                                indexOfPreviousJob = jobBufferBeforeTree.index(prevJob)
                                                jobBufferBeforeTree[indexOfPreviousJob],currentJob = buildSimpleConnection(prevJob, currentJob)
                                                #print('pre '+prevJob.attrib['JOBNAME'])
                                                #buildConnection(jobNameList[-1][0], jobName)
                                        except:
                                            pass
                                        print('current '+currentJob.attrib['JOBNAME'])
                                        jobBufferBeforeTree.append(currentJob)
            jobNameList.append(sameLevelJobs)
            #print(jobNameList)
            print()
    root = ET.Element('DEFTABLE')       
    folderName = jobBufferBeforeTree[0].attrib['PARENT_FOLDER']
    folder = ET.Element('FOLDER', DATACENTER="DCMAU01", PARENT_FOLDER=folderName)
    root.append(folder)
    tree = ET.ElementTree(root)
    for job in jobBufferBeforeTree:
        folder.append(job)
    return tree

##job1 = createJob(JOBNAME = 'JOB1')
##job2 = createJob(JOBNAME = 'JOB2')
##x,y = buildSimpleConnection(job1, job2)
##print(ET.tostring(x))
##print(ET.tostring(y))

modifiedFile = "new.xml"
createSingleFlowTemplate(['BIH'],['ZZ'],['P'],['PSGL'],['ABC','DEF'], flow).write(modifiedFile)

