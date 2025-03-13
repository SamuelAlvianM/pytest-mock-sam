from flask import Blueprint, jsonify, request
from model.coffee_model import customer_db

cust_blueprint = Blueprint('cust_blueprint', __name__)



@cust_blueprint.route('/customer-site', methods=['GET'])
def get_all_cust():
    return jsonify(list(customer_db.values())), 200


@cust_blueprint.route("/customer-site/<int:customer_id>", methods=['GET'])
def get_cust_by_id(customer_id):
    customer = customer_db.get(customer_id)
    if not customer:
        return jsonify({"message": "Coffee not found"}), 404
    return jsonify(customer), 200

@cust_blueprint.route("/coffee", methods=['POST'])
def create_coffee():
    data = request.json
    new_id = max(customer_db.keys(), default=0) + 1
    new_coffee = {
        "id": new_id,
        "name": data.get("name"),
        "product": data.get("product"),
        "ingredients": data.get("ingredients", []),
        "sold": data.get("sold", 0),
    }

    coffee_db[new_id] = new_coffee
    return jsonify(new_coffee), 201

@cust_blueprint.route("/coffee/<int:customer_id>", methods=["PUT"])
def update_coffee(customer_id):
    if customer_id not in customer_db:
        return jsonify({"error": "Coffee not found"}), 404

    data = request.json
    customer_db[customer_id].update({
        "name": data.get("name", customer_db[customer_id]["name"]),
        "product": data.get("product", customer_db[customer_id]["product"]),
        "ingredients": data.get("ingredients", customer_db[customer_id]["ingredients"]),
        "sold": data.get("sold", customer_db[customer_id]["sold"]),
    })

    return jsonify(customer_db[customer_id]), 200