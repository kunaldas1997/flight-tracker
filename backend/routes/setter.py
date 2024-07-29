# For admin purpose
# Needs access token to send data to server
# Does two jobs : Add new flight, and Add the same flight as a topic for user to subscribe via email.

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

set_data_route = Blueprint("set_data_route", __name__)


# only accessible to admin
@set_data_route.route("/", methods=["POST"])
@jwt_required()
def add_data():
    from app import collection
    from app import topicCollection

    data = request.json

    current_user = get_jwt_identity()
    if current_user:
        flight_in_db = collection.find_one({"flight_number": data["flight_number"]})
        if not flight_in_db:
            collection.insert_one(data)
            if not topicCollection.find_one(data["flight_number"]):
                topicCollection.insert_one(
                    {"flight_number": data["flight_number"]}, {"$set": {"users": []}}
                )
            return jsonify({"message": "Insert Success"})
        return jsonify({"message": "Flight already scheduled"})
    return jsonify({"message": "Inserted Succesfully"}), 201
