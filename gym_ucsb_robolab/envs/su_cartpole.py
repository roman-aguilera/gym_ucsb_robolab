import numpy as np
from numpy import pi
from gym.envs.mujoco import mujoco_env


class SUCartPoleEnv(mujoco_env.MujocoEnv):
    def __init__(self, num_steps  = 1500):
        mujoco_env.MujocoEnv.__init__(self, 'su_cartpole.xml', 1)
        self.num_steps = num_steps
        self.cur_step = 0

    def step(self, action):
        # get newest state variables
        # q_pos = self.sim.get_state()[1]
        # q_vel = self.sim.get_state()[2]

        self.do_simulation(action, self.frame_skip)

        ob = np.concatenate([self.sim.data.qpos, self.sim.data.qvel]).ravel()
        reward = np.sin(self.sim.data.qpos[1])

        # TODO figure out how to keep state history around (maybe do this in the agent??)
        self.cur_step += 1
        if self.cur_step > self.num_steps:
            done = True

        return ob, reward, done, {}

    def reset_model(self):
        qpos = self.init_qpos + self.np_random.uniform(size=self.model.nq, low=-0.01, high=0.01)
        qvel = self.init_qvel + self.np_random.uniform(size=self.model.nv, low=-0.01, high=0.01)
        self.set_state(qpos, qvel)
        return self._get_obs()

    def render(self, mode='human', close=False):
        pass


    def viewer_setup(self):
        v = self.viewer
        v.cam.trackbodyid = 0
        v.cam.distance = self.model.stat.extent