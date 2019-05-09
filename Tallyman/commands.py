FW = [
'ctmfw "/opt/ibm/working/BIH_T2/data/in/TALLYMAN/AU/new/SecurityActions_??????????????.txt" CREATE 0 300 10 3 60',
'ctmfw "/opt/ibm/working/BIH_T2/data/in/TALLYMAN/AU/new/CustomerFlags_??????????????.txt" CREATE 0 300 10 3 60',
'ctmfw "/opt/ibm/working/BIH_T2/data/in/TALLYMAN/AU/new/AccountFlags_??????????????.txt" CREATE 0 300 10 3 60',
'ctmfw "/opt/ibm/working/BIH_T2/data/in/TALLYMAN/AU/new/SecurityFlags_??????????????.txt" CREATE 0 300 10 3 60'
]

GBT = [
'/opt/ibm/working/BIH_T2/appl/sh/RunDataStageJob.ksh -p BIH_SMPL_PASSTHR2_T2 -j Generic_GenBatchId_MSeq.SECR_ACTION -v "PS_ACE_BIH=PS_ACE_BIH_P" -v "PS_GENERIC=PS_TALLYM_SECURITY_ACTIONS"',
'/opt/ibm/working/BIH_T2/appl/sh/RunDataStageJob.ksh -p BIH_SMPL_PASSTHR2_T2 -j Generic_GenBatchId_MSeq.CUST_FLAG -v "PS_ACE_BIH=PS_ACE_BIH_P" -v "PS_GENERIC=PS_TALLYM_CUSTOMER_FLAGS"',
'/opt/ibm/working/BIH_T2/appl/sh/RunDataStageJob.ksh -p BIH_SMPL_PASSTHR2_T2 -j Generic_GenBatchId_MSeq.ACC_FLAG -v "PS_ACE_BIH=PS_ACE_BIH_P" -v "PS_GENERIC=PS_TALLYM_ACCOUNT_FLAGS"',
'/opt/ibm/working/BIH_T2/appl/sh/RunDataStageJob.ksh -p BIH_SMPL_PASSTHR2_T2 -j Generic_GenBatchId_MSeq.SECR_FLAG -v "PS_ACE_BIH=PS_ACE_BIH_P" -v "PS_GENERIC=PS_TALLYM_SECURITY_FLAGS"'
]

MSEQ = [
'/opt/ibm/working/BIH_T2/appl/sh/RunDataStageJob.ksh -p BIH_SMPL_PASSTHR2_T2 -j Generic_Passthrough_MSeq.SECR_ACTION -v "PS_ACE_BIH=PS_ACE_BIH_P" -v "PS_GENERIC=PS_TALLYM_SECURITY_ACTIONS"',
'/opt/ibm/working/BIH_T2/appl/sh/RunDataStageJob.ksh -p BIH_SMPL_PASSTHR2_T2 -j Generic_Passthrough_MSeq.CUST_FLAG -v "PS_ACE_BIH=PS_ACE_BIH_P" -v "PS_GENERIC=PS_TALLYM_CUSTOMER_FLAGS"',
'/opt/ibm/working/BIH_T2/appl/sh/RunDataStageJob.ksh -p BIH_SMPL_PASSTHR2_T2 -j Generic_Passthrough_MSeq.ACC_FLAG -v "PS_ACE_BIH=PS_ACE_BIH_P" -v "PS_GENERIC=PS_TALLYM_ACCOUNT_FLAGS"',
'/opt/ibm/working/BIH_T2/appl/sh/RunDataStageJob.ksh -p BIH_SMPL_PASSTHR2_T2 -j Generic_Passthrough_MSeq.SECR_FLAG -v "PS_ACE_BIH=PS_ACE_BIH_P" -v "PS_GENERIC=PS_TALLYM_SECURITY_FLAGS"'
]

CD = [
'/opt/ibm/working/connectdirect/TMPC_BIH_CAMO/TMPC_SecurityActions_CD.sh',
'/opt/ibm/working/connectdirect/TMPC_BIH_CAMO/TMPC_CustomerFlags_CD.sh',
'/opt/ibm/working/connectdirect/TMPC_BIH_CAMO/TMPC_AccountFlags_CD.sh',
'/opt/ibm/working/connectdirect/TMPC_BIH_CAMO/TMPC_SecurityFlags_CD.sh'
]

EBT = [
'/opt/ibm/working/BIH_T2/appl/sh/RunDataStageJob.ksh -p BIH_SMPL_PASSTHR2_T2 -j Generic_EndBatchId_MSeq.SECR_ACTION -v "PS_ACE_BIH=PS_ACE_BIH_P" -v "PS_GENERIC=PS_TALLYM_SECURITY_ACTIONS"',
'/opt/ibm/working/BIH_T2/appl/sh/RunDataStageJob.ksh -p BIH_SMPL_PASSTHR2_T2 -j Generic_EndBatchId_MSeq.CUST_FLAG -v "PS_ACE_BIH=PS_ACE_BIH_P" -v "PS_GENERIC=PS_TALLYM_CUSTOMER_FLAGS"',
'/opt/ibm/working/BIH_T2/appl/sh/RunDataStageJob.ksh -p BIH_SMPL_PASSTHR2_T2 -j Generic_EndBatchId_MSeq.ACC_FLAG -v "PS_ACE_BIH=PS_ACE_BIH_P" -v "PS_GENERIC=PS_TALLYM_ACCOUNT_FLAGS"',
'/opt/ibm/working/BIH_T2/appl/sh/RunDataStageJob.ksh -p BIH_SMPL_PASSTHR2_T2 -j Generic_EndBatchId_MSeq.SECR_FLAG -v "PS_ACE_BIH=PS_ACE_BIH_P" -v "PS_GENERIC=PS_TALLYM_SECURITY_FLAGS"'
]