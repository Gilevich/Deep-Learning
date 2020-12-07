import gym
import random

class RandomActionWrapper(gym.ActionWrapper):
    def __init__(self, env, epsilon=0.1):
        super(RandomActionWrapper, self).__init__(env)
        self.epsilon = epsilon

    def action(self,action):
        if random.random() > self.epsilon:
            print("Random!")
            return self.env.action_space.sample()
        return action


def main():
    env = RandomActionWrapper(gym.make("CartPole-v0"))
    obs = env.reset()
    TotalReward = 0.0
    while True:
        obs, reward, done, _ = env.step(0)
        TotalReward += reward
        if done:
            break

if __name__ == '__main__':
    main()
