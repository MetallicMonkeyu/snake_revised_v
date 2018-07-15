#All getters function for information

class Handler:
    game = None

    def __init__(self, game):
        self.game = game

    def get_game_state(self):
        return self.game.game_state

    # Display Info
    def get_width(self):
        return self.game.display.width

    def get_height(self):
        return self.game.display.height

    def get_grid(self):
        return self.game.display.grid

    def get_frame(self):
        return self.game.display

    # Events Listeners:
    def get_mouse_listener(self):
        return self.game.mouse_listener

    def get_keyboard_listener(self):
        return self.game.keyboard_listener

    # Game Entities:
    def get_snake(self):
        return self.game.game_state.snake

    def get_food(self):
        return self.game.game_state.food
