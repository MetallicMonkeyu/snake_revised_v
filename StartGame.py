#Game starter
#starting notice: Tkinter for python2, tkinter for python3

from Display import GameFrame
from State import *
from threading import *
from Handler import Handler
from Listeners import *


class StartGame:
    # Display:
    display = None
    # GameState:
    menu_state = None
    game_state = None
    over_state = None
    current_state = None
    # Running:
    thread = None
    running = False
    # Handler:
    handler = None
    # Evens Listeners:
    mouse_listener = None
    keyboard_listener = None

    def __init__(self):
        self.display = GameFrame()
        # Handler
        self.handler = Handler(self)
        # Events Listeners:
        self.init_listeners()
        # GameState
        self.menu_state = MenuState(self.handler)
        self.game_state = GameState(self.handler)
        self.over_state = OverState(self.handler)
        # Thread
        self.thread = Thread(target=self.run)

    def set_menu_state(self):
        self.current_state = self.menu_state

    def set_game_state(self):
        self.game_state.__init__(self.handler)
        self.current_state = self.game_state

    def set_over_state(self):
        self.current_state = self.over_state

    # Thread Control
    def start(self):
        if not self.running:
            self.running = True
            self.thread.start()

    def stop(self):
        if self.running:
            self.running = False
            self.thread.join()

    def run(self):
        self.tick()
        self.render(self.display.canvas)
        if self.running:
            self.display.root.after(5, self.run)

    # Game Control
    def tick(self):
        if self.current_state is None:
            return
        self.current_state.tick()

    def render(self, canvas):
        if self.current_state is None:
            return
        self.display.clear_canvas()
        self.current_state.render(canvas)

    # Events Control
    def init_listeners(self):
        self.mouse_listener = MouseListener()
        self.display.root.bind("<Motion>", self.mouse_listener.mouse_moved)
        self.display.root.bind("<Button-1>", self.mouse_listener.mouse_clicked)

        self.keyboard_listener = KeyboardListener(self.handler)
        self.display.root.bind("<Key>", self.keyboard_listener.key_pressed)

game = StartGame()
game.set_menu_state()
game.start()
game.display.root.mainloop()
