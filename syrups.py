#!/usr/bin/env python3
# Software License Agreement (BSD License)
#
# Copyright (c) 2022, UFACTORY, Inc.
# All rights reserved.
#
# Author: Vinman <vinman.wen@ufactory.cc> <vinman.cub@gmail.com>

from xarm.wrapper import XArmAPI
from common_functions import arm_speed

ip = "192.168.1.215"

#Initialize the xArm with the following parameters:
arm = XArmAPI(ip)
arm.motion_enable(enable=True)
arm.set_mode(0) #Set the mode to 0 (position control mode for x, y, z, roll, pitch, yaw) OR set the mode to 1 (servo control mode for 6 joints)
arm.set_state(state=0) #Start with state 0 (ready)
arm.set_gripper_mode(0) #Set the gripper mode to 0 (position control mode)



def move_cup_to_syrup():
    arm.set_servo_angle(angle=[-23.9, 20.3, -36.4, 92.8, 84.4, 11.9], speed=arm_speed,  wait=False, radius=0.0)
    arm.set_servo_angle(angle=[-11.1, 4.2, -20.0, 91.9, 82.4, 11.9], speed=arm_speed,  wait=False, radius=0.0)
    arm.set_servo_angle(angle=[-0.8, -20.5, -13.7, 100.4, 82.2, 32.2], speed=arm_speed,  wait=False, radius=0.0)
    arm.set_servo_angle(angle=[21.6, -16.3, -22.2, 119.8, 62.8, 32.2], speed=arm_speed,  wait=False, radius=0.0)
    arm.set_position(*[506.7, 444.6, 208.4, 154.2, 87.9, -165.4], speed=arm_speed,  radius=0.0, wait=False)
    arm.set_gripper_position(800, wait=True, speed=5000, auto_enable=True)


def get_ready_to_syrup():
    arm.set_servo_angle(angle=[51.4, -14.1, -17.8, 192.0, 57.6, -4.8], speed=arm_speed,  wait=False, radius=0.0)
    arm.set_servo_angle(angle=[50.3, -40.0, -39.8, 192.0, 12.8, -4.8], speed=arm_speed,  wait=False, radius=0.0)
    arm.set_servo_angle(angle=[47.2, 25.6, -99.9, 191.9, 16.3, -14.4], speed=arm_speed,  wait=False, radius=0.0)
    arm.set_servo_angle(angle=[46.9, 37.8, -119.4, 191.9, 5.6, -14.4], speed=arm_speed,  wait=False, radius=0.0)
    arm.set_servo_angle(angle=[46.9, 39.5, -119.4, 191.9, 5.6, -14.4], speed=arm_speed,  wait=False, radius=0.0)


def squirt_syrup_grab_cup():
    arm_speed = 25
    arm.set_servo_angle(angle=[46.9, 43.3, -119.4, 191.9, 5.6, -14.4], speed=arm_speed,  wait=False, radius=0.0)
    arm.set_servo_angle(angle=[46.9, 39.2, -120.5, 191.9, 5.6, -14.4], speed=arm_speed, wait=False, radius=0.0)
    arm.set_servo_angle(angle=[44.3, -3.4, -120.5, 191.9, -33.7, -14.4], speed=arm_speed,  wait=False, radius=0.0)
    arm.set_servo_angle(angle=[50.5, -22.1, -11.0, 191.9, 55.1, -14.4], speed=arm_speed,  wait=False, radius=0.0)
    arm.set_servo_angle(angle=[50.6, 2.7, -34.4, 191.9, 55.1, -7.7], speed=arm_speed,  wait=False, radius=0.0)
    arm.set_gripper_position(300, wait=True, speed=5000, auto_enable=True)
    

def get_cup_again():
    arm.set_servo_angle(angle=[50.5, -26.3, -9.6, 189.8, 55.1, -7.7], speed=arm_speed,  wait=False, radius=0.0)
    arm.set_servo_angle(angle=[53.1, -26.8, -32.5, 181.8, 27.8, -7.7], speed=arm_speed,  wait=False, radius=0.0)
    arm.set_servo_angle(angle=[77.6, -26.8, -32.5, 181.8, 27.8, -7.7], speed=arm_speed,  wait=False, radius=0.0)
    arm.set_servo_angle(angle=[77.6, 11.8, -17.8, 175.7, 79.3, -7.7], speed=arm_speed,  wait=False, radius=0.0)
    arm.set_servo_angle(angle=[73.7, 30.5, -15.3, 172.7, 100.9, -7.7], speed=arm_speed,  wait=False, radius=0.0)
    arm.set_servo_angle(angle=[73.2, 33.0, -16.2, 172.7, 101.9, -7.7], speed=arm_speed,  wait=False, radius=0.0)

def pump_syrup():
    move_cup_to_syrup()
    get_ready_to_syrup()
    squirt_syrup_grab_cup()
    get_cup_again()


"""
arm.set_servo_angle(angle=[-23.9, 20.3, -36.4, 92.8, 84.4, 11.9], speed=arm_speed,  wait=False, radius=0.0)
    arm.set_servo_angle(angle=[-11.1, 4.2, -20.0, 91.9, 82.4, 11.9], speed=arm_speed,  wait=False, radius=0.0)
    arm.set_servo_angle(angle=[-0.8, -20.5, -13.7, 100.4, 82.2, 32.2], speed=arm_speed,  wait=False, radius=0.0)
    arm.set_servo_angle(angle=[21.6, -16.3, -22.2, 119.8, 62.8, 32.2], speed=arm_speed,  wait=False, radius=0.0)
    arm.set_position(*[506.7, 444.6, 208.4, 154.2, 87.9, -165.4], speed=0,  radius=0.0, wait=False)
    arm.set_gripper_position(800, wait=True, speed=5000, auto_enable=True)
    arm.set_servo_angle(angle=[51.4, -14.1, -17.8, 192.0, 57.6, -4.8], speed=arm_speed,  wait=False, radius=0.0)
    arm.set_servo_angle(angle=[50.3, -40.0, -39.8, 192.0, 12.8, -4.8], speed=arm_speed,  wait=False, radius=0.0)
    arm.set_servo_angle(angle=[47.2, 25.6, -99.9, 191.9, 16.3, -14.4], speed=arm_speed,  wait=False, radius=0.0)
    arm.set_servo_angle(angle=[46.9, 37.8, -119.4, 191.9, 5.6, -14.4], speed=arm_speed,  wait=False, radius=0.0)
    arm.set_servo_angle(angle=[46.9, 39.5, -119.4, 191.9, 5.6, -14.4], speed=arm_speed,  wait=False, radius=0.0)
    arm_speed = 25
    arm.set_servo_angle(angle=[46.9, 43.3, -119.4, 191.9, 5.6, -14.4], speed=arm_speed,  wait=False, radius=0.0)
    arm.set_servo_angle(angle=[46.9, 39.2, -120.5, 191.9, 5.6, -14.4], speed=arm_speed, wait=False, radius=0.0)
    arm.set_servo_angle(angle=[44.3, -3.4, -120.5, 191.9, -33.7, -14.4], speed=arm_speed,  wait=False, radius=0.0)
    arm.set_servo_angle(angle=[50.5, -22.1, -11.0, 191.9, 55.1, -14.4], speed=arm_speed,  wait=False, radius=0.0)
    arm.set_servo_angle(angle=[50.6, 2.7, -34.4, 191.9, 55.1, -7.7], speed=arm_speed,  wait=False, radius=0.0)
    arm.set_gripper_position(300, wait=True, speed=5000, auto_enable=True)
    arm.set_servo_angle(angle=[50.5, -26.3, -9.6, 189.8, 55.1, -7.7], speed=arm_speed,  wait=False, radius=0.0)
    arm.set_servo_angle(angle=[53.1, -26.8, -32.5, 181.8, 27.8, -7.7], speed=arm_speed,  wait=False, radius=0.0)
    arm.set_servo_angle(angle=[77.6, -26.8, -32.5, 181.8, 27.8, -7.7], speed=arm_speed,  wait=False, radius=0.0)
    arm.set_servo_angle(angle=[77.6, 11.8, -17.8, 175.7, 79.3, -7.7], speed=arm_speed,  wait=False, radius=0.0)
    arm.set_servo_angle(angle=[73.7, 30.5, -15.3, 172.7, 100.9, -7.7], speed=arm_speed,  wait=False, radius=0.0)
    arm.set_servo_angle(angle=[73.2, 33.0, -16.2, 172.7, 101.9, -7.7], speed=arm_speed,  wait=False, radius=0.0)
"""