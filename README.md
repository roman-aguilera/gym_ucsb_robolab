# UCSB Robolab's Gym

This is the UCSB Robolab's collection of OpenAI gym environments. 

## Installation

To use the easiest way is to clone or download the repo. Then use:

pip install -e ./gym_ucsb_robolab

## Usage

all you need to do is add:

```
import gym
import gym_ucsb_robolab
```

to your code, and you should be able to access all of our environments as if they were baked right into gym. 


## Errors with mujoco_py
If you get an error related to mujoco_py failing to compile try the following:

First try using python 3.6
Next install mujoco_py manually by cloning it and installing version 1.5

```
git clone https://github.com/openai/mujoco-py/
cd mujoco-py
git checkout -b 1.50.1.1 
pip install -e .
```
