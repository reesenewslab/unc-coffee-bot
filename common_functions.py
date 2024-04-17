"""File of common use functions across the project."""

from xarm.wrapper import XArmAPI

ip = "192.168.1.215" #Change this to your xArm IP address

#Initialize the xArm with the following parameters:
arm = XArmAPI(ip)
arm.motion_enable(enable=True)
arm.set_mode(0) #Set the mode to 0 (position control mode for x, y, z, roll, pitch, yaw) OR set the mode to 1 (servo control mode for 6 joints)
arm.set_state(state=0) #Start with state 0 (ready)
arm.set_gripper_mode(0) #Set the gripper mode to 0 (position control mode)

arm_speed: int = 50

def open_gripper():
    arm.set_gripper_position(800, wait=True, speed=5000, auto_enable=True) 


