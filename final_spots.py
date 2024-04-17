
from xarm.wrapper import XArmAPI #Import the xArmAPI class from the xArm Python SDK

ip = "192.168.1.215" #Change this to your xArm IP address

#Initialize the xArm with the following parameters:
arm = XArmAPI(ip)
arm.motion_enable(enable=True)
arm.set_mode(0) #Set the mode to 0 (position control mode for x, y, z, roll, pitch, yaw) OR set the mode to 1 (servo control mode for 6 joints)
arm.set_state(state=0) #Start with state 0 (ready)
arm.set_gripper_mode(0) #Set the gripper mode to 0 (position control mode)

arm_speed: int = 50



def spot0():
    arm.set_servo_angle(angle=[30.6, 13.2, -21.4, 102.8, 83.9, 11.9], speed=arm_speed,  wait=False, radius=0.0)
    arm.set_servo_angle(angle=[48.8, 19.7, -23.5, 125.9, 78, 2.1], speed=arm_speed,  wait=False, radius=0.0)
    arm.set_servo_angle(angle=[48.5, 29.9, -25.4, 127, 85, -3.3], speed=arm_speed,  wait=False, radius=0.0)


def spot1():
    arm.set_servo_angle(angle=[23.7, 12.2, -13.1, 70.3, 85.6, 2.2], speed=arm_speed,  wait=False, radius=0.0)
    arm.set_servo_angle(angle=[72.9, 18.3, -16, 130.6, 85.5, -4.1], speed=arm_speed,  wait=False, radius=0.0)
    arm.set_servo_angle(angle=[70.7, 32.3, -19.9, 130.6, 96, -8.8], speed=arm_speed,  wait=False, radius=0.0)


def spot2():
    arm.set_servo_angle(angle=[8.2, 12.3, -20.4, 49.1, 93.2, 4.7], speed=arm_speed,  wait=False, radius=0.0)
    arm.set_servo_angle(angle=[84.7, 12.5, -13.2, 117.9, 84.6, 1.3], speed=arm_speed,  wait=False, radius=0.0)
    arm.set_servo_angle(angle=[81.1, 28.5, -18.1, 116.7, 91.7, -6.8], speed=arm_speed,  wait=False, radius=0.0)


def spot3():
    arm.set_servo_angle(angle=[41.2, 16.6, -28.5, 46,95.1, 11.9], speed=arm_speed,  wait=False, radius=0.0)
    arm.set_servo_angle(angle=[74.5, 18.9, -17.4, 78.5, 90.1, 1], speed=arm_speed,  wait=False, radius=0.0)
    arm.set_servo_angle(angle=[76.4, 30.2, -23.3, 78.5, 88.2, -4.3], speed=arm_speed,  wait=False, radius=0.0)