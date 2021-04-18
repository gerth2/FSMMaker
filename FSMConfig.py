# Singleton configuration of the full FSM 

class FSMConfig(object):
    _instance = None

    # FSM Generator State, with on-load defaults
    allStates = {}
    allTransitions = {}
    allData = {}

    configFPath = None

    outputFPath = "./output.java"
    className = "mainFSM"
    defaultStateID = None
    description = "Auto-Generated State Machine"
    packageName = "frc.robot"

    def __new__(self):
        if self._instance is None:
            print('Creating the object')
            self._instance = super(FSMConfig, self).__new__(self)
            # Put any initialization here.
        return self._instance


