import xml.etree.ElementTree as ET
from createJob import createJob
from createConnection import buildSimpleConnection



def createSingleFlowTemplate(appCode, countryCode, effectiveAppCode, srcSys, projectCode, filePattern, server, flow): #add 'effectiveAppCode' and 'srcSys'
    
    '''define 'folderName' variable here and then pass it while creating jobs and folder'''
    folderName = 'BIHZZ_T2_EDW_MIDANZSRC'#change
    subapp = 'BIHJP_T2_EDW_MIDANZ_EPS'#change
    application = 'BIHJP_T2'#change
    
    jobNameList = []
    levelwiseJobs = []
    levelwiseJobsExt = []
    
    jobBufferBeforeTree = []

    serverToCode = {'PCMAU01':'P', 'DCMAU02':'T2', 'QCMAU01':'P'}
    serverToNode = {'PCMAU01':'aup4430l.unix.anz', 'DCMAU02':'aud4459l.unix.anz', 'QCMAU01':'auq4527l.unix.anz'}
    

    serverCode = []
    serverCode.append(serverToCode[server])
    
    for layer in flow: #layer is a list of dict
        sameLevelJobs = []
        sameLevelJobsNames = []
        sameLevelJobsNamesWithoutAct = []
        
        for node in layer: #node is a dict
            for actExt in node: #actExt is a key of dictionary
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
                                            jobNameWithoutAct = (ac if ('ac' in extList) else '')+(cc if 'cc' in extList else '')+('_'+sc if 'sc' in extList else '')+('_'+eac if 'eac' in extList else '')+(ss if 'ss' in extList else '')+('_'+pc if 'pc' in extList else '')+('_'+fp if 'fp' in extList else '')
                                            jobName = jobNameWithoutAct+'_'+actExt
                                            currentJob = createJob(JOBNAME=jobName, NODEID=serverToNode[server], SUB_APPLICATION=subapp, APPLICATION=application)
                                            if jobName in sameLevelJobsNames:
                                                pass
                                            else:
                                                sameLevelJobs.append(currentJob)
                                                sameLevelJobsNames.append(jobName)
                                                sameLevelJobsNamesWithoutAct.append(jobNameWithoutAct)
                                            #print(jobName)

        levelwiseJobs.append(sameLevelJobs)
        levelwiseJobsExt.append(sameLevelJobsNamesWithoutAct)

    for p in levelwiseJobs:
        for q in p:
            print(q.attrib["JOBNAME"])
        print()
    print('________________________________________')

    
    for i in range(1, len(levelwiseJobs)):
        for j in range(0,len(levelwiseJobs[i])):
            #print(levelwiseJobsExt[i][j])
            currentJobExt = levelwiseJobsExt[i][j]
            try:
                indexOfPrevJob = levelwiseJobsExt[i-1].index(currentJobExt)
                prevJob = levelwiseJobs[i-1][indexOfPrevJob]#this will work only if same job extension exist for the previous job
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
    #folderName = jobBufferBeforeTree[0].attrib['PARENT_FOLDER']
    folder = ET.Element('FOLDER', DATACENTER=server, FOLDER_NAME=folderName)
    root.append(folder)
    tree = ET.ElementTree(root)
    for job in jobBufferBeforeTree:
        folder.append(job)
    return tree


if __name__ == "__main__":#change this block
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
    flow = [[{'AR':extension}],[{'SBT':extSbt}],[{'FW':extension}],[{'DLT':extension}],[{'CP':extension}],[{'RG':extension}],[{'LD':extension}],[{'TV':extension},{'DV':extension},{'EBT':extSbt}]]
    modifiedFile = "new.xml"
    server = "DCMAU02"
    short_file_names = ["PS_ACTION_TBL",
                        "PS_ACTN_REASON_TBL",
                        "PS_ANZ_POS_WFC",
                        "PSXLATITEM",
                        "PSTREENODE",
                        "PSOPRDEFN",
                        "PS_COMPENSATION",
                        "PS_ADDRESSES",
                        "PS_DEPT_TBL",
                        "PS_ASSIGNMENT",
                        "PS_CITIZENSHIP",
                        "PS_COMP_RATECD_TBL"]#change
    
    #createSingleFlowTemplate(appCode, countryCode, effectiveAppCode, srcSys, projectCode, filePattern, server, flow)
    createSingleFlowTemplate(['BIH'],['AU'],['BH'],['PSHCM'],['EPS_RS'],short_file_names, server, flow).write(modifiedFile)
