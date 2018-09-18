from gym.envs.registration import register

register(
    id='su_cartpole-v0',
    entry_point='gym_ucsb_robolab.envs:SUCartPoleEnv',
)
