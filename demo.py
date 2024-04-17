#Template for controlling the xArm using the xArm Python SDK

from xarm.wrapper import XArmAPI #Import the xArmAPI class from the xArm Python SDK

ip = "192.168.1.215" #Change this to your xArm IP address

#Initialize the xArm with the following parameters:
arm = XArmAPI(ip)
arm.motion_enable(enable=True)
arm.set_mode(0) #Set the mode to 0 (position control mode for x, y, z, roll, pitch, yaw) OR set the mode to 1 (servo control mode for 6 joints)
arm.set_state(state=0) #Start with state 0 (ready)
arm.set_gripper_mode(0) #Set the gripper mode to 0 (position control mode)


#Here is an example of the arm moving to 3 positions sequentially, then opening, then closing the gripper
#Change the x, y, z, roll, pitch, yaw, and speed based on your operation. wait=True will make the program wait until the arm finishes the movement before moving to the next line of code

arm.set_position(x=378, y=254, z=355, roll=-180, pitch=0, yaw=-29.9, speed=100, is_radian=False, wait=True)

arm.set_position(x=300, y=200, z=355, roll=-180, pitch=0, yaw=-29.9, speed=100, radius=0, is_radian=False, wait=True)

arm.set_position(x=250, y=254, z=355, roll=-180, pitch=0, yaw=-29.9, speed=100, radius=0, is_radian=False, wait=True)

arm.set_gripper_position(850, wait=True) #This sets the gripper position to 850 (fully open)
arm.set_gripper_position(0, wait=True) #This sets the gripper position to 0 (fully closed)

#Here is an example of the arm moving to 2 positions sequentially using joint angles, then opening and closing the gripper
#Use this method if you want to control the arm using joint angles instead of x, y, z, roll, pitch, yaw
#Change the angles and speed based on your operation. Each angle in the list corresponds to a joint angle from 1 to 6 (in degrees)

arm.set_servo_angle(angle=[0, 0, 0, 0, 0, 0], speed=100, wait=True) #Move to the home position

arm.set_servo_angle(angle=[0, 0, 0, 0, 0, 90], speed=100, wait=True) #Move to a new position

arm.set_gripper_position(850, wait=True) #This sets the gripper position to 850 (fully open)
arm.set_gripper_position(0, wait=True) #This sets the gripper position to 0 (fully closed)


arm.disconnect() #Disconnect the arm after the program is finished. You may not need to do this if you are running multiple programs sequentially


#Use these commands to control the robot as needed. You can find more commands in the xArm Python SDK documentation
