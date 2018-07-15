#Scoring information
class Player:
    score = 0

    def __init__(self):
        self.score = 0

    def increment_score(self, val):
        self.score += val

    # Setters / Getters
    def get_score(self):
        return self.score

    def set_score(self, score):
        self.score = score
