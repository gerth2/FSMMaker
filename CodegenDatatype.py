from enum import Enum

class CodegenDatatype(Enum):
     INT = 1
     DOUBLE = 2
     BOOLEAN = 3

def parseAsType(cgDT, str):
    if(cgDT == CodegenDatatype.INT):
        return int(str)
    elif(cgDT == CodegenDatatype.DOUBLE):
        return float(str)
    elif(cgDT == CodegenDatatype.BOOLEAN):
        return bool(str)

def toJavaDatatypeStr(cgDT):
    if(cgDT == CodegenDatatype.INT):
        return "int"
    elif(cgDT == CodegenDatatype.DOUBLE):
        return "double"
    elif(cgDT == CodegenDatatype.BOOLEAN):
        return "boolean"

def fromXMLCfgStr(cfgStr):
    cfgStr = cfgStr.lower().strip()
    if(cfgStr == "int" ):
        return CodegenDatatype.INT
    elif(cfgStr == "double" ):
        return CodegenDatatype.DOUBLE
    elif(cfgStr == "boolean"):
        return  CodegenDatatype.BOOLEAN