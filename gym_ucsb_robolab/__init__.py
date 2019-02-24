from gym.envs.registration import register

register(
    id='su_cartpole-v0',
    entry_point='gym_ucsb_robolab.mujoco:SUCartPoleEnv',
)

register(
    id='su_cartpole_sparse-v0',
    entry_point='gym_ucsb_robolab.mujoco:SUCartPoleSparseEnv',
)

register(
    id='su_cartpole_et-v0',
    entry_point='gym_ucsb_robolab.mujoco:SUCartPoleEtEnv',
)

register(
    id='su_cartpole_discrete-v0',
    entry_point='gym_ucsb_robolab.mujoco:SUCartPoleDiscreteEnv',
)


register(
    id='su_pendulum-v0',
    entry_point='gym_ucsb_robolab.mujoco:SUPendulumEnv',
)

