[//]: # (Image References)

[image1]: https://user-images.githubusercontent.com/10624937/42135619-d90f2f28-7d12-11e8-8823-82b970a54d7e.gif "Trained Agent"

# Project 1: Navigation

### 1 Introduction

This project is focused on training an agent to move and collect/avoid certain kinds of objects in a 3D world. 

![Trained Agent][image1]

A reward of +1 is provided for collecting a yellow banana, and a reward of -1 is provided for collecting a blue banana. 
Therefore, the desired behaviour is to collect as many yellow bananas while avoiding the blue bananas.

The state space has 37 dimensions and contains the agent's velocity, along with ray-based perception of objects around agent's forward direction.  Given this information, the agent has to learn how to best select actions.  Four discrete actions are available, corresponding to:
- **`0`** - move forward.
- **`1`** - move backward.
- **`2`** - turn left.
- **`3`** - turn right.

The task is episodic and is considered complete when the agent scores an average of 13+ points during the last 100 episodes.

### 2 Getting Started

1. Clone this repository to your local machine/server
2. Download the environment from one of the links below.  You need only select the environment that matches your operating system:
    - Linux: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Linux.zip)
    - Mac OSX: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana.app.zip)
    - Windows (32-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86.zip)
    - Windows (64-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86_64.zip)
    
    (_For Windows users_) Check out [this link](https://support.microsoft.com/en-us/help/827218/how-to-determine-whether-a-computer-is-running-a-32-bit-version-or-64) if you need help with determining if your computer is running a 32-bit version or 64-bit version of the Windows operating system.

    (_For AWS_) If you'd like to train the agent on AWS (and have not [enabled a virtual screen](https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Training-on-Amazon-Web-Service.md)), then please use [this link](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Linux_NoVis.zip) to obtain the environment.

3. Unzip (or decompress) the downloaded file into the root folder of your local clone of this repository. 

#### 2.1 Requirements
To install required dependencies for running the code using Anaconda please follow the instructions bellow.
1. Make a new environment e.g. \
    `conda create -n drlnd-p1`
    
2. Activate the environment
    - `activate drlnd-p1` (for Windows)
    - `conda activate drlnd-p1` (elsewhere)
    
3. Install python version 3.6 (newer versions have dependency problems with unityagents) \
    `conda install python=3.6`
    
4. Install pytorch based on your preferences (please refer to the Install table on [pytorch site](https://pytorch.org/))
    - for example installing PyTorch witch CUDA 10.2 support: \
        `conda install pytorch torchvision cudatoolkit=10.2 -c pytorch`
        
5. Install jupyter notebook package \
    `conda install notebook`
    
6. Install Unity Machine Learning Agents package using pip \
    `pip install unityagents`

Congratulations! If everything went well, you should now have an environment which is ready to run the 
code in this repository. 

### 3 Instructions
To run the notebook, you just have to activate the previously created conda repository from Anaconda console and start a jupyter notebook server in the local clone root.
1. Activate the environment
    - `activate drlnd-p1` (for Windows)
    - `conda activate drlnd-p1` (elsewhere)

2. Change current console folder to the root of the cloned repository \
    `cd \d path/to/local/repo/clone/` 

3. Run jupyter notebook server \
    `jupyter notebook`
    
4. Open `Navigation.ipynb` and follow the instructions