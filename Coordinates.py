#Objects coordinates

class Coord:
    x = None
    y = None
    def __init__(self, position):
        try:
            self.x = position[0]
            self.y = position[1]
        except:
            print ("Invalid input type for position")

    def __add__(self, other):
        p = [self.x + other.x, self.y + other.y]
        return Coord(p)

    def __sub__(self, other):
        p = [self.x - other.x, self.y - other.y]
        return Coord(p)

    def __str__(self):
        return str([self.x, self.y])

    def __eq__(self, other):
        if (self.x == other.x) and (self.y == other.y):
            return True
        else:
            return False
