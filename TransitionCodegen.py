

from FSMConfig import FSMConfig
from CodegenUtils import indent


class TransitionCodegen:


    def __init__(self, parent):
        self.parent = parent

    def getCondition(self):
        if(self.parent.condition is not None):
            return self.parent.condition.cg.getCode()
        else:
            return "true"

    def getCurStateUpdate(self):
        gc = FSMConfig()
        return "curState = " + gc.allStates[self.parent.toStateID].cg.getFullIdentifier() + ";"