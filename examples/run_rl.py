''' An example of training a reinforcement learning agent on the environments in RLCard
'''
import os
import argparse

import torch

import rlcard
from rlcard import models
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
    
    if not args.selfplay:
        assert args.opponent != None
        agents.pop()
        agent = models.load(args.opponent).agents[1]
        agents.append(agent)
    env.set_agents(agents)

    # Start training
    with Logger(args.log_dir) as logger:
        for episode in range(args.num_episodes):

            if args.algorithm == 'nfsp':
                if args.selfplay:
                    for agent_ in agents:
                        agent_.sample_episode_policy()
                else:
                    agents[0].sample_episode_policy()

            # Generate data from the environment
            trajectories, payoffs = env.run(is_training=True)

            # Reorganaize the data to be state, action, reward, next_state, done
            trajectories = reorganize(trajectories, payoffs)

            # Feed transitions into agent memory, and train the agent
            # Here, we assume that DQN always plays the first position
            # and the other players play randomly (if any)
            if args.selfplay:
                for i in range(env.num_players):
                    for ts in trajectories[i]:
                        agents[i].feed(ts)
            else:
                for ts in trajectories[0]:
                    agents[0].feed(ts)

            # Evaluate the performance. Play with random agents.
            if episode % args.evaluate_every == 0:
                logger.log_performance(
                    episode,
                    tournament(
                        env,
                        args.num_eval_games,
                    )
                )
    # Get the paths
    csv_path, fig_path = logger.csv_path, logger.fig_path
    # Plot the learning curve
    plot_curve(csv_path, fig_path, args.algorithm)
    
    for i in range(env.num_players):
        # Save model
        save_path = os.path.join(args.log_dir, f'{i}_model.pth')
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
        default='dqn',
        # default='nfsp',
        choices=[
            'dqn',
            'nfsp',
        ],
    )
    parser.add_argument(
        '--selfplay',
        type=bool,
        default=False,
    )
    parser.add_argument(
        '--opponent',
        type=str,
        default="bigleduc-holdem-rule-v1",
        choices=[
            "bigleduc-holdem-rule-v1",
            "bigleduc-holdem-rule-v2",
            "bigleduc-holdem-rule-v3",
            "bigleduc-holdem-rule-v4",
            "bigleduc-holdem-rule-v5",
            "bigleduc-holdem-rule-v6",
        ]
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
        default=100000,
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
        # default='experiments/bigleduc_holdem_nfsp_result/',
        default='experiments/bigleduc_holdem_dqn_vs_rulev1/',
        # default='experiments/bigleduc_holdem_dqn_vs_rulev2/',
        # default='experiments/bigleduc_holdem_dqn_vs_rulev3/',
        # default='experiments/bigleduc_holdem_dqn_vs_rulev4/',
        # default='experiments/bigleduc_holdem_dqn_vs_rulev5/',
        # default='experiments/bigleduc_holdem_dqn_vs_rulev6/',
    )

    args = parser.parse_args()

    os.environ["CUDA_VISIBLE_DEVICES"] = args.cuda
    train(args)

