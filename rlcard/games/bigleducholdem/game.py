import numpy as np
from copy import copy

from rlcard.games.bigleducholdem import Dealer
from rlcard.games.bigleducholdem import Player
from rlcard.games.bigleducholdem import Judger
from rlcard.games.bigleducholdem import Round

from rlcard.games.leducholdem import Game

class BigleducholdemGame(Game):

    def __init__(self, allow_step_back=False, num_players=2):
        ''' Initialize the class bigleducholdem Game
        '''
        self.allow_step_back = allow_step_back
        self.np_random = np.random.RandomState()
        ''' No big/small blind
        # Some configarations of the game
        # These arguments are fixed in Leduc Hold'em Game

        # Raise amount and allowed times
        self.raise_amount = 2
        self.allowed_raise_num = 2

        self.num_players = 2
        '''
        # Some configarations of the game
        # These arguments can be specified for creating new games

        # Small blind and big blind
        self.small_blind = 1
        self.big_blind = 2 * self.small_blind

        # Raise amount and allowed times
        self.raise_amount = self.big_blind
        self.allowed_raise_num = 6

        self.num_players = num_players
