from rlcard.utils.utils import rank2int
from rlcard.games.leducholdem import Judger

class BigleducholdemJudger(Judger):
    ''' The Judger class for Bigleduc Hold'em
    '''
    def __init__(self, np_random):
        ''' Initialize a judger class
        '''
        super(BigleducholdemJudger, self).__init__(np_random)
