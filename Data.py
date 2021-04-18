from DataCodegen import DataCodegen
import xml.etree.ElementTree as ET
from CodegenDatatype import fromXMLCfgStr

class Data:

    def __init__(self, id):
        self.id = id
        self.name = ""
        self.isInput = False
        self.isOutput = False
        self.dataType = None
        self.cg = DataCodegen(self)

    def parseCfg(self, etreeNode):
        for child in etreeNode:
            if(child.tag == "name"):
                self.name = str(child.text).strip()
            elif(child.tag == "isInput"):
                self.isInput = bool(child.text)
            elif(child.tag == "isOutput"):
                self.isOutput = bool(child.text)
            elif(child.tag == "type"):
                self.dataType = fromXMLCfgStr(child.text)


    def dumpCfg(self):
        return ET.Element() #TODO: generate XML representation of current object