#Widget features

import tkinter
from tkinter import Canvas
from Timer import Timer


class Widget:

    def __init__(self):
        pass

    def tick(self):
        pass

    def render(self, canvas):
        pass


class Button(Widget):
    # Function Bind
    clicked_action = None

    # Button Property
    color_hover = '#50E4DA'
    color_normal = '#4FBAB3'
    color_text = '#FFFFFF'
    font = ("Comic Sans MS", '16')

    # Status
    hover = False
    trigger = False

    def __init__(self, x, y, width, height, text = None, handler = None):
        self.handler = handler
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    # Function Bind:
    def bind(self, method_handler):
        self.clicked_action = method_handler

    # Button Config
    def set_text(self, text):
        assert isinstance(text, str)
        self.text = text

    # Button Action:
    def tick(self):
        self.check_hover()
        self.check_trigger()

    def render(self, canvas):
        assert isinstance(canvas, Canvas)
        if self.hover:
            canvas.create_rectangle(
                self.x,
                self.y,
                self.x + self.width,
                self.y + self.height,
                outline = '',
                fill=self.color_hover
            )
            canvas.create_text(
                self.x + self.width / 2,
                self.y + self.height / 2,
                text=self.text,
                font=self.font,
                fill=self.color_text
            )
        else:
            canvas.create_rectangle (
                self.x,
                self.y,
                self.x + self.width,
                self.y + self.height,
                fill=self.color_normal,
                outline=''
            )
            canvas.create_text (
                self.x + self.width / 2,
                self.y + self.height / 2,
                text=self.text,
                font=self.font,
                fill=self.color_text
            )

    # Methods:
    def check_hover(self):
        if (self.handler.get_mouse_listener().x!=None):
            if (self.x < self.handler.get_mouse_listener().x < self.x + self.width) \
                    and (self.y < self.handler.get_mouse_listener().y < self.y + self.height):
                self.hover = True
            else:
                self.hover = False

    def check_trigger(self):
        if (self.handler.get_mouse_listener().x_click!=None):
            if (self.x < self.handler.get_mouse_listener().x_click < self.x + self.width)\
                    and (self.y < self.handler.get_mouse_listener().y_click < self.y + self.height):
                if self.clicked_action is None:
                    print ("The {0} button doesn't bind to any method".format(self.text))
                    self.handler.get_mouse_listener().clear_mouse_click()
                    return
                self.handler.get_mouse_listener().clear_mouse_click()
                self.clicked_action()


class Label(Widget):
    # Constants
    UP = tkinter.N
    DOWN = tkinter.S
    LEFT = tkinter.W
    RIGHT = tkinter.E
    CENTER = tkinter.CENTER

    # Properties
    handler = None
    x = 0
    y = 0
    text = ''

    # Styles
    font = None
    color_text = '#FFFFFF'
    anchor_point = CENTER

    def __init__(self, x, y, text, size=20, style='', handler=None):
        self.handler = handler
        self.x = x
        self.y = y
        self.text = text
        self.font = ("Comic Sans MS", str(size), style)

    def tick(self):
        pass

    def render(self, canvas):
        canvas.create_text(
            self.x,
            self.y,
            text=self.text,
            font=self.font,
            fill=self.color_text,
            anchor = self.anchor_point)

    # Label Config
    def set_text (self, text):
        assert isinstance(text, str)
        self.text = text

    def set_color(self, color):
        assert isinstance(color, str)
        self.color_text = color

    def set_anchor(self, anchor):
        self.anchor_point = anchor


class BubbleLabel(Widget):
    handler = None
    container = None
    # Properties
    x = 0
    y = 0
    text = ''
    speed = 1

    # Styles
    font = None
    color_text = '#FF7C96'

    # Timers
    death_timer = None
    tick_timer = None

    def __init__(self, container, x, y, text, size=20, style='', handler=None):
        self.handler = handler
        assert isinstance(container, list)
        self.container = container
        self.container.append(self)
        # Text Properties and Styles
        self.x = x
        self.y = y
        self.text = text
        self.font = ("Comic Sans MS", str(size), style)
        # Timers
        self.death_timer = Timer(400)
        self.tick_timer = Timer(20)

    def tick(self):
        if self.tick_timer.triggered():
            self.y -= self.speed
            self.speed += 1
        if self.death_timer.triggered():
            del self.container[self.container.index(self)]

    def render(self, canvas):
        canvas.create_text(
            self.x,
            self.y,
            text=self.text,
            font=self.font,
            fill=self.color_text,
        )
