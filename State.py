from Action import Action
from StateCodegen import StateCodegen
from StateGraphic import StateGraphic

import xml.etree.ElementTree as ET


class State:

    def __init__(self, id):
        self.id = id
        self.fromState = None
        self.toState = None
        self.cg = StateCodegen(self)
        self.graphic = StateGraphic(self)
        self.name = ""
        self.actions = []
            
    def parseCfg(self, etreeNode):
        for child in etreeNode:
            if(child.tag == "name"):
                self.name = str(child.text).strip()
            elif(child.tag == "action"):
                newAction = Action()
                newAction.parseCfg(child)
                self.actions.append(newAction)

    def dumpCfg(self):
        return ET.Element() #TODO: generate XML representation of current object