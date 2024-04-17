#!/usr/bin/env python3
# Software License Agreement (BSD License)
#
# Copyright (c) 2022, UFACTORY, Inc.
# All rights reserved.
#
# Author: Vinman <vinman.wen@ufactory.cc> <vinman.cub@gmail.com>

from xarm.wrapper import XArmAPI

ip = "192.168.1.213" #Change this to your xArm IP address

#Initialize the xArm with the following parameters:
arm = XArmAPI(ip)
arm.motion_enable(enable=True)
arm.set_mode(0) #Set the mode to 0 (position control mode for x, y, z, roll, pitch, yaw) OR set the mode to 1 (servo control mode for 6 joints)
arm.set_state(state=0) #Start with state 0 (ready)
arm.set_gripper_mode(0) #Set the gripper mode to 0 (position control mode)

arm_speed: int = 50

#TODO: get normal espresso moiton!

def click_right():
    """Go to the next page."""
    #TODO: make sure this is actually what I meant
    arm.set_servo_angle(angle=[-18.1, -0.9, -45.4, 88.9, 77.4, 13.7], speed=arm_speed, wait=False, radius=0.0)
    arm.set_servo_angle(angle=[-16.9, 2.0, -49.4, 86.0, 78.3, 13.7], speed=arm_speed, wait=False, radius=0.0)
    arm.set_servo_angle(angle=[-23.5, -12.4, -27.3, 88.8, 89.6, 13.7], speed=arm_speed, wait=False, radius=0.0)

def make_coffee():
    """Makes the coffee."""
    arm.set_servo_angle(angle=[-23.5, -12.4, -27.3, 88.8, 89.6, 13.7], speed=arm_speed, wait=False, radius=0.0)
    coffee: str = input("hello")
    match coffee:
        case "CAPPUCINO":
            arm.set_servo_angle(angle=[-14.6, -12.0, -27.3, 88.8, 81.7, 13.7], speed=arm_speed, wait=False, radius=0.0)
        case "LATTE":
            arm.set_servo_angle(angle=[-16.3, -3.0, -35.8, 92.7, 81.7, 13.7], speed=arm_speed, wait=False, radius=0.0)
        case "DOUBLE_ESPRESSO":
            arm.set_servo_angle(angle=[-13.9, -12.3, -30.8, 93.2, 80.9, 13.7], speed=arm_speed, wait=False, radius=0.0)
        case "AMERICANO":
            click_right()
            arm.set_servo_angle(angle=[-14.0, -12.4, -27.7, 88.8, 80.4, 13.7], speed=arm_speed, wait=False, radius=0.0)
        case "FLAT_WHITE":
            click_right()
            arm.set_servo_angle(angle=[-15.3, -8.6, -32.1, 89.4, 87.6, 13.7], speed=arm_speed, wait=False, radius=0.0)
        case "TEA":
            click_right()
            click_right()
            arm.set_servo_angle(angle=[-16.7, -3.0, -40.9, 81.7, 91.3, 13.7], speed=arm_speed, wait=False, radius=0.0)
    arm.set_servo_angle(angle=[-23.5, -12.4, -27.3, 88.8, 89.6, 13.7], speed=arm_speed, wait=False, radius=0.0)

