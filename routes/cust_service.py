from flask import Blueprint, jsonify, request
from model.coffee_model import coffee_db

cust_blueprint = Blueprint('cust_blueprint', __name__)



@cust_blueprint.route('/customer-site', methods=['GET'])
def get_all_coffees():
    return jsonify(list(coffee_db.values())), 200