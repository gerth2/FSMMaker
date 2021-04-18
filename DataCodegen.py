import xml.etree.ElementTree as ET
from CodegenDatatype import fromXMLCfgStr, toJavaDatatypeStr
from CodegenUtils import indent

class DataCodegen:

    def __init__(self, parent):
        self.parent = parent

    def getIdentifier(self):
        return self.parent.name

    def getDeclaration(self):
        return indent(1) + "private " + toJavaDatatypeStr(self.parent.dataType) + " " + self.getIdentifier() + ";\n"

    def getGetter(self):
        retStr = ""
        retStr += indent(1) + "public " + toJavaDatatypeStr(self.parent.dataType) + " get" + self.getIdentifier() + "() {\n"
        retStr += indent(2) + "return " + self.getIdentifier() + ";\n"
        retStr += indent(1) + "}\n"
        return retStr

    def getSetter(self):
        retStr = ""
        retStr += indent(1) + "public void set" + self.getIdentifier() + "( " + toJavaDatatypeStr(self.parent.dataType) + " val ) {\n"
        retStr += indent(2) + self.getIdentifier() + " = val;\n"
        retStr += indent(1) + "}\n"
        return retStr