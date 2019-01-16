from gym.envs.registration import register

register(
    id='su_cartpole-v0',
    entry_point='gym_ucsb_robolab.envs:SUCartPoleEnv',
)

register(
    id='su_cartpole_sparse-v0',
    entry_point='gym_ucsb_robolab.envs:SUCartPoleSparseEnv',
)

register(
    id='su_cartpole_et-v0',
    entry_point='gym_ucsb_robolab.envs:SUCartPoleEtEnv',
)

register(
    id='su_pendulum-v0',
    entry_point='gym_ucsb_robolab.envs:SUPendulumEnv',
)

