from enum import Enum

class CodegenOperator(Enum):
     GT = 1
     LT = 2
     EQ = 3
     NEQ = 4
     GTEQ = 5
     LTEQ = 6

def toJavaDatatypeStr(cgOP):
    if(cgOP == CodegenOperator.GT):
        return " > "
    elif(cgOP == CodegenOperator.LT):
        return " < "
    elif(cgOP == CodegenOperator.EQ):
        return " == "
    elif(cgOP == CodegenOperator.NEQ):
        return " != "
    elif(cgOP == CodegenOperator.GTEQ):
        return " >= "
    elif(cgOP == CodegenOperator.LTEQ):
        return " <= "

def fromXMLCfgStr(cfgStr):
    cfgStr = cfgStr.lower().strip()
    if(cfgStr == "gt" ):
        return CodegenOperator.GT
    elif(cfgStr == "lt" ):
        return CodegenOperator.LT
    elif(cfgStr == "eq" ):
        return CodegenOperator.EQ
    elif(cfgStr == "neq" ):
        return CodegenOperator.NEQ
    elif(cfgStr == "gteq" ):
        return CodegenOperator.GTEQ
    elif(cfgStr == "lteq" ):
        return CodegenOperator.LTEQ

def toXMLCfgStr(cgOP):
    return str(cgOP)