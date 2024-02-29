import numpy as np

# changes Made:
# - Added Cliff attribute to indicate if the agent fell over the cliff
# - implemented reward system
# - Set Negative reward for falling over the cliff to -100
# - Added cliff with X
# - a Check to see if the agent fell over the cliff
# 

class Env:
    def __init__(self):
        self.height = 5
        self.width = 10
        self.posX = 0
        self.posY = 0
        self.endX = self.width-1
        self.endY = 4
        self.cliff = False  # Added Cliff attribute to indicate if the agent fell over the cliff
        self.actions = [0, 1, 2, 3]
        self.stateCount = self.height*self.width
        self.actionCount = len(self.actions)


    def reset(self):
        self.posX = 0
        self.posY = 0
        self.done = False
        return 0, 0, False

    # take action Left, Right, Up, Down [0, 1, 2, 3] respectively
    def step(self, action):
        if action == 0:  # left
            self.posX = max(0, self.posX - 1)
        if action == 1:  # right
            self.posX = min(self.width - 1, self.posX + 1)
        if action == 2:  # up
            self.posY = max(0, self.posY - 1)
        if action == 3:  # down
            self.posY = min(self.height - 1, self.posY + 1)
        
        # Check if the agent fell over the cliff
        self.cliff = (self.posY == self.height - 1) and (1 <= self.posX <= self.width - 2)  

        #end episode if you touch cliff or reach the goal
        done = self.cliff or (self.posX == self.endX and self.posY == self.endY)
        nextState = self.width * self.posY + self.posX

        #REWAED SYSTEM
        if self.cliff:
            reward = -100  # Negative reward for falling over the cliff
        else:
            reward = -1 if not done else 0  # -1 for each step, 0 if the episode is done

        return nextState, reward, done

    # return a random action
    def randomAction(self):
        return np.random.choice(self.actions)

    # display environment
    def render(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.posY == i and self.posX == j:
                    print("O", end='')
                elif self.endY == i and self.endX == j:
                    print("T", end='')
                elif i == 2 and 0 <= j <= self.width - 4:
                    print("X", end='')  # Added cliff with X
                else:
                    print(".", end='')
            print("")