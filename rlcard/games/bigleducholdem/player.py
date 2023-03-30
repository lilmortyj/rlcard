from rlcard.games.leducholdem import Player

class BigleducholdemPlayer(Player):

    def __init__(self, player_id, np_random):
        ''' Initilize a player.

        Args:
            player_id (int): The id of the player
        '''
        super(BigleducholdemPlayer, self).__init__(player_id, np_random)