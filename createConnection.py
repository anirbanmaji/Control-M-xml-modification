import xml.etree.ElementTree as ET
def buildSimpleConnection(predecessor, successor):
    predName = predecessor.attrib['JOBNAME']
    succName = successor.attrib['JOBNAME']
    
    predecessor.append(outConditionBuilder(predName+'-TO-'+succName, '+'))
    successor.append(inConditionBuilder(predName+'-TO-'+succName))
    successor.append(outConditionBuilder(predName+'-TO-'+succName, '-'))
    
    return predecessor, successor

def outConditionBuilder(conditionName, sign, odate = 'ODAT'):
    outCond = ET.Element('OUTCOND', NAME=conditionName, ODATE=odate, SIGN=sign)
    return outCond

def inConditionBuilder(conditionName, and_or='A', op='', odate = 'ODAT'):
    if op == '':
        inCond = ET.Element('INCOND', NAME=conditionName, ODATE=odate, AND_OR="A")
    else:
        inCond = ET.Element('INCOND', NAME=conditionName, ODATE=odate, AND_OR="A", OP=op)
    return inCond
