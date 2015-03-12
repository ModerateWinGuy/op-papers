import hand


class Strategy():

    def __init__(self, start_hand, current_player):
        self.current_player = current_player
        self.hand = start_hand
        self.current_strat = 1

    def hit(self):
        run = {self.strat_one, self.strat_two}

    def strat_one(self):
        if self.hand.score < 17:
            return True
        else:
            return False

    def strat_two(self):
        if self.hand.score < 17 and self.current_player.score > self.hand.score:
            return True
        else:
            return False