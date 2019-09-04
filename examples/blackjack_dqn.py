# Example of using doudizhu environment
import rlcard
from rlcard.agents.agent import DQNAgent
import tensorflow as tf


# make environment
env = rlcard.make('blackjack')

print('############## Environment of Blackjack Initilized ################')

with tf.Session() as sess:
    config = 'test'
    # set agents
    agent_0 = DQNAgent(config, sess)
#env.set_agents([agent_0])

# seed everything
#env.set_seed(0)
#agent_0.set_seed(0)

#wins = 0

#env.init_game()
#state, player = env.init_game()
#print(state, player)
#action = agent_0.step(state)
#state, player = env.step(action)
#print(state, player)
#print(env.step_back())
#print(env.step_back())
#for _ in range(10):
#	# TODO: add multi-process
#
#        
#        # generate data from the environment
#        trajectories, payoffs = env.run()
#        print(trajectories)
#        print(payoffs)
#        wins += payoffs[0]
#
#        # Update agents here

#print(wins)