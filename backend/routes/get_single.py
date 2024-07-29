# This is for admin purpose
# This is for the admin to get the one single flight 


from flask import Blueprint, jsonify
from bson.objectid import ObjectId
from flask_jwt_extended import jwt_required, get_jwt_identity

get_single_route = Blueprint("get_single_route", __name__)


@get_single_route.route("/flight/<flight_number>", methods=["GET"])
@jwt_required()
def get_item(flight_number):
    from app import collection

    current_user = get_jwt_identity()
    print(current_user)
    query = {"flight_number": str(flight_number)}

    if current_user:
        item = collection.find_one(query)
        if item:
            if isinstance(item.get("_id"), ObjectId):
                item["_id"] = str(item["_id"])
                item["flight_number"] = item["flight_number"]
                item["src"] = item["src"]
                item["dest"] = item["dest"]
                item["dept"] = item["dept"]
                item["arr"] = item["arr"]
                item["status"] = item["status"]
                
            return jsonify(item), 200
        else:
            return jsonify({"message": "Item not found"}), 404
        
    return jsonify({'auth_err': "Authentication error"})
