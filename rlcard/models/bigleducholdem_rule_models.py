''' Bigleduc Hold 'em rule model
'''
import rlcard
from rlcard.models.model import Model

class BigleducHoldemRuleAgentV1(object):
    ''' Bigleduc Hold 'em Rule agent version 1
    '''
    def __init__(self):
        self.use_raw = True

    @staticmethod
    def step(state):
        ''' Predict the action when given raw state. A simple rule-based AI.
        Args:
            state (dict): Raw state from the game

        Returns:
            action (str): Predicted action
        '''
        legal_actions = state['raw_legal_actions']
        # Aggressively play 'raise' and 'call'
        if 'raise' in legal_actions:
            return 'raise'
        if 'call' in legal_actions:
            return 'call'
        if 'check' in legal_actions:
            return 'check'
        else:
            return 'fold'

    def eval_step(self, state):
        return self.step(state), []


class BigleducHoldemRuleAgentV2(object):
    ''' Bigleduc Hold 'em Rule agent version 2
    '''
    def __init__(self):
        self.use_raw = True

    @staticmethod
    def step(state):
        ''' Predict the action when given raw state. A simple rule-based AI.
        Args:
            state (dict): Raw state from the game

        Returns:
            action (str): Predicted action
        '''
        legal_actions = state['raw_legal_actions']
        state = state['raw_obs']
        hand = state['hand']
        public_card = state['public_card']
        action = 'fold'
        # When having only 2 hand cards at the game start, choose fold to drop terrible cards
        # Fold all bad hand types to save money
        if public_card:
            if public_card[1] == hand[1]:
                action = 'raise'
            else:
                action = 'fold'
        else:
            if hand[0] in ['J', 'Q', 'K']:
                action = 'raise'
            elif hand[0] == ['8', '9', 'T']:
                action = 'call'
            elif hand[0] == ['5', '6', '7']:
                action = 'check'
            else:
                action = 'fold'

        #return action
        if action in legal_actions:
            return action
        else:
            if action == 'raise':
                return 'call'
            if action == 'check':
                return 'fold'
            if action == 'call':
                return 'raise'
            else:
                return action

    def eval_step(self, state):
        return self.step(state), []


class BigleducHoldemRuleAgentV3(object):
    ''' Bigleduc Hold 'em Rule agent version 3
    '''
    def __init__(self):
        self.use_raw = True

    @staticmethod
    def step(state):
        ''' Predict the action when given raw state. A simple rule-based AI.
        Args:
            state (dict): Raw state from the game

        Returns:
            action (str): Predicted action
        '''
        legal_actions = state['raw_legal_actions']
        # Aggressively play 'raise' and 'call'
        
        if 'check' in legal_actions:
            return 'check'
        if 'call' in legal_actions:
            return 'call'
        if 'raise' in legal_actions:
            return 'raise'
        else:
            return 'fold'

    def eval_step(self, state):
        return self.step(state), []


class BigleducHoldemRuleAgentV4(object):
    ''' Bigleduc Hold 'em Rule agent version 4
    '''
    def __init__(self):
        self.use_raw = True

    @staticmethod
    def step(state):
        ''' Predict the action when given raw state. A simple rule-based AI.
        Args:
            state (dict): Raw state from the game

        Returns:
            action (str): Predicted action
        '''
        legal_actions = state['raw_legal_actions']
        # Aggressively play 'raise' and 'call'
        
        if 'fold' in legal_actions:
            return 'fold'
        if 'check' in legal_actions:
            return 'check'
        if 'call' in legal_actions:
            return 'call'
        else:
            return 'raise'

    def eval_step(self, state):
        return self.step(state), []


class BigleducHoldemRuleAgentV5(object):
    ''' Bigleduc Hold 'em Rule agent version 5
    '''
    def __init__(self):
        self.use_raw = True

    @staticmethod
    def step(state):
        ''' Predict the action when given raw state. A simple rule-based AI.
        Args:
            state (dict): Raw state from the game

        Returns:
            action (str): Predicted action
        '''
        legal_actions = state['raw_legal_actions']
        state = state['raw_obs']
        hand = state['hand']
        public_card = state['public_card']
        action = 'raise'
        # When having only 2 hand cards at the game start, choose fold to drop terrible cards
        # Fold all bad hand types to save money
        if public_card:
            if public_card[1] == hand[1]:
                action = 'raise'
            else:
                if hand[0] in ['T', 'J', 'Q', 'K']:
                    action = 'raise'
                elif hand[0] == ['6', '7', '8', '9']:
                    action = 'call'
                else:
                    action = 'check'
        else:
            if hand[0] in ['T', 'J', 'Q', 'K']:
                action = 'raise'
            elif hand[0] == ['6', '7', '8', '9']:
                action = 'call'
            else:
                action = 'check'

        #return action
        if action in legal_actions:
            return action
        else:
            if action == 'raise':
                return 'call'
            if action == 'check':
                return 'fold'
            if action == 'call':
                return 'raise'
            else:
                return action

    def eval_step(self, state):
        return self.step(state), []


class BigleducHoldemRuleAgentV6(object):
    ''' Bigleduc Hold 'em Rule agent version 6
    '''
    def __init__(self):
        self.use_raw = True

    @staticmethod
    def step(state):
        ''' Predict the action when given raw state. A simple rule-based AI.
        Args:
            state (dict): Raw state from the game

        Returns:
            action (str): Predicted action
        '''
        legal_actions = state['raw_legal_actions']
        state = state['raw_obs']
        hand = state['hand']
        public_card = state['public_card']
        action = 'call'
        # When having only 2 hand cards at the game start, choose fold to drop terrible cards
        # Fold all bad hand types to save money
        if public_card:
            if public_card[1] == hand[1]:
                action = 'raise'
            else:
                if hand[0] in ['Q', 'K']:
                    action = 'raise'
                elif hand[0] == ['8', '9', 'T', 'J']:
                    action = 'call'
                elif hand[0] == ['4', '5', '6', '7']:
                    action = 'check'
                else:
                    action = 'fold'
        else:
            if hand[0] in ['J', 'Q', 'K']:
                action = 'raise'
            elif hand[0] == ['6', '7', '8', '9', 'T']:
                action = 'call'
            elif hand[0] == ['4', '5']:
                action = 'check'
            else:
                action = 'fold'

        #return action
        if action in legal_actions:
            return action
        else:
            if action == 'raise':
                return 'call'
            if action == 'check':
                return 'fold'
            if action == 'call':
                return 'raise'
            else:
                return action

    def eval_step(self, state):
        return self.step(state), []


class BigleducHoldemRuleModelV1(Model):
    def __init__(self):
        env = rlcard.make('bigleduc-holdem')
        rule_agent = BigleducHoldemRuleAgentV1()
        self.rule_agents = [rule_agent for _ in range(env.num_players)]

    @property
    def agents(self):
        return self.rule_agents


class BigleducHoldemRuleModelV2(Model):
    def __init__(self):
        env = rlcard.make('bigleduc-holdem')
        rule_agent = BigleducHoldemRuleAgentV2()
        self.rule_agents = [rule_agent for _ in range(env.num_players)]

    @property
    def agents(self):
        return self.rule_agents


class BigleducHoldemRuleModelV3(Model):
    def __init__(self):
        env = rlcard.make('bigleduc-holdem')
        rule_agent = BigleducHoldemRuleAgentV3()
        self.rule_agents = [rule_agent for _ in range(env.num_players)]

    @property
    def agents(self):
        return self.rule_agents


class BigleducHoldemRuleModelV4(Model):
    def __init__(self):
        env = rlcard.make('bigleduc-holdem')
        rule_agent = BigleducHoldemRuleAgentV4()
        self.rule_agents = [rule_agent for _ in range(env.num_players)]

    @property
    def agents(self):
        return self.rule_agents


class BigleducHoldemRuleModelV5(Model):
    def __init__(self):
        env = rlcard.make('bigleduc-holdem')
        rule_agent = BigleducHoldemRuleAgentV5()
        self.rule_agents = [rule_agent for _ in range(env.num_players)]

    @property
    def agents(self):
        return self.rule_agents


class BigleducHoldemRuleModelV6(Model):
    def __init__(self):
        env = rlcard.make('bigleduc-holdem')
        rule_agent = BigleducHoldemRuleAgentV6()
        self.rule_agents = [rule_agent for _ in range(env.num_players)]

    @property
    def agents(self):
        return self.rule_agents