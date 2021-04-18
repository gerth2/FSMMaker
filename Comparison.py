from CodegenOperator import CodegenOperator
from ComparisonCodegen import ComparisonCodegen
from FSMConfig import FSMConfig
import xml.etree.ElementTree as ET
from CodegenDatatype import parseAsType
from FSMConfig import FSMConfig
from CodegenOperator import fromXMLCfgStr

class Comparison:

    def __init__(self):
        self.ADataId = None
        self.BDataId = None
        self.constVal = None
        self.operator = None
        self.cg = ComparisonCodegen(self)

    def parseCfg(self, etreeNode):
        gc = FSMConfig()
        for child in etreeNode:
            if(child.tag == "AData"):
                self.ADataId = int(child.text)
            elif(child.tag == "BData"):
                bDataTypeStr = child.attrib["type"]
                if(bDataTypeStr == "constant"):
                    for subChild in child:
                        if(subChild.tag == "value"):
                            self.constVal = parseAsType(gc.allData[self.ADataId].dataType, subChild.text)
                elif(bDataTypeStr == "data"):
                     for subChild in child:
                        if(subChild.tag == "id"):
                            self.BDataId = int(subChild.text)
            elif(child.tag == "operator"):
                self.operator = fromXMLCfgStr(child.text)


    def dumpCfg(self):
        return ET.Element() #TODO: generate XML representation of current object