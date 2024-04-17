"""Main file where everything will be!."""


from drinks import make_coffee
from syrups import pump_syrup
from final_spots import spot0, spot1, spot2, spot3
from common_functions import open_gripper
from enum import Enum
from common_functions import open_gripper, get_full_cup, get_to_cup, pick_up_and_place_cup, leave_cup_move_to_button, move_full_cup_to_central_spot

#TODO: set arm speed across the files 
#TODO: figure how much movign goes before syrups
#TODO: set syrup TCP speed -- and make syrup multipe functions??
#TODO: set IP address
#TODO: create final place to go before restarting again
#TODO: how many syrups will we have
#TODO: finalize click right
#TODO: get wait times for each drink. where to add

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
   CARAMEL = 2
   NONE =  "NONE"

# no idea the actual data type but lets assume string. this is what robot will press
coffee_type: Coffee = Coffee.ESPRESSO

# type of syrup, includes none
syrup: Syrup = Syrup.VANILLA

#wait time for each coffee type
wait_times: float = 0

# out of 3 (0,1,2,3), will be moduloed in the loop to keep it on a cycle
final_place_number: int = 0


def cup_intro_sequence():
   """First three function that remove the cup, place it in front of the coffee machine and leave the cup to hit the button."""
   get_to_cup()
   pick_up_and_place_cup()
   leave_cup_move_to_button()


def get_cup_fom_machine():
   """Pick up cup from machine."""
   get_full_cup()


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
   move_full_cup_to_central_spot()


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
   cup_intro_sequence()
   select_coffee(coffee_type)
   get_cup_fom_machine()
   select_syrup(syrup)
   move_to_central_location()
   move_to_final_location()


if __name__ == "__main__":
   main()

