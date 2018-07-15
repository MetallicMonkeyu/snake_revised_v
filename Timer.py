#Feature to show game time

from time import *


class Timer:
    time_base = 0
    current_time = None
    last_time = None

    def __init__(self, time):
        self.time_base = time

    def tick(self):
        self.current_time = int(round(time() * 1000))
        if self.last_time is None:
            self.last_time = self.current_time

    def triggered(self):
        self.tick()
        if (self.current_time - self.last_time) >= self.time_base:
            self.last_time = self.current_time
            return True
        else:
            return False

    def set_time_base(self, value):
        self.time_base = value

    def get_time_base(self):
        return self.time_base
