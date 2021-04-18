import os
from FSMConfig import FSMConfig
from tkinter import *
import xml.etree.ElementTree as ET
from string import Template

from Data import Data
from Transition import Transition
from State import State





def loadFile(fpath):
    gc = FSMConfig()
    tree = ET.parse(fpath)
    root = tree.getroot()
    if(root.tag == "FSM"):
        #First Pass - data
        for child in root :
            if(child.tag == "data"):
                newID = int(child.attrib["id"])
                gc.allData[newID] = Data(newID)
                gc.allData[newID].parseCfg(child)

        # Second Pass - States
        for child in root:
            if(child.tag == "state"):
                newID = int(child.attrib["id"])
                gc.allStates[newID] = State(newID)
                gc.allStates[newID].parseCfg(child)

        # Third Pass - Transitions
        for child in root:
            if(child.tag == "transition"):
                newID = int(child.attrib["id"])
                gc.allTransitions[newID] = Transition(newID)
                gc.allTransitions[newID].parseCfg(child)
                
        # Fourth Pass - global configuration
        for child in root:
            if(child.tag == "config"):
                parseGlobalCfg(child)
        
    gc.configFPath = fpath

def parseGlobalCfg(etreeNode):
    gc = FSMConfig()
    for child in etreeNode:
        if(child.tag == "defaultStateID"):
            gc.defaultStateID = int(child.text.strip())
        elif(child.tag == "outputFPath"):
            gc.outputFPath = str(child.text.strip())
        elif(child.tag == "className"):
            gc.className = str(child.text.strip())
        elif(child.tag == "description"):
            gc.description = str(child.text.strip())
        elif(child.tag == "packageName"):
            gc.packageName = str(child.text.strip())


def dumpGlobalCfg():
    pass #TODO - generate the global config tags

def saveFile(fpath):
    pass

def codegen():
    gc = FSMConfig()

    outputFolder = os.path.dirname(gc.outputFPath)
    if not os.path.exists(outputFolder):
        os.makedirs(outputFolder)

    with open(gc.outputFPath, "w") as outFile:
        outFileContents = ""
        
        with open('FSMTemplate.java', "r") as tfile:
            t = Template(tfile.read())
            substDict = {
                "packagename" : gc.packageName,
                "description" : gc.description,
                "classname" : gc.className,
                "statelist" : "".join([state.cg.getEnumDeclaration() for state in gc.allStates.values()]),
                "initialstate" : gc.allStates[gc.defaultStateID].cg.getFullIdentifier(),
                "datadeclarations" : "".join([data.cg.getDeclaration() for data in gc.allData.values()]),
                "setters" : "".join([data.cg.getSetter() for data in gc.allData.values() if data.isInput]),
                "getters" : "".join([data.cg.getGetter() for data in gc.allData.values() if data.isOutput]),
                "nextstatecases" : "".join([state.cg.getNextStateCase() for state in gc.allStates.values()]),
                "stateoutputcases" : "".join([state.cg.getStateOutputAction() for state in gc.allStates.values()])
            }
            outFileContents = t.substitute(substDict)
        
        outFile.write(outFileContents)



if (__name__ == "__main__"):
    loadFile("testConfig.xml")
    codegen()
    saveFile("testResavedConfig.xml")

#    dflt_canvas_width = 600
#    dflt_canvas_height = 800
#
#    colours = ("#476042", "yellow")
#    box=[]
#
#    for ratio in ( 0.2, 0.35 ):
#        box.append( (dflt_canvas_width * ratio,
#                        dflt_canvas_height * ratio,
#                        dflt_canvas_width * (1 - ratio),
#                        dflt_canvas_height * (1 - ratio) ) )
#
#    master = Tk()
#
#    mainCanvas = Canvas(master, 
#            width=dflt_canvas_width, 
#            height=dflt_canvas_height)
#    mainCanvas.pack()
#
#    for i in range(2):
#        mainCanvas.create_rectangle(box[i][0], box[i][1],box[i][2],box[i][3], fill=colours[i])
#
#    mainCanvas.create_line(0, 0,                 # origin of canvas
#                box[0][0], box[0][1], # coordinates of left upper corner of the box[0]
#                fill=colours[0], 
#                width=3)
#    mainCanvas.create_line(0, dflt_canvas_height,     # lower left corner of canvas
#                box[0][0], box[0][3], # lower left corner of box[0]
#                fill=colours[0], 
#                width=3)
#    mainCanvas.create_line(box[0][2],box[0][1],  # right upper corner of box[0] 
#                dflt_canvas_width, 0,      # right upper corner of canvas
#                fill=colours[0], 
#                width=3)
#    mainCanvas.create_line(box[0][2], box[0][3], # lower right corner pf box[0]
#                dflt_canvas_width, dflt_canvas_height, # lower right corner of canvas
#                fill=colours[0], width=3)
#
#    mainCanvas.create_text(dflt_canvas_width / 2,
#                dflt_canvas_height / 2,
#                text="Python")
#    mainloop()