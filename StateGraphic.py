from GraphicsUtils import round_rectangle, update_rectangle_coords
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty

class StateGraphic(Widget):

    def __init__(self, stateParent):
        self.stateParent = stateParent

        self.TEXT_MARGIN_H = 35
        self.TEXT_MARGIN_V = 15

        super().__init__()

    def initialDraw(self, rootIn):
        rootIn.add_widget(self)

    def update(self):
        pass

    def parseCfg(self, etreeNode):
        for child in etreeNode:
            if(child.tag == "x1"):
                self.set_center_x(int(child.text))
            elif(child.tag == "width"):
                self.size[0] = int(child.text)
            elif(child.tag == "y1"):
                self.set_center_y(int(child.text))
            elif(child.tag == "height"):
               self.size[1] = int(child.text)

    def highlightBody(self):
        pass

    def unhighlightBody(self):
        pass

    def highlightEdge(self):
        pass

    def unhighlightEdge(self):
        pass

    def checkBodyIntersect(self, x, y):
        inX = (x > self.x1) and (x < (self.x1 + self.width))
        inY = (y > self.y1) and (y < (self.x1 + self.height))
        return inX and inY

    def checkEdgeIntersect(self, x, y):
        pass

    def moveBy(self, deltaX, deltaY):
        self.x1 += deltaX
        self.y1 += deltaY
        self.update()
