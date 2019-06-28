FW = ['ctmfw "/opt/ibm/working/BIH_T2/data/in/GADEN/AU/new/Litigation_IF_ContactLog_Gadens_??????????????.txt" CREATE 0 300 10 3 60',
'ctmfw "/opt/ibm/working/BIH_T2/data/in/GADEN/AU/new/Litigation_IF_AccUpdates_Gadens_??????????????.txt" CREATE 0 300 10 3 60',
'ctmfw "/opt/ibm/working/BIH_T2/data/in/GADEN/AU/new/Litigation_IF_SecUpdates_Gadens_??????????????.txt" CREATE 0 300 10 3 60',
'ctmfw "/opt/ibm/working/BIH_T2/data/in/GADEN/AU/new/SolicitorDefaultUpdates_Gadens_HL_??????????????.txt" CREATE 0 300 10 3 60'

]

GBT = ['/opt/ibm/working/BIH_D1/appl/sh/RunDataStageJob.ksh -p BIH_SMPL_PASSTHR2_D -j Generic_GenBatchId_MSeq.IF_ContactLog_Gadens -v "PS_ACE_BIH=PS_ACE_BIH_P" -v "PS_GENERIC=PS_IF_ContactLog_Gadens"',
'/opt/ibm/working/BIH_D1/appl/sh/RunDataStageJob.ksh -p BIH_SMPL_PASSTHR2_D -j Generic_GenBatchId_MSeq.LI_IF_AccUpdates_Gadens -v "PS_ACE_BIH=PS_ACE_BIH_P" -v "PS_GENERIC=PS_LI_IF_AccUpdates_Gadens"',
'/opt/ibm/working/BIH_D1/appl/sh/RunDataStageJob.ksh -p BIH_SMPL_PASSTHR2_D -j Generic_GenBatchId_MSeq.LI_IF_SecUpdates_Gadens -v "PS_ACE_BIH=PS_ACE_BIH_P" -v "PS_GENERIC=PS_LI_IF_SecUpdates_Gadens"',
'/opt/ibm/working/BIH_D1/appl/sh/RunDataStageJob.ksh -p BIH_SMPL_PASSTHR2_D -j Generic_GenBatchId_MSeq.SolicitorDefaultUpdates_Gadens -v "PS_ACE_BIH=PS_ACE_BIH_P" -v "PS_GENERIC=PS_SolicitorDefaultUpdates_Gadens"',
]

MSEQ = ['/opt/ibm/working/BIH_D1/appl/sh/RunDataStageJob.ksh -p BIH_SMPL_PASSTHR2_D -j Generic_Passthrough_MSeq.IF_ContactLog_Gadens -v "PS_ACE_BIH=PS_ACE_BIH_P" -v "PS_GENERIC=PS_IF_ContactLog_Gadens"',
'/opt/ibm/working/BIH_D1/appl/sh/RunDataStageJob.ksh -p BIH_SMPL_PASSTHR2_D -j Generic_Passthrough_MSeq.LI_IF_AccUpdates_Gadens -v "PS_ACE_BIH=PS_ACE_BIH_P" -v "PS_GENERIC=PS_LI_IF_AccUpdates_Gadens"',
'/opt/ibm/working/BIH_D1/appl/sh/RunDataStageJob.ksh -p BIH_SMPL_PASSTHR2_D -j Generic_Passthrough_MSeq.LI_IF_SecUpdates_Gadens -v "PS_ACE_BIH=PS_ACE_BIH_P" -v "PS_GENERIC=PS_LI_IF_SecUpdates_Gadens"',
'/opt/ibm/working/BIH_D1/appl/sh/RunDataStageJob.ksh -p BIH_SMPL_PASSTHR2_D -j Generic_Passthrough_MSeq.SolicitorDefaultUpdates_Gadens -v "PS_ACE_BIH=PS_ACE_BIH_P" -v "PS_GENERIC=PS_SolicitorDefaultUpdates_Gadens"',
]

CD = [
'/opt/ibm/working/connectdirect/Gadens_IF_LIT_TMPC/GADENS_IF_LIT_CONTACTLOG_CD.sh',
'/opt/ibm/working/connectdirect/Gadens_IF_LIT_TMPC/GADENS_IF_LIT_ACCUPDATES_CD.sh',
'/opt/ibm/working/connectdirect/Gadens_IF_LIT_TMPC/GADENS_IF_LIT_SECUPDATES_CD.sh',
'/opt/ibm/working/connectdirect/Gadens_IF_LIT_TMPC/SOLI_UPDATE_GADENS_CD.sh'
]

EBT = ['/opt/ibm/working/BIH_D1/appl/sh/RunDataStageJob.ksh -p BIH_SMPL_PASSTHR2_D -j Generic_EndBatchId_MSeq.IF_ContactLog_Gadens -v "PS_ACE_BIH=PS_ACE_BIH_P" -v "PS_GENERIC=PS_IF_ContactLog_Gadens"',
'/opt/ibm/working/BIH_D1/appl/sh/RunDataStageJob.ksh -p BIH_SMPL_PASSTHR2_D -j Generic_EndBatchId_MSeq.LI_IF_AccUpdates_Gadens -v "PS_ACE_BIH=PS_ACE_BIH_P" -v "PS_GENERIC=PS_LI_IF_AccUpdates_Gadens"',
'/opt/ibm/working/BIH_D1/appl/sh/RunDataStageJob.ksh -p BIH_SMPL_PASSTHR2_D -j Generic_EndBatchId_MSeq.LI_IF_SecUpdates_Gadens -v "PS_ACE_BIH=PS_ACE_BIH_P" -v "PS_GENERIC=PS_LI_IF_SecUpdates_Gadens"',
'/opt/ibm/working/BIH_D1/appl/sh/RunDataStageJob.ksh -p BIH_SMPL_PASSTHR2_D -j Generic_EndBatchId_MSeq.SolicitorDefaultUpdates_Gadens -v "PS_ACE_BIH=PS_ACE_BIH_P" -v "PS_GENERIC=PS_SolicitorDefaultUpdates_Gadens"',
]