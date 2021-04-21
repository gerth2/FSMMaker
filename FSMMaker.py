import os
from FSMConfig import FSMConfig
from tkinter import filedialog
from tkinter import messagebox
from tkinter import *
import xml.etree.ElementTree as ET
from string import Template

from Data import Data
from Transition import Transition
from State import State
import webbrowser




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

def donothing():
    pass # Placeholder till we actually implement the thing

def guiDrawLoop():

    root.after(20, guiDrawLoop)

root = Tk()

#############################################################3
## MAIN CODE EXECUTION STARTS HERE
#############################################################3

if (__name__ == "__main__"):
    loadFile("testConfig.xml")
    codegen()
    saveFile("testResavedConfig.xml")

    dflt_canvas_width = 600
    dflt_canvas_height = 800


    root.title("FSM Maker")


    mainCanvas = Canvas(root, 
            width=dflt_canvas_width, 
            height=dflt_canvas_height,
            bg='black')
    mainCanvas.pack()

    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="New", command=reset)
    filemenu.add_command(label="Open", command=guiOpenHandler)
    filemenu.add_command(label="Save", command=guiSaveHandler)
    filemenu.add_command(label="Save As", command=guiSaveAsHandler)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)

    configmenu = Menu(menubar, tearoff=0)
    configmenu.add_command(label="Setup IO", command=donothing)
    configmenu.add_command(label="Edit FSM Properties", command=donothing)
    menubar.add_cascade(label="Config", menu=configmenu)

    buildmenu = Menu(menubar, tearoff=0)
    buildmenu.add_command(label="Codegen Java", command=codegen)
    menubar.add_cascade(label="Build", menu=buildmenu)

    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help Online", command=openOnlineHelp)
    helpmenu.add_command(label="About", command=showAbout)
    menubar.add_cascade(label="Help", menu=helpmenu)


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

    root.config(menu=menubar)

    guiDrawLoop() # Kick off first periodic background draw loop
    mainloop() # Allow normal event loop processing