from gym.envs.registration import register

register(
    id='mj_su_cartpole-v0',
    entry_point='gym_ucsb_robolab.mujoco:MJSUCartPoleEnv',
)

register(
    id='mj_su_cartpole_sparse-v0',
    entry_point='gym_ucsb_robolab.mujoco:MJSUCartPoleSparseEnv',
)

register(
    id='mj_su_cartpole_et-v0',
    entry_point='gym_ucsb_robolab.mujoco:MJSUCartPoleEtEnv',
)

register(
    id='mj_su_cartpole_discrete-v0',
    entry_point='gym_ucsb_robolab.mujoco:MJSUCartPoleDiscreteEnv',
)

register(
    id='su_cartpole-v0',
    entry_point='gym_ucsb_robolab.classic_control:SUCartPoleEnv',
)

register(
    id='su_pendulum-v0',
    entry_point='gym_ucsb_robolab.mujoco:SUPendulumEnv',
)

