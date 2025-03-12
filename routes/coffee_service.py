from flask import Blueprint, jsonify, request
from model.coffee_model import coffee_db

coffee_blueprint = Blueprint('coffee_blueprint', __name__)



@coffee_blueprint.route('/coffee', methods=['GET'])
def get_all_coffees():
    return jsonify(list(coffee_db.values())), 200



@coffee_blueprint.route("/coffee/<int:coffee_id>", methods=['GET'])
def get_coffee_by_id(coffee_id):
    coffee = coffee_db.get(coffee_id)
    if not coffee:
        return jsonify({"message": "Coffee not found"}), 404
    return jsonify(coffee), 200




@coffee_blueprint.route("/coffee", methods=['POST'])
def create_coffee():
    data = request.json
    new_id = max(coffee_db.keys(), default=0) + 1
    new_coffee = {
        "id": new_id,
        "name": data.get("name"),
        "product": data.get("product"),
        "ingredients": data.get("ingredients", []),
        "sold": data.get("sold", 0),
    }

    coffee_db[new_id] = new_coffee
    return jsonify(new_coffee), 201




@coffee_blueprint.route("/coffee/<int:coffee_id>", methods=["PUT"])
def update_coffee(coffee_id):
    if coffee_id not in coffee_db:
        return jsonify({"error": "Coffee not found"}), 404

    data = request.json
    coffee_db[coffee_id].update({
        "name": data.get("name", coffee_db[coffee_id]["name"]),
        "product": data.get("product", coffee_db[coffee_id]["product"]),
        "ingredients": data.get("ingredients", coffee_db[coffee_id]["ingredients"]),
        "sold": data.get("sold", coffee_db[coffee_id]["sold"]),
    })

    return jsonify(coffee_db[coffee_id]), 200




@coffee_blueprint.route("/coffee/<int:coffee_id>", methods=["DELETE"])
def delete_coffee(coffee_id):
    if coffee_id not in coffee_db:
        return jsonify({"error": "Coffee not found"}), 404

    del coffee_db[coffee_id]
    return jsonify({"message": "Coffee deleted successfully"}), 200