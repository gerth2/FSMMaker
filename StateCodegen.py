from FSMConfig import FSMConfig
from CodegenUtils import indent

class StateCodegen:

    def __init__(self, parent):
        self.parent = parent

    def getEnumMember(self):
        return self.parent.name.upper()

    def getFullIdentifier(self):
        return "STATE." + self.getEnumMember()

    def getEnumDeclaration(self):
        return indent(2) + self.getEnumMember() + ",\n"

    def getStateOutputAction(self):
        retStr = ""
        retStr += indent(3) + "case " + self.getEnumMember() + ":\n"
        for action in self.parent.actions:
            retStr += indent(4) + action.cg.getCode()
            
        retStr += indent(4) + "break;\n"
        return retStr

    def getNextStateCase(self):
        gc = FSMConfig()
        retStr = ""
        retStr += indent(3) + "case " + self.getEnumMember() + ":\n"

        exitingTransitions = [x for x in gc.allTransitions.values() if x.fromStateID == self.parent.id]
        exitingTransitions.sort(key=lambda x: x.priority)
        for trans in exitingTransitions:
            retStr += indent(4) + "if(" + trans.cg.getCondition() + "){\n"
            retStr += indent(5) + "// Take transition " + str(trans.id) + "\n"
            for action in trans.actions:
                retStr += indent(5) + action.cg.getCode()
            retStr += indent(5) + trans.cg.getCurStateUpdate() + "\n"
            retStr += indent(5) + "break;\n"
            retStr += indent(4) + "}\n\n"

        retStr += indent(3) + "break;\n\n"
        return retStr