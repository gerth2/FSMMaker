from ActionCodegen import ActionCodegen
from FSMConfig import FSMConfig
import xml.etree.ElementTree as ET
from CodegenDatatype import parseAsType
from FSMConfig import FSMConfig

class Action:

    def __init__(self):
        self.tgtId = None
        self.srcId = None
        self.constVal = None
        self.cg = ActionCodegen(self)

    def parseCfg(self, etreeNode):
        gc = FSMConfig()
        for child in etreeNode:
            if(child.tag == "target"):
                self.tgtId = int(child.text)
            elif(child.tag == "source"):
                srcTypeStr = child.attrib["type"]
                if(srcTypeStr == "constant"):
                    for subChild in child:
                        if(subChild.tag == "value"):
                            self.constVal = parseAsType(gc.allData[self.tgtId].dataType, subChild.text)
                elif(srcTypeStr == "data"):
                     for subChild in child:
                        if(subChild.tag == "id"):
                            self.srcId = int(subChild.text)


    def dumpCfg(self):
        return ET.Element() #TODO: generate XML representation of current object