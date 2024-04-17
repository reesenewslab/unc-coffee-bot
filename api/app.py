from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/order_coffee", methods=["POST"])
def order_coffee():
    data = request.json
    coffee_type = data.get("coffee_type")
    syrup_type = data.get("syrup_type")

    if coffee_type:
        drink_ordered = {"coffee_type": coffee_type}

        if syrup_type:
            drink_ordered["syrup_type"] = syrup_type

        return jsonify(f"You ordered {coffee_type} with {syrup_type}")
    else:
        return jsonify({"error": "Coffee type is required"}), 400

if __name__ == "__main__":
    app.run(debug=True)
