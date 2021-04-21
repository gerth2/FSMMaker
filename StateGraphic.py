from GraphicsUtils import round_rectangle, update_rectangle_coords

class StateGraphic:

    def __init__(self, parent):
        self.parent = parent
        self.x1 = 10
        self.y1 = 10
        self.x2 = 50
        self.y2 = 50
        self.TEXT_MARGIN_H = 35
        self.TEXT_MARGIN_V = 15
        self.canvas = None

    def initialDraw(self, canvas_in):
        self.canvas = canvas_in
        self.rect = round_rectangle(self.canvas, self.x1, self.y1, self.x2, self.y2, fill="black", outline="white", width=2) 
        self.nameTxt = self.canvas.create_text(self.x1+self.TEXT_MARGIN_H , self.y1+self.TEXT_MARGIN_V , text=self.parent.name, fill="white")        

    def update(self):
        update_rectangle_coords(self.canvas, self.rect, self.x1, self.y1, self.x2, self.y2)
        self.canvas.itemconfigure(self.nameTxt, text=self.parent.name)
        self.canvas.coords(self.nameTxt, self.x1+self.TEXT_MARGIN_H , self.y1+self.TEXT_MARGIN_V )

    def parseCfg(self, etreeNode):
        for child in etreeNode:
            if(child.tag == "x1"):
                self.x1 = int(child.text)
            elif(child.tag == "x2"):
                self.x2 = int(child.text)
            elif(child.tag == "y1"):
                self.y1 = int(child.text)
            elif(child.tag == "y2"):
                self.y2 = int(child.text)

    def highlightBody(self):
        self.canvas.itemconfigure(self.rect, fill="#333")

    def unhighlightBody(self):
        self.canvas.itemconfigure(self.rect, fill="#000")

    def highlightEdge(self):
        self.canvas.itemconfigure(self.rect, width=6)

    def unhighlightEdge(self):
        self.canvas.itemconfigure(self.rect, width=2)

    def checkBodyIntersect(self, x, y):
        inX = (x > self.x1) and (x < self.x2)
        inY = (y > self.y1) and (y < self.y2)
        return inX and inY

    def checkEdgeIntersect(self, x, y):
        inX = (x > self.x1) and (x < self.x2)
        inY = (y > self.y1) and (y < self.y2)
        nearTop = abs(y - self.y1) < 7 and inX
        nearBottom = abs(y - self.y2) < 7 and inX
        nearLeft = abs(x - self.x1) < 7 and inY
        nearRight = abs(x - self.x2) < 7 and inY
        return nearTop or nearBottom or nearLeft or nearRight

    def moveBy(self, deltaX, deltaY):
        self.x1 += deltaX
        self.x2 += deltaX
        self.y1 += deltaY
        self.y2 += deltaY
        self.update()
