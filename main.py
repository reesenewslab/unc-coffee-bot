"""Main file where everything will be!."""


from drinks import make_coffee
from syrups import pump_syrup
from final_spots import spot0, spot1, spot2, spot3
from common_functions import open_gripper
from xarm.wrapper import XArmAPI
from enum import Enum


ip = "192.168.1.213" #Change this to your xArm IP address

#Initialize the xArm with the following parameters:
arm = XArmAPI(ip)
arm.motion_enable(enable=True)
arm.set_mode(0) #Set the mode to 0 (position control mode for x, y, z, roll, pitch, yaw) OR set the mode to 1 (servo control mode for 6 joints)
arm.set_state(state=0) #Start with state 0 (ready)
arm.set_gripper_mode(0) #Set the gripper mode to 0 (position control mode)

arm_speed: int = 50


#enums to store coffee and syrup types that will come in from the json. numbers will likely be replaced with whatever the value from the json is called
class Coffee(Enum):
   ESPRESSO = "ESPRESSO"
   DOUBLE_ESPRESSO = "DOUBLE ESPRESSO"
   LATTE = "LATTE"
   CAPPUCINO = "CAPPUCINO"
   FLAT_WHITE = "FLAT WHITE"
   TEA= "TEA"


class Syrup(Enum):
   VANILLA = "VANILLA"
   CARAMEL =2
   NONE =  "NONE"

# no idea the actual data type but lets assume string. this is what robot will press
coffee_type: Coffee = Coffee.ESPRESSO

# type of syrup, includes none
syrup: Syrup = Syrup.VANILLA

#wait time for each coffee type
wait_times: float = 0

# out of 3 (0,1,2,3), will be moduloed in the loop to keep it on a cycle
final_place_number: int = 0


def dispense_cup():
   """Dispense the cup. runs the blockly the grabs the cup"""
   return None


def move_to_machine():
   """Move the dispensed cup to the spot under the coffee machine via blockly"""
   return None


def drop_cup_at_machine():
   """Place cup under coffee machine."""
   return None


def get_cup_fom_machine():
   """Pick up cup from machine."""
   return None


def select_coffee(coffee_type: Coffee):
   make_coffee(coffee_type)


def select_syrup(syrup: Syrup):
   """Place cup under the correct syrup"""
   if syrup == Syrup.NONE:
      return None
   else:
        pump_syrup()


def move_to_central_location():
   """Move the dispensed cup to a central location"""
   return None


def move_to_final_location():
   """Place the cup in the final spot depending on what spot has been used last."""
   # this will increase the place to the next place and keep it to max 4 with mod! spots are 0-4
   global final_place_number
   final_place_number = (final_place_number + 1) % 4
   if final_place_number == 0:
      spot0()
   elif final_place_number == 1:
      spot1()
   elif final_place_number == 2:
      spot2()
   elif final_place_number == 3:
     spot3()
   open_gripper()
     


def main():
   """Execute all of the functions to make the coffee!"""
   dispense_cup()
   move_to_machine()
   drop_cup_at_machine()
   select_coffee(coffee_type)
   get_cup_fom_machine()
   select_syrup(syrup)
   move_to_central_location()
   move_to_final_location()


if __name__ == "__main__":
   main()

