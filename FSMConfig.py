# Singleton configuration of the full FSM 

class FSMConfig(object):
    _instance = None



    def __new__(self):
        if self._instance is None:
            self._instance = super(FSMConfig, self).__new__(self)
            self.resetToDefault(self._instance)

        return self._instance

    def resetToDefault(self):
        # FSM Generator State, with on-load defaults
        self.allStates = {}
        self.allTransitions = {}
        self.allData = {}

        self.configFPath = None

        self.outputFPath = "./output.java"
        self.className = "mainFSM"
        self.defaultStateID = None
        self.description = "Auto-Generated State Machine"
        self.packageName = "frc.robot"