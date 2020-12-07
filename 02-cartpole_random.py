import gym

def main():
    env = gym.make("CartPole-v0")
    TotalReward = 0
    TotalSteps = 0
    obs = env.reset()
    while True:
        action = env.action_space.sample()
        obs, reward, done, _ = env.step(action)
        TotalReward += reward
        TotalSteps += 1
        if done:
            break
    print("Episode done in %d steps, total reward %.2f" % (TotalSteps, TotalReward))


if __name__ == '__main__':
    main()
