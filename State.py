#State information (revised version)

from Widgets import *
from GameEntities import *
from Player import *


class MenuState:
    # Widgets:
    start_button = None
    game_title = None
    # handler:
    handler = None

    def __init__(self, hanlder):
        self.handler = hanlder
        # Restart Button
        button_width = 120
        button_height = 33
        frame = self.handler.get_frame()

        self.start_button = Button(
            x = frame.width/2 - button_width/2,
            y = frame.height/2,
            width = button_width,
            height = button_height,
            text = "Start",
            handler = self.handler
        )
        self.start_button.bind(self.handler.game.set_game_state)

        self.game_title = Label(
            x = frame.width/2,
            y = int(frame.height * 0.37),
            size = 35,
            style = 'bold',
            text = "Test Snake Game",
        )
        self.game_title.set_color("#FFC579")

    def tick(self):
        self.start_button.tick()
        self.game_title.tick()

    def render(self, canvas):
        self.start_button.render(canvas)
        self.game_title.render(canvas)


class GameState:
    # Handler
    handler = None

    # Game Infos
    player = None

    # Game Entities
    snake = None
    food = None

    # GUI widgets
    score_label = None
    score_render = None
    effects_container = []

    # Timers
    MIN_SPEED = 90
    MAX_SPEED = 40
    SPEED_STEP = int ((MIN_SPEED - MAX_SPEED) / 10.0)
    speed_controller = None

    def __init__(self, handler):
        print ("<Game State> Init")
        self.handler = handler
        self.player = Player()
        self.snake = Snake(self.handler)
        self.food = Food(self.handler, self.snake)

        self.speed_controller = Timer(self.MIN_SPEED)
        self.init_gui()

    def init_gui(self):
        frame = self.handler.get_frame()
        self.score_label = Label(
            x = int(frame.width * 0.02),
            y = int(frame.height * 0.04),
            size = 20,
            style = 'bold',
            text = "Score: ",
        )
        self.score_label.set_anchor(Label.LEFT)
        self.score_label.set_color("#A5FF9B")

        self.score_render = Label(
            x=int(frame.width * 0.02 + 80),
            y=int(frame.height * 0.04),
            size=20,
            style='bold',
            text="0",
        )
        self.score_label.set_anchor(Label.LEFT)
        self.score_render.set_color("#EBFF97")

    def tick(self):
        if self.speed_controller.triggered():
            if self.snake is not None:
                self.snake.tick()
            if self.food is not None:
                self.food.tick()
        self.score_label.tick()
        self.score_render.tick()
        for e in self.effects_container:
            assert isinstance(e, Widget)
            e.tick()

    def render(self, canvas):
        if self.snake is not None:
            self.snake.render(canvas)
        if self.food is not None:
            self.food.render(canvas)
        self.score_label.render(canvas)
        self.score_render.render(canvas)
        for e in self.effects_container:
            assert isinstance(e, Widget)
            e.render(canvas)

    # Game Events:
    def get_score_event(self):
        self.food = Food(self.handler, self.snake)
        self.player.increment_score(1)
        self.score_render.set_text(str(self.player.get_score()))
        # Generate Get Score Effect
        BubbleLabel(
            container = self.effects_container,
            x = self.snake.head_position().x * self.handler.get_grid(),
            y = int (self.snake.head_position().y * self.handler.get_grid() * 0.95),
            text = '+1',
            size = 25,
            style = 'bold'
        )
        # Increase Speed
        new_speed = self.speed_controller.get_time_base() - self.SPEED_STEP
        if new_speed >= self.MAX_SPEED:
            print ("Speed Increased!")
            self.speed_controller.set_time_base(new_speed)

    def __del__(self):
        print ("<Game State> Destroyed")


class OverState:
    # Handler
    handler = None

    def __init__(self, handler):
        self.handler = handler
        button_width = 120
        button_height = 33
        frame = self.handler.get_frame()

        self.menu_button = Button(
            x = frame.width/2 - button_width/2,
            y = frame.height/2 - button_height/2,
            width = button_width,
            height = button_height,
            text = "Menu",
            handler = self.handler
        )
        self.menu_button.bind(self.handler.game.set_menu_state)

        self.restart_button = Button(
            x = frame.width/2 - button_width/2,
            y = frame.height/2 + button_height,
            width = button_width,
            height = button_height,
            text = "Restart",
            handler = self.handler
        )
        self.restart_button.bind(self.handler.game.set_game_state)

        self.game_over_title = Label(
            x = frame.width/2,
            y = int(frame.height * 0.37),
            size = 35,
            style = 'bold',
            text = "Game Over",
        )
        self.game_over_title.set_color("#FF83AD")

    def tick(self):
        self.menu_button.tick()
        self.restart_button.tick()
        self.game_over_title.tick()

    def render(self, canvas):
        self.menu_button.render(canvas)
        self.restart_button.render(canvas)
        self.game_over_title.render(canvas)
