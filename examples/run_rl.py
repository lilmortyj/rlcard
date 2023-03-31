''' An example of training a reinforcement learning agent on the environments in RLCard
'''
import os
import argparse

import torch

import rlcard
from rlcard.agents import RandomAgent
from rlcard.utils import (
    get_device,
    set_seed,
    tournament,
    reorganize,
    Logger,
    plot_curve,
)

def train(args):

    # Check whether gpu is available
    device = get_device()
        
    # Seed numpy, torch, random
    set_seed(args.seed)

    # Make the environment with seed
    env = rlcard.make(
        args.env,
        config={
            'seed': args.seed,
        }
    )

    agents = []
    for _ in range(env.num_players):
        # Initialize the agent and use random agents as opponents
        if args.algorithm == 'dqn':
            from rlcard.agents import DQNAgent
            agent = DQNAgent(
                num_actions=env.num_actions,
                state_shape=env.state_shape[0],
                mlp_layers=[64,64],
                device=device,
            )
        elif args.algorithm == 'nfsp':
            from rlcard.agents import NFSPAgent
            agent = NFSPAgent(
                num_actions=env.num_actions,
                state_shape=env.state_shape[0],
                hidden_layers_sizes=[64,64],
                q_mlp_layers=[64,64],
                device=device,
            )
        agents.append(agent)
        
    env.set_agents(agents)

    loggers = [Logger(os.path.join(args.log_dir, str(k))) for k in range(env.num_players)]
    for i in range(env.num_players):
        loggers[i] = loggers[i].__enter__()
    
    # Start training
    for episode in range(args.num_episodes):

        if args.algorithm == 'nfsp':
            for agent_ in agents:
                agent_.sample_episode_policy()

        # Generate data from the environment
        trajectories, payoffs = env.run(is_training=True)

        # Reorganaize the data to be state, action, reward, next_state, done
        trajectories = reorganize(trajectories, payoffs)

        # Feed transitions into agent memory, and train the agent
        # Here, we assume that DQN always plays the first position
        # and the other players play randomly (if any)
        for i in range(env.num_players):
            for ts in trajectories[i]:
                agents[i].feed(ts)

        # Evaluate the performance. Play with random agents.
        if episode % args.evaluate_every == 0:
            result = tournament(
                env,
                args.num_eval_games,
            )
            for i in range(env.num_players):
                loggers[i].log_performance(
                    episode,
                    result[i]
                )

    for i in range(env.num_players):
        loggers[i].__exit__(None, None, None)
        
        # Get the paths
        csv_path, fig_path = loggers[i].csv_path, loggers[i].fig_path

        # Plot the learning curve
        plot_curve(csv_path, fig_path, args.algorithm)

        # Save model
        save_path = os.path.join(os.path.join(args.log_dir, str(i)), 'model.pth')
        torch.save(agents[i], save_path)
        print('Model saved in', save_path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser("DQN/NFSP example in RLCard")
    parser.add_argument(
        '--env',
        type=str,
        default='bigleduc-holdem',
        choices=[
            'blackjack',
            'leduc-holdem',
            'bigleduc-holdem',
            'limit-holdem',
            'doudizhu',
            'mahjong',
            'no-limit-holdem',
            'uno',
            'gin-rummy',
            'bridge',
        ],
    )
    parser.add_argument(
        '--algorithm',
        type=str,
        # default='dqn',
        default='nfsp',
        choices=[
            'dqn',
            'nfsp',
        ],
    )
    parser.add_argument(
        '--cuda',
        type=str,
        default='3',
    )
    parser.add_argument(
        '--seed',
        type=int,
        default=42,
    )
    parser.add_argument(
        '--num_episodes',
        type=int,
        default=500000,
    )
    parser.add_argument(
        '--num_eval_games',
        type=int,
        default=2000,
    )
    parser.add_argument(
        '--evaluate_every',
        type=int,
        default=1000,
    )
    parser.add_argument(
        '--log_dir',
        type=str,
        # default='experiments/bigleduc_holdem_dqn_result/',
        default='experiments/bigleduc_holdem_nfsp_result/',
    )

    args = parser.parse_args()

    os.environ["CUDA_VISIBLE_DEVICES"] = args.cuda
    train(args)

