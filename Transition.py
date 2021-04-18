

from Action import Action
from TransitionCodegen import TransitionCodegen
from TransitionGraphic import TransitionGraphic

import xml.etree.ElementTree as ET


class Transition:

    def __init__(self, id):
        self.id = id
        self.fromStateID = None
        self.toStateID = None
        self.cg = TransitionCodegen(self)
        self.graphic = TransitionGraphic(self)
        self.actions = []
    
        
    def parseCfg(self, etreeNode):
        for child in etreeNode:
            if(child.tag == "from"):
                self.fromStateID = int(child.text)
            elif(child.tag == "to"):
                self.toStateID = int(child.text)
            elif(child.tag == "action"):
                newAction = Action()
                newAction.parseCfg(child)
                self.actions.append(newAction)


    def dumpCfg(self):
        return ET.Element() #TODO: generate XML representation of current object
