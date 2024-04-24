
from xarm.wrapper import XArmAPI #Import the xArmAPI class from the xArm Python SDK
from common_functions import arm_speed

ip = "192.168.1.215" 

#Initialize the xArm with the following parameters:
arm = XArmAPI(ip)
arm.motion_enable(enable=True)
arm.set_mode(0) #Set the mode to 0 (position control mode for x, y, z, roll, pitch, yaw) OR set the mode to 1 (servo control mode for 6 joints)
arm.set_state(state=0) #Start with state 0 (ready)
arm.set_gripper_mode(0) #Set the gripper mode to 0 (position control mode)


def reset_spot():
    arm.set_servo_angle(angle=[54.4, -34.8, -50.1, 103.4, 78, 79.7], speed=arm_speed,  wait=False, radius=0.0)
    arm.set_servo_angle(angle=[-41.6, -5.5, -82.8, 121.5, 74.5, -59.0], speed=arm_speed,  wait=False, radius=0.0)


def open_gripper():
    arm.set_gripper_position(800, wait=True, speed=5000, auto_enable=True) 

def spot0():
    arm.set_servo_angle(angle=[30.6, 13.2, -21.4, 102.8, 83.9, 11.9], speed=arm_speed,  wait=False, radius=0.0)
    arm.set_servo_angle(angle=[48.8, 19.7, -23.5, 125.9, 78, 2.1], speed=arm_speed,  wait=False, radius=0.0)
    arm.set_servo_angle(angle=[48.5, 29.9, -25.4, 127, 85, -3.3], speed=arm_speed,  wait=False, radius=0.0)
    open_gripper()
    arm.set_servo_angle(angle=[50.1, 17.1, -21.4, 127, 86.4, 5], speed=arm_speed,  wait=False, radius=0.0)
    reset_spot()

def spot1():
    arm.set_servo_angle(angle=[23.7, 12.2, -13.1, 70.3, 85.6, 2.2], speed=arm_speed,  wait=False, radius=0.0)
    arm.set_servo_angle(angle=[72.9, 18.3, -16, 130.6, 85.5, -4.1], speed=arm_speed,  wait=False, radius=0.0)
    arm.set_servo_angle(angle=[70.7, 32.3, -19.9, 130.6, 96, -8.8], speed=arm_speed,  wait=False, radius=0.0)
    open_gripper()
    arm.set_servo_angle(angle=[61.3, 16.1, -28.3, 103.4, 82.9, 14.7], speed=arm_speed,  wait=False, radius=0.0)
    reset_spot()

def spot2():
    arm.set_servo_angle(angle=[8.2, 12.3, -20.4, 49.1, 93.2, 4.7], speed=arm_speed,  wait=False, radius=0.0)
    arm.set_servo_angle(angle=[84.7, 12.5, -13.2, 117.9, 84.6, 1.3], speed=arm_speed,  wait=False, radius=0.0)
    arm.set_servo_angle(angle=[79.8, 31.3, -20.3, 116.7, 91.8, -6.8], speed=arm_speed,  wait=False, radius=0.0)
    open_gripper()
    arm.set_servo_angle(angle=[81, 14.1, -12.4, 116.7, 94.7, -6.8], speed=arm_speed,  wait=False, radius=0.0)
    reset_spot()

def spot3():
    arm.set_servo_angle(angle=[41.2, 16.6, -28.5, 46,95.1, 11.9], speed=arm_speed,  wait=False, radius=0.0)
    arm.set_servo_angle(angle=[74.5, 18.9, -17.4, 78.5, 90.1, 1], speed=arm_speed,  wait=False, radius=0.0)
    arm.set_servo_angle(angle=[76.4, 30.2, -23.3, 78.5, 88.2, -4.3], speed=arm_speed,  wait=False, radius=0.0)
    open_gripper()
    arm.set_servo_angle(angle=[72.2, 13.6, -13.9, 76.6, 94, -4.3], speed=arm_speed,  wait=False, radius=0.0)
    reset_spot()

