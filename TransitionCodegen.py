

from FSMConfig import FSMConfig
from CodegenUtils import indent


class TransitionCodegen:


    def __init__(self, parent):
        self.parent = parent

    def getCondition(self):
        return "true" # TODO

    def getCurStateUpdate(self):
        gc = FSMConfig()
        return "curState = " + gc.allStates[self.parent.toStateID].cg.getFullIdentifier() + ";"