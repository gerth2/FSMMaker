from CodegenOperator import toJavaDatatypeStr
from CodegenDatatype import CodegenDatatype
from FSMConfig import FSMConfig



class ComparisonCodegen:

    def __init__(self, parent):
        self.parent = parent

    def getCode(self):
        gc = FSMConfig()
        retStr = gc.allData[self.parent.ADataId].cg.getIdentifier() + toJavaDatatypeStr(self.parent.operator)
        outType = gc.allData[self.parent.ADataId].dataType

        if(self.parent.constVal is not None):
            if(outType == CodegenDatatype.BOOLEAN):
                if(self.parent.constVal):
                    retStr += "true"
                else:
                    retStr += "false"
            else:
                retStr += str(self.parent.constVal) # "str" happens to convert nicely to a java-readable expression?
        else:
            retStr += gc.allData[self.parent.srcId].cg.getIdentifier()

        return retStr