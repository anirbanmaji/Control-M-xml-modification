class Dependency(currentNode, successors=None):
    self.currentNode = currentNode
    self.successors = successors

ebt = Dependency('EBT')
tv = Dependency()
fw = Dependency('FW',['DLT'])

fw>dlt>cp>ld>tv,dv,ebt
