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