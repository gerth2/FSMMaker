from CodegenDatatype import CodegenDatatype
from FSMConfig import FSMConfig



class ActionCodegen:

    def __init__(self, parent):
        self.parent = parent

    def getCode(self):
        gc = FSMConfig()
        retStr = gc.allData[self.parent.tgtId].cg.getIdentifier() + " = "
        outType = gc.allData[self.parent.tgtId].dataType

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

        retStr += ";\n"

        return retStr