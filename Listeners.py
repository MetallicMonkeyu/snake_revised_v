#Controller for keyboard and mouse

import tkinter


class KeyboardListener:
    # Handler:
    handler = None
    key_trigger_action_queue = []

    def __init__(self, handler):
        self.handler = handler

    def bind(self, method):
        self.key_trigger_action_queue.append(method)

    def key_pressed(self, event):
        print ("Key pressed: {0}".format(event.keysym))
        for action in self.key_trigger_action_queue:
            action(event.keysym)

class MouseListener:
    x = None
    y = None
    x_click = None
    y_click = None

    def __init__(self):
        pass

    def mouse_moved(self, event):
        self.x = event.x
        self.y = event.y

    def mouse_clicked(self, event):
        self.x_click = event.x
        self.y_click = event.y

    def clear_mouse_click(self):
        self.x_click = None
        self.y_click = None
