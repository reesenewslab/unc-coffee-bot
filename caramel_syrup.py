#!/usr/bin/env python3
# Software License Agreement (BSD License)
#
# Copyright (c) 2022, UFACTORY, Inc.
# All rights reserved.
#
# Author: Vinman <vinman.wen@ufactory.cc> <vinman.cub@gmail.com>

from xarm.wrapper import XArmAPI
from common_functions import arm_speed, set_arm_speed

ip = "192.168.1.215"

#Initialize the xArm with the following parameters:
arm = XArmAPI(ip)
arm.motion_enable(enable=True)
arm.set_mode(0) #Set the mode to 0 (position control mode for x, y, z, roll, pitch, yaw) OR set the mode to 1 (servo control mode for 6 joints)
arm.set_state(state=0) #Start with state 0 (ready)
arm.set_gripper_mode(0) #Set the gripper mode to 0 (position control mode)



def move_cup_to_caramel():
    # start down, front of coffee tray
    arm.set_servo_angle(angle=[-23.9, 20.3, -36.4, 92.8, 84.4, 11.9], speed=arm_speed,  wait=False, radius=0.0)
    # down, front of syrups tray
    arm.set_servo_angle(angle=[-11.1, 4.2, -20.0, 91.9, 82.4, 11.9], speed=arm_speed,  wait=False, radius=0.0)
    # up, front of syrups tray
    arm.set_servo_angle(angle=[-0.8, -20.5, -13.7, 100.4, 82.2, 32.2], speed=arm_speed,  wait=False, radius=0.0)
    # go in for caramel
    arm.set_servo_angle(angle=[34.4, 4.5, -36.1, 132.5, 64.9, 18.8], speed=arm_speed,  wait=False, radius=0.0)
    # let go
    arm.set_gripper_position(800, wait=True, speed=5000, auto_enable=True)


def get_ready_to_caramel():
    #  move back to front of syrups
    arm.set_servo_angle(angle=[17.9, -20.9, -7.6, 127.1, 73.9, 25.0], speed=arm_speed,  wait=False, radius=0.0)
    # spin for caramel to avoid wire crashing
    arm.set_servo_angle(angle=[50.8, -31.4, -39.3, 138.9, 24.6, 41.1], speed=arm_speed,  wait=False, radius=0.0)
    arm.set_servo_angle(angle=[60.6, 24.9, -113.8, 127.9, 1.1, -44.3], speed=arm_speed,  wait=False, radius=0.0)


def squirt_caramel_grab_cup():
    # go down and up
    set_arm_speed(4)
    arm.set_servo_angle(angle=[57.5, 37.2, -113.8, 127.9, 20.7, -44.3], speed=arm_speed, wait=False, radius=0.0)
    arm.set_servo_angle(angle=[57.5, 41.3, -113.8, 127.9, 20.7, -44.3], speed=arm_speed, wait=False, radius=0.0)
    arm.set_servo_angle(angle=[57.5, 40.4, -117.9, 127.9, 20.7, -44.3], speed=arm_speed, wait=False, radius=0.0)
    set_arm_speed(25)
    # finished going back up
    # unspin
    arm.set_servo_angle(angle=[60.6, 24.9, -113.8, 127.9, 1.1, -44.3], speed=arm_speed, wait=False, radius=0.0)
    arm.set_servo_angle(angle=[50.8, -31.4, -39.3, 138.9, 24.6, 41.1], speed=arm_speed, wait=False, radius=0.0)
    arm.set_servo_angle(angle=[39.9, -1.8, -37.9, 138.9, 55.5, 22.9], speed=arm_speed, wait=False, radius=0.0)
    arm.set_servo_angle(angle=[38.6, -4.1, -34.4, 138.9, 55.5, 22.9], speed=arm_speed, wait=False, radius=0.0)

    arm.set_position(*[449.4, 534.7, 196.8, -159.2, 81.1, -85], speed=arm_speed, radius=0.0, wait=False)

    # grab syrupy cupy
    arm.set_gripper_position(305, wait=True, speed=5000, auto_enable=True)
    

def get_cup_again_caramel():
    # move up/back
    arm.set_servo_angle(angle=[28, -1.1, -41.6, 110.5, 67.3, 38.3], speed=arm_speed, wait=False, radius=0.0)
    arm.set_servo_angle(angle=[18.1, -28, -15.9, 110.5, 67.2, 38.3], speed=arm_speed, wait=False, radius=0.0)


    arm.set_servo_angle(angle=[-0.8, -20.5, -13.7, 100.4, 82.2, 32.2], speed=arm_speed, wait=False, radius=0.0)
    # move down
    arm.set_servo_angle(angle=[-11.1, 4.2, -20.0, 91.9, 82.4, 11.9], speed=arm_speed, wait=False, radius=0.0)
    # ending position
    arm.set_position(*[201.6, 359.6, 89.3, 173.5, 82.6, -78.2], speed=arm_speed, radius=0.0, wait=False)
    # ending position equivalent in joint angle - should not move from prev line
    arm.set_servo_angle(angle=[-1.1, 12.3, -23.5, 70.3, 86.9, 11.9], speed=arm_speed,  wait=False, radius=40.0)

    
def pump_caramel():
    move_cup_to_caramel()
    get_ready_to_caramel()
    squirt_caramel_grab_cup()
    get_cup_again_caramel()




            
           

           
     





