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
    id='su_cartpole_discrete-v0',
    entry_point='gym_ucsb_robolab.classic_control:SUCartPoleDiscEnv'
)

register(
    id='su_pendulum-v0',
    entry_point='gym_ucsb_robolab.classic_control:SUPendulumEnv',
)

register(
    id='lorenz-v0',
    entry_point='gym_ucsb_robolab.simple_nonlinear:LorenzEnv',
)

register(
    id='5linkWalker-v3',
    max_episode_steps=1000,
    entry_point='gym.envs.mujoco:FiveLinkwalkerv3Env',
)
