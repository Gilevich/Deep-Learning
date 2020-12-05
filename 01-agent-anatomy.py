import random

class Environment:
    def __init__(self):
        self.steps_left = 20

    def GetObservation(self):
        return [0.0, 0.0, 0.0]

    def GetAction(self):
        return [0, 1]

    def isDone(self):
        return self.steps_left == 0

    def action(self, action):
        if self.isDone():
            raise Exception("Game is over")
        self.steps_left -= 1
        return random.random()


class Agent:
    def __init__(self):
        self.TotalReward = 0.0

    def step(self, env):
        CurrentObs = env.GetObservation()
        actions = env.GetAction()
        reward = env.action(random.choice(actions))
        self.TotalReward += reward


if __name__ == "__main__":
    env = Environment()
    agent = Agent()

    while not env.isDone():
        agent.step(env)
    print('Total reward: %.4f' % agent.TotalReward)
