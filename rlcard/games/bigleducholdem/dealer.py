from rlcard.games.base import Card
from rlcard.games.limitholdem import Dealer

class BigleducholdemDealer(Dealer):

    def __init__(self, np_random):
        ''' Initialize a bigleducholdem dealer class
        '''
        self.np_random = np_random
        self.deck = [
            Card('S', '2'), Card('H', '2'),
            Card('S', '3'), Card('H', '3'),
            Card('S', '4'), Card('H', '4'),
            Card('S', '5'), Card('H', '5'),
            Card('S', '6'), Card('H', '6'),
            Card('S', '7'), Card('H', '7'),
            Card('S', '8'), Card('H', '8'),
            Card('S', '9'), Card('H', '9'),
            Card('S', 'T'), Card('H', 'T'),
            Card('S', 'J'), Card('H', 'J'),
            Card('S', 'Q'), Card('H', 'Q'),
            Card('S', 'K'), Card('H', 'K'),
            ]
        self.shuffle()
        self.pot = 0
