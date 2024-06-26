from flask import Flask, request, jsonify

import sys
sys.path.append('../')
from main import main
from coffee_types import Coffee
from syrup_types import Syrup
from main import final_place_number

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

# class Coffee(Enum):
#    ESPRESSO = "ESPRESSO"
#    MACCHIATO = "MACCHIATO"
#    LATTE = "LATTE"
#    CAPPUCINO = "CAPPUCINO"
#    FLAT_WHITE = "FLAT WHITE"
#    TEA= "TEA"
#    AMERICANO= "AMERICANO"

@app.route("/order_coffee", methods=["POST"])
def order_coffee():
    data = request.json
    coffee_type = data.get("coffee_type")
    syrup_type = data.get("syrup_type")
    syrup_order = Syrup.NONE
    coffee_order = Coffee.ESPRESSO

    if coffee_type: 
        coffee_order = Coffee[coffee_type.upper().replace(" ", "_")]
    else:
        return jsonify({"error": "Coffee type is required"}), 400
    if syrup_type:
        syrup_order = Syrup[syrup_type.upper()]
    else:
        syrup_type = Syrup.NONE

    main(coffee_order, syrup_order)
    return jsonify(f"spot{final_place_number}")
        

if __name__ == "__main__":
    app.run(debug=True)
