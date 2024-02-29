# changes Made:
# Added reward to display
# Accumulate the reward 
# tracked the fasted episode so far in realtime

from medium_qlearning_env import Env
import numpy as np
import time
import os

# create environment
env = Env()

# QTable : contains the Q-Values for every (state,action) pair
qtable = np.random.rand(env.stateCount, env.actionCount).tolist()

# hyperparameters
episode = 50
gamma = 0.1
epsilon = 0.08
decay = 0.1

# Initialize variables to track the fastest episode
fastest_episode = 0
fastest_steps = float('inf')

# training loop
for i in range(episode): #changed epoches to episode
    state, reward, done = env.reset()
    steps = 0
    total_reward = 0#Added reward to display

    while not done:
        os.system('cls')
        print("episode #", i + 1, "/", episode)
        env.render()
        time.sleep(0.05)

        steps += 1

        # act randomly sometimes to allow exploration
        if np.random.uniform() < epsilon:
            action = env.randomAction()
        # if not select max action in Qtable (act greedy)
        else:
            action = qtable[state].index(max(qtable[state]))

        # take action
        next_state, reward, done = env.step(action)

        # update qtable value with Bellman equation   
        qtable[state][action] = reward + gamma * max(qtable[next_state])
        total_reward += reward  # Accumulate the reward

        # update state
        state = next_state

    epsilon -= decay * epsilon

 # Check if the current episode is faster than the previous fastest
    if steps < fastest_steps:
        fastest_steps = steps
        fastest_episode = i + 1

    #Printetd out steps and return
    print("\nDone in", steps, "steps.")
    print("\nFastest Episode #", fastest_episode, "with a total of", fastest_steps,"steps  taken")
    print("Total Return:", total_reward)
    time.sleep(0.8)