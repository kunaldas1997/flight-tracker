# This is for homepage
# Gets data of all flights

from flask import Blueprint, request, jsonify

get_data_route = Blueprint("get_data_route", __name__)


@get_data_route.route("/", methods=["GET"])
def get_data():
    from app import collection

    items = list(collection.find({}))
    for item in items:
        item['_id'] = str(item['_id'])
    if items :
        return jsonify(items), 200
    return jsonify({"message": "Item not found"}), 404
