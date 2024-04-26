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
    arm.set_servo_angle(angle=[-23.9, 20.3, -36.4, 92.8, 84.4, 11.9], speed=arm_speed,  wait=False, radius=0.0)
    arm.set_servo_angle(angle=[-11.1, 4.2, -20.0, 91.9, 82.4, 11.9], speed=arm_speed,  wait=False, radius=0.0)
    arm.set_servo_angle(angle=[-0.8, -20.5, -13.7, 100.4, 82.2, 32.2], speed=arm_speed,  wait=False, radius=0.0)
    arm.set_servo_angle(angle=[21.6, -16.3, -22.2, 119.8, 62.8, 32.2], speed=arm_speed,  wait=False, radius=0.0)
    # replacing position with more precise angles
    # arm.set_position(*[506.7, 444.6, 208.4, 154.2, 87.9, -165.4], speed=arm_speed,  radius=0.0, wait=False)
    #go in
    arm.set_servo_angle(angle=[34.8, -15.7, -16.6, 148.4, 57.1, 19.1], speed=arm_speed,  wait=False, radius=0.0)
    #adjust going in to be more delicate
    arm.set_servo_angle(angle=[35.7, -3.6, -31.7, 148.4, 57.1, 19.1], speed=arm_speed,  wait=False, radius=0.0)
    arm.set_servo_angle(angle=[36.2, 5.3, -38.8, 148.4, 57.1, 19.1], speed=arm_speed,  wait=False, radius=0.0)
    arm.set_gripper_position(800, wait=True, speed=5000, auto_enable=True)


def get_ready_to_caramel():
    arm.set_position(*[515.0, 482.0, 205.4, 156.9, 84.3, -149.7], speed=arm_speed,  radius=0.0, wait=False)
    arm.set_position(*[513.3, 453.7, 209.8, 179.4, 83.5, -143.0], speed=arm_speed,  radius=0.0, wait=False)



    arm.set_servo_angle(angle=[55.3, -7.7, -23.7, 199, 57, -8.5], speed=arm_speed,  wait=False, radius=0.0)
    arm.set_servo_angle(angle=[50.3, -40.0, -39.8, 192.0, 12.8, -4.8], speed=arm_speed,  wait=False, radius=0.0)
    arm.set_servo_angle(angle=[47.2, 25.6, -99.9, 191.9, 16.3, -14.4], speed=arm_speed,  wait=False, radius=0.0)
    arm.set_servo_angle(angle=[46.9, 37.8, -119.4, 191.9, 5.6, -14.4], speed=arm_speed,  wait=False, radius=0.0)
    set_arm_speed(4)
    arm.set_servo_angle(angle=[46.9, 39.5, -119.4, 191.9, 5.6, -14.4], speed=arm_speed,  wait=False, radius=0.0)


def squirt_caramel_grab_cup():
    arm.set_servo_angle(angle=[46.9, 43.3, -119.4, 191.9, 5.6, -14.4], speed=arm_speed,  wait=False, radius=0.0)
    arm.set_servo_angle(angle=[46.9, 39.2, -120.5, 191.9, 5.6, -14.4], speed=arm_speed, wait=False, radius=0.0)
    set_arm_speed(30)
    arm.set_servo_angle(angle=[44.3, -3.4, -120.5, 191.9, -33.7, -14.4], speed=arm_speed,  wait=False, radius=0.0)
    arm.set_servo_angle(angle=[50.5, -22.1, -11.0, 191.9, 55.1, -14.4], speed=arm_speed,  wait=False, radius=0.0)
    arm.set_servo_angle(angle=[55.3, -7.7, -23.7, 199.0, 57.0, -8.5], speed=arm_speed,  wait=False, radius=0.0)

    arm.set_position(*[513.3, 459.7, 209.8, 179.4, 83.5, -143.0], speed=arm_speed,  radius=0.0, wait=False)
    arm.set_position(*[515.0, 482.0, 205.4, 156.9, 84.3, -149.7], speed=arm_speed,  radius=0.0, wait=False)
    arm.set_gripper_position(300, wait=True, speed=5000, auto_enable=True)
    

def get_cup_again_caramel():
    arm.set_servo_angle(angle=[50.5, -26.3, -9.6, 189.8, 55.1, -7.7], speed=arm_speed,  wait=False, radius=0.0)
    arm.set_position(*[424.8, 462.5, 346.5, -114.0, 82.6, -62.0], speed=arm_speed,  radius=0.0, wait=False)
    arm.set_position(*[449.3, 443.8, 440.9, -19.0, 80.8, 52.8], speed=arm_speed,  radius=0.0, wait=False)
    arm.set_position(*[351.8, 371.3, 436.6, -64.1, 86.5, 28.6], speed=arm_speed, radius=0.0, wait=False)
    arm.set_position(*[231.8, 324.3, 336.2, 169.8, 88.8, -78.5], speed=arm_speed,  radius=0.0, wait=False)
    arm.set_position(*[245.4, 341.4, 206.7, -102.2, 85.8, 8.2], speed=arm_speed,  radius=0.0, wait=False)
    arm.set_position(*[201.6, 359.6, 89.3, 173.5, 82.6, -78.2], speed=arm_speed, radius=0.0, wait=False)
    arm.set_servo_angle(angle=[-1.1, 12.3, -23.5, 70.3, 86.9, 11.9], speed=arm_speed,  wait=False, radius=40.0)

    
def pump_carame():
    move_cup_to_caramel()
    get_ready_to_caramel()
    squirt_caramel_grab_cup()
    get_cup_again_caramel()


