# unc-coffee-bot
The code repository for the coffee making robot.

## Getting Started
First, clone this repository:
```bash
git clone https://github.com/reesenewslab/unc-coffee-bot.git
```

### Download xArm SDK
Before starting anything with the Python implementation of the xArm, please clone the official SDK and set it up in your favourite folder:
```bash
git clone https://github.com/xArm-Developer/xArm-Python-SDK.git
cd xArm-Python-SDK
python setup.py install
```

### demo.py
Provided is a demo script named demo.py which can be used as a template for the movement and gripping functions. In this script you will find the functions to make the robot move in the xyz cartesian coordinate system and in the joint coordinate system. The functions for controlling the gripper are given as well.

Follow the comments provided in the script to help get a better understanding of each line.

