

class TransitionGraphic:

    def __init__(self, parent):
        self.parent = parent
        self.startAttachAngle = 0 # Angle on the starting node where this line is supposed to attach
        self.endAttachAngle = 0 # Angle on the ending node where this line is supposed to attach


    def initialDraw(self, canvas):
        pass

    def update(self):
        pass

    def parseCfg(self, etreeNode):
        pass