

from FSMConfig import FSMConfig

class GraphicsMouseManager:

    def __init__(self):
        self.leftDown = False
        self.middleDown = False
        self.rightDown = False
        self.gcLocal = FSMConfig()

        self.prevDragX = None
        self.prevDragY = None
        self.draggedObject = None

    def downHandler(self, event):
        if(event.num == 1):
            self.leftDown = True
            self.prevDragX = event.x
            self.prevDragY = event.y

            for state in self.gcLocal.allStates.values():
                if(state.graphic.checkBodyIntersect(event.x, event.y)):
                    self.draggedObject = state.graphic
                    break

        elif(event.num == 2):
            self.middleDown = True
        elif(event.num == 3):
            self.rightDown = True

        #print("Click! {},{} on {}".format(event.x, event.y, event.num))

    def upHandler(self, event):
        if(event.num == 1):
            self.leftDown = False
            self.prevDragX = None
            self.prevDragY = None
            self.draggedObject = None

        elif(event.num == 2):
            self.middleDown = False
        elif(event.num == 3):
            self.rightDown = False

        #print("Release! {},{} on {}".format(event.x, event.y, event.num))

    def motionHandler(self, event):
        #print("Move! {},{}".format(event.x, event.y))

        for state in self.gcLocal.allStates.values():
            state.graphic.unhighlightBody()
            state.graphic.unhighlightEdge()
        

        if(self.leftDown):
            if(self.draggedObject is not None):
                deltaX = event.x - self.prevDragX
                deltaY = event.y - self.prevDragY
                self.draggedObject.moveBy(deltaX, deltaY)
                self.draggedObject.highlightBody()
                self.prevDragX = event.x
                self.prevDragY = event.y

        else:

            for state in self.gcLocal.allStates.values():
                if(state.graphic.checkBodyIntersect(event.x, event.y)):
                    state.graphic.highlightBody()
                    break

            for state in self.gcLocal.allStates.values():
                if(state.graphic.checkEdgeIntersect(event.x, event.y)):
                    state.graphic.highlightEdge()
                    break
