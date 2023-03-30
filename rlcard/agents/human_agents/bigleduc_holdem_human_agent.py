from rlcard.agents import LeducholdemHumanAgent


class HumanAgent(LeducholdemHumanAgent):
    ''' A human agent for Bigleduc Holdem. It can be used to play against trained models
    '''

    def __init__(self, num_actions):
        ''' Initilize the human agent

        Args:
            num_actions (int): the size of the ouput action space
        '''
        super(HumanAgent, self).__init__(num_actions)