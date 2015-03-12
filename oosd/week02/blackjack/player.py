import re
import hand
import strategy

class Player:

    def __init__(self):
        self.hand = hand.Hand()

    def take_card(self, cd):
        self.hand.add(cd)

    def show_hand(self):
        return str(self.hand) + " Score: " + str(self.hand.score())

    def hits(self):
        return  (raw_input("(h)it or (s)tand: ") == "h")

    def score(self):
        return self.hand.score()


class HousePlayer(Player):

    def __init__(self, current_player):
        Player.__init__(self)
        self.strat = strategy.Strategy(self.hand, current_player)

    def hits(self):
        return self.strat.hit()

    def show_hand_hidden_down(self):
        cards = str(self.hand)
        #replace first card with '**'
        card_to_hide = re.compile("(^\w+)\s")
        return card_to_hide.sub("** ", cards)
