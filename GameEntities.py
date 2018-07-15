#Game required objects established

from Coordinates import Coord
from random import *
from EntityRenders import *


# Enum
class DIR:
    UP = "Up"
    DOWN = "Down"
    LEFT = "Left"
    RIGHT = "Right"


# Entities
class Food:
    position = None
    handler = None
    color_assets = ('#FFFD98', '#FF8BA3', '#97FF8B')
    color = None

    def __init__(self, handler, snake):
        self.handler = handler
        while True:
            self.position = self.gen_food()
            if self.position not in snake.body:
                break
        self.color = self.color_assets[randint(0, len(self.color_assets) - 1)]

    def tick(self):
        pass

    def render(self, canvas):
        grid = self.handler.get_grid()
        canvas.create_oval(
            self.position.x * grid,
            self.position.y * grid,
            self.position.x * grid + grid,
            self.position.y * grid + grid,
            outline = '',
            fill = self.color,
        )

    def gen_food(self):
        x = int(random() * (self.handler.get_width() / self.handler.get_grid()))
        y = int(random() * (self.handler.get_height() / self.handler.get_grid()))
        return Coord([x, y])

    def __del__(self):
        print ("[Food] Destroyed")


class Snake:
    body = None
    direction = DIR.RIGHT
    # Handler
    handler = None
    # Status
    dir_changed = False
    # Renderer
    renderer = None

    def __init__(self, handler):
        self.handler = handler
        self.body = [Coord([0,0]), Coord([1,0]), Coord([2,0])]
        self.renderer = SnakeRenderer()
        handler.get_keyboard_listener().bind(self.change_direction)

    def tick(self):
        self.move()
        self.grow()
        print ("Head: " + str(self.head_position()))
        self.allow_direction_change()
        self.check_game_over()

    def render(self, canvas):
        grid = self.handler.get_grid()
        """
        for part in self.body:
            canvas.create_oval(
                part.x * grid,
                part.y * grid,
                part.x * grid + grid,
                part.y * grid + grid,
                fill = "#FFFFFF"
            )
        """
        self.renderer.render(self.body, canvas, grid)

    def move(self):
        if self.direction == DIR.RIGHT:
            move = [1, 0]
        elif self.direction == DIR.LEFT:
            move = [-1, 0]
        elif self.direction == DIR.UP:
            move = [0, -1]
        else:
            move = [0, 1]
        self.body.append(self.body[-1] + Coord(move))

    def grow(self):
        if not(self.body[-1] == self.handler.get_food().position):
            del self.body[0]
        else:
            # Get Score Event
            self.handler.get_game_state().get_score_event()

    def check_game_over(self):
        x_max = self.handler.get_width() / self.handler.get_grid()
        y_max = self.handler.get_height() / self.handler.get_grid()
        if self.body[-1] in self.body[0:len(self.body)-1]:
            self.handler.game.set_over_state()
        if self.body[-1].x < 0 or self.body[-1].x >= x_max or self.body[-1].y < 0 or self.body[-1].y >= y_max:
            self.handler.game.set_over_state()

    # Events Methods:
    def change_direction(self, direction):
        # Debugging:
        print ("[Snake] In change_direction method")
        if self.dir_changed:
            # print "[Snake] Already changed, return"
            return
        if (direction == DIR.UP) and (self.direction != DIR.UP) and (self.direction != DIR.DOWN):
            # print "[Snake] Direction changed to {0}".format(direction)
            self.direction = DIR.UP
            self.dir_changed = True
        elif (direction == DIR.DOWN) and (self.direction != DIR.UP) and (self.direction != DIR.DOWN):
            # print "[Snake] Direction changed to {0}".format(direction)
            self.direction = DIR.DOWN
            self.dir_changed = True
        elif (direction == DIR.LEFT) and (self.direction != DIR.RIGHT) and (self.direction != DIR.LEFT):
            # print "[Snake] Direction changed to {0}".format(direction)
            self.direction = DIR.LEFT
            self.dir_changed = True
        elif (direction == DIR.RIGHT) and (self.direction != DIR.RIGHT) and (self.direction != DIR.LEFT):
            # print "[Snake] Direction changed to {0}".format(direction)
            self.direction = DIR.RIGHT
            self.dir_changed = True

    def allow_direction_change(self):
        self.dir_changed = False

    def head_position(self):
        return self.body[-1]

    def __del__(self):
        print ("[Snake] Destroyed")


