import os
from FSMConfig import FSMConfig

import xml.etree.ElementTree as ET
from string import Template

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.modules import inspector
from kivy.core.window import Window


from Data import Data
from Transition import Transition
from State import State
import webbrowser



class FSMMaker(Widget):
    pass


class FSMMakerApp(App):


    dflt_canvas_width = 600
    dflt_canvas_height = 800

    def build(self):
        newThing = FSMMaker()
        inspector.create_inspector(Window, newThing)
        return newThing

    def on_start(self, **kwargs):
        guiInitialDraw()






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
                "packagename"      : gc.packageName,
                "description"      : gc.description.replace("\n", "\n * "),
                "classname"        : gc.className,
                "statelist"        : "".join([state.cg.getEnumDeclaration() for state in gc.allStates.values()]),
                "initialstate"     : gc.allStates[gc.defaultStateID].cg.getFullIdentifier(),
                "datadeclarations" : "".join([data.cg.getDeclaration() for data in gc.allData.values()]),
                "setters"          : "".join([data.cg.getSetter() for data in gc.allData.values() if data.isInput]),
                "getters"          : "".join([data.cg.getGetter() for data in gc.allData.values() if data.isOutput]),
                "nextstatecases"   : "".join([state.cg.getNextStateCase() for state in gc.allStates.values()]),
                "stateoutputcases" : "".join([state.cg.getStateOutputAction() for state in gc.allStates.values()])
            }
            outFileContents = t.substitute(substDict)
        
        outFile.write(outFileContents)

def reset():
   gc = FSMConfig()
   gc.resetToDefault()

def guiOpenHandler():
    filename =  filedialog.askopenfilename(initialdir = ".",title = "Select Config File to Open",filetypes = (("Config Files","*.xml"),("all files","*.*")))
    reset()
    loadFile(filename)
    guiInitialDraw()

def guiSaveHandler():
    gc = FSMConfig()
    if(gc.configFPath is not None):
        reset()
        saveFile(gc.configFPath)
    else:
        guiSaveAsHandler()

def guiSaveAsHandler():
    filename =  filedialog.asksaveasfilename(initialdir = ".",title = "Select Save File location",filetypes = (("Config Files","*.xml")))
    reset()
    saveFile(filename)

def showAbout():
    messagebox.showinfo("About", "Awesome About Info goes Here Eventually")

def openOnlineHelp():
    webbrowser.open("https://github.com/gerth2/FSMMaker")

def guiInitialDraw():
    gc = FSMConfig()
    root = App.get_running_app().root
    if(root is not None):
        for state in gc.allStates.values():
            state.graphic.initialDraw(root)
        for transition in gc.allTransitions.values():
            transition.graphic.initialDraw(root)

def guiUpdateAll():
    gc = FSMConfig()
    for state in gc.allStates.values():
        state.graphic.update()
    for transition in gc.allTransitions.values():
        transition.graphic.update()


#############################################################3
## MAIN CODE EXECUTION STARTS HERE
#############################################################3

if (__name__ == "__main__"):



    app = FSMMakerApp()


    loadFile("./testConfig.xml")


    FSMMakerApp().run()

