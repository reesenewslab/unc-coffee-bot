"""File of common use functions across the project."""

from xarm.wrapper import XArmAPI

ip = "192.168.1.215" 

#Initialize the xArm with the following parameters:
arm = XArmAPI(ip)
arm.motion_enable(enable=True)
arm.set_mode(0) #Set the mode to 0 (position control mode for x, y, z, roll, pitch, yaw) OR set the mode to 1 (servo control mode for 6 joints)
arm.set_state(state=0) #Start with state 0 (ready)
arm.set_gripper_mode(0) #Set the gripper mode to 0 (position control mode)

arm_speed: int = 30
tcp_speed = 30
tcp_acc = 30


def get_to_cup():
    """very beginning, going to grab the cup from the dispenser for the first time."""
    arm.set_gripper_position(700, wait=True, speed=5000, auto_enable=True)       

    arm.set_servo_angle(angle=[-31.8, 30.2, -61.2, 135.7, 71.8, -167.9], speed=arm_speed,  wait=False, radius=0.0)
    arm.set_servo_angle(angle=[-26.6, 57.3, -85.1, 135.7, 70.0, -164.8], speed=arm_speed,  wait=False, radius=0.0)
    arm.set_servo_angle(angle=[-30.0, 67.4, -95.9, 125.1, 71.4, -158.6], speed=arm_speed,  wait=False, radius=0.0)

    arm.set_gripper_position(113, wait=True, speed=5000, auto_enable=True)       


def pick_up_and_place_cup():
    """Take cup from dispenser and place it under coffee machine."""

    arm.set_servo_angle(angle=[-29.9, 58.2, -87.9, 125.1, 70.5, -158.6], speed=arm_speed,  wait=False, radius=0.0)
    arm.set_servo_angle(angle=[-27.8, 46.0, -81.3, 123.1, 64.3, -158.5], speed=arm_speed,  wait=False, radius=0.0)

    arm.set_servo_angle(angle=[-22.2, 18.6, -70.0, 133.7, 61.0, -147.7], speed=arm_speed,  wait=False, radius=0.0)
    arm.set_servo_angle(angle=[-8.8, 19.7, -47.1, 134.9, 58.9, 15.9], speed=arm_speed,  wait=False, radius=40.0)

    arm.set_servo_angle(angle=[-16.4, 42.1, -55.2, 121.0, 84.5, 6.0], speed=arm_speed, wait=False, radius=0.0)
    arm.set_servo_angle(angle=[-12.1, 42.4, -50.8, 110.9, 89.0, 6.0], speed=arm_speed, wait=False, radius=0.0)
    arm.set_servo_angle(angle=[-8.4, 42.5, -54.5, 110.9, 86.5, 8.4], speed=arm_speed, wait=False, radius=0.0)

    arm.set_gripper_position(800, wait=True, speed=5000, auto_enable=True)           


def leave_cup_move_to_button():
    """Leave cup under coffee machine and lift gripper to be in position for hitting coffee buttons."""
    arm.set_servo_angle(angle=[-15.8, 18.6, -30.7, 111.2, 76.6, 13.7], speed=arm_speed,  wait=False, radius=40.0)
    arm.set_servo_angle(angle=[-35.2, 13.6, -27.3, 88.8, 78.3, 13.7], speed=arm_speed,  wait=False, radius=40.0)
    arm.set_servo_angle(angle=[-23.5, -12.4, -27.3, 88.8, 89.6, 13.7], speed=arm_speed,  wait=False, radius=40.0)


def get_full_cup():
    """Pick up cup from the coffee machine after coffee was dispensed."""
    arm.set_servo_angle(angle=[-20.6, 18.6, -30.9, 104.5, 77.5, 11.9], speed=arm_speed,  wait=False, radius=40.0)
    arm.set_servo_angle(angle=[-0.5, 26.9, -38.7, 128.9, 78.9, 11.9], speed=arm_speed,  wait=False, radius=40.0)
    arm.set_gripper_position(300, wait=True, speed=5000, auto_enable=True)
    

def move_full_cup_to_central_spot():
    """Moves the cup of coffee to a central spot before putting it down in it's final spot 0-3."""
    arm.set_servo_angle(angle=[-2.2, 23.7, -35.8, 128.9, 78.9, 11.9], speed=arm_speed,  wait=False, radius=40.0)
    arm.set_servo_angle(angle=[-23.9, 20.3, -36.4, 92.8, 84.4, 11.9], speed=arm_speed,  wait=False, radius=40.0)
    arm.set_servo_angle(angle=[-13.5, 20.3, -33.9, 68.9, 90.8, 11.9], speed=arm_speed,  wait=False, radius=40.0)
    arm.set_servo_angle(angle=[-1.1, 12.3, -23.5, 70.3, 86.9, 11.9], speed=arm_speed,  wait=False, radius=40.0)


