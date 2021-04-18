from CodegenUtils import indent

class StateCodegen:

    def __init__(self, parent):
        self.parent = parent

    def getIdentifier(self):
        return "STATE." + self.parent.name.upper()

    def getEnumDeclaration(self):
        return indent(2) + self.parent.name.upper() + ",\n"

    def getStateOutputAction(self):
        retStr = ""
        for action in self.parent.actions:
            retStr += indent(3) + action.cg.getCode()
        return retStr