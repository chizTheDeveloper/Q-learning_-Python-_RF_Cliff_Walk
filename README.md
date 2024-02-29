**CST8509 Lab3 Gymnasium**
Overview
This repository contains completed tasks for the CST8509 Lab3 on Gymnasium. Gymnasium, successor to OpenAI Gym, provides a standard API for Reinforcement Learning Environments. In this lab exercise, we implement a custom Gymnasium environment for the CliffWalking environment and evaluate a selection of Stable-Baselines3 algorithms in that environment.

-**Tasks Completed**
  -Implement gym_examples/GridWorld-v0

 -Modified the existing custom PyGame-enabled Gymnasium environment gym_examples/GridWorld-v0 to create a new environment aisd_examples/AISDCliffWalking-v0.
  Trial run with gym_examples/GridWorld-v0

 -Executed a trial run with a "null agent" using the provided code snippet to visualize the GridWorld environment.
  Modify gym_examples/GridWorld-v0 to CliffWalker

 -Made necessary modifications to transform the 5x5 grid of GridWorld-v0 into a 12x4 grid environment named CliffWalker.

-Integrated the environment with the *rl.py Q-Learning agent from Lab2, incorporating code to calculate the number of states and handle Box return values.
 Use your environment with Stable-Baselines3

-Installed Stable-Baselines3 in the virtual environment and adapted code to use the GridWorld-v0 environment. Tested the environment with DQN and PPO algorithms.

**Instructions for Execution**
 -Clone this repository to your local machine.
 -Follow the instructions provided in each task to execute the corresponding code and complete the lab exercise.
 -Ensure all dependencies are installed in your environment, including Stable-Baselines3.
 -Execute the Python files provided to observe the functionality of the Gymnasium environment with the implemented changes.
