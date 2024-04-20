#!/usr/bin/env python3
# Software License Agreement (BSD License)
#
# Copyright (c) 2022, UFACTORY, Inc.
# All rights reserved.
#
# Author: Vinman <vinman.wen@ufactory.cc> <vinman.cub@gmail.com>

from xarm.wrapper import XArmAPI
import time
from enum import Enum
from common_functions import arm_speed


ip = "192.168.1.215"

#Initialize the xArm with the following parameters:
arm = XArmAPI(ip)
arm.motion_enable(enable=True)
arm.set_mode(0) #Set the mode to 0 (position control mode for x, y, z, roll, pitch, yaw) OR set the mode to 1 (servo control mode for 6 joints)
arm.set_state(state=0) #Start with state 0 (ready)
arm.set_gripper_mode(0) #Set the gripper mode to 0 (position control mode)


class Coffee(Enum):
   ESPRESSO = "ESPRESSO"
   LATTE = "LATTE"
   CAPPUCINO = "CAPPUCINO"
   MACCHIATO= "MACCHIATO"
   FLAT_WHITE = "FLAT WHITE"
   TEA= "TEA"
   AMERICANO= "AMERICANO"

def click_right():
    """Go to the next page."""
    arm.set_servo_angle(angle=[-22.2, 3.2, -46.9, 88.8, 84.4, 13.7], speed=arm_speed, wait=False, radius=0.0)
    arm.set_servo_angle(angle=[-19.3, 6.8, -49.6, 89.4, 84.7, 13.7], speed=arm_speed,  wait=False, radius=0.0)
    arm.set_servo_angle(angle=[-22.2, 3.2, -46.9, 88.8, 84.4, 13.7], speed=arm_speed,  wait=False, radius=0.0)
    arm.set_servo_angle(angle=[-23.5, -12.4, -27.3, 88.8, 89.6, 13.7], speed=arm_speed, wait=False, radius=0.0)


def make_coffee(coffee_type: Coffee):
    """Makes the coffee."""
    match coffee_type:
        case Coffee.ESPRESSO:
            arm.set_servo_angle(angle=[-16.0, -12.1, -33.8, 83.9, 83.7, 13.7], speed=arm_speed, wait=False, radius=0.0)
            arm.set_servo_angle(angle=[-15.6, -12.0, -30.7, 88.5, 84.6, 13.7], speed=arm_speed, wait=False, radius=0.0)

        case Coffee.CAPPUCINO:
            arm.set_servo_angle(angle=[-14.6, -12.0, -27.3, 88.8, 81.7, 13.7], speed=arm_speed, wait=False, radius=0.0)
        case Coffee.LATTE:
            arm.set_servo_angle(angle=[-16.3, -3.0, -35.8, 92.7, 81.7, 13.7], speed=arm_speed, wait=False, radius=0.0)
        case Coffee.MACCHIATO:
            arm.set_servo_angle(angle=[-16.9, -5, -39.1, 89.4, 81.5, 13.7], speed=arm_speed, wait=False, radius=0.0)
        case Coffee.AMERICANO:
            click_right()
            arm.set_servo_angle(angle=[-14.0, -12.4, -27.7, 88.8, 80.4, 13.7], speed=arm_speed, wait=False, radius=0.0)
        case Coffee.FLAT_WHITE:
            click_right()
            arm.set_servo_angle(angle=[-15.3, -8.6, -32.1, 89.4, 87.6, 13.7], speed=arm_speed, wait=False, radius=0.0)
        case Coffee.TEA:
            click_right()
            click_right()
            arm.set_servo_angle(angle=[-16.7, -3.0, -40.9, 81.7, 91.3, 13.7], speed=arm_speed, wait=False, radius=0.0)
            arm.set_servo_angle(angle=[-23.5, -12.4, -27.3, 88.8, 89.6, 13.7], speed=arm_speed, wait=False, radius=0.0)
            time.sleep(40)
            click_right()
            click_right()
            arm.set_servo_angle(angle=[-16.7, -3.0, -40.9, 81.7, 91.3, 13.7], speed=arm_speed, wait=False, radius=0.0)
    time.sleep(2)
    arm.set_servo_angle(angle=[-23.5, -12.4, -27.3, 88.8, 89.6, 13.7], speed=arm_speed, wait=False, radius=0.0)

    if coffee_type == Coffee.ESPRESSO or coffee_type == Coffee.TEA:
        time.sleep(40)
    else:
        time.sleep(90)


