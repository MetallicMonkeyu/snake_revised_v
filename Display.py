from tkinter import *

from Listeners import *

#Initiate Frame
class GameFrame:
    # Root Frame:
    root = Tk()
    height = 600
    width = 800
    grid = 20
    # Canvas
    canvas = None

    def __init__(self):
        # Root Init:
        self.root.wm_title("Test Snake")
        # Canvas Init:
        self.canvas = Canvas (
            self.root,
            height = self.height,
            width = self.width,
            bg='#545454',
            borderwidth=0,
            highlightthickness=0
        )
        self.canvas.pack()

    def clear_canvas(self):
        self.canvas.delete(ALL)


