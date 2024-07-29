# This is an update api.
# once you get the flight, you can perform  PATCH request for following:
#
# arr: Arrival time
# dept: Departure time
# gate: Gate Number
# status: Flight Status
# 


from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from bson.objectid import ObjectId

update_data_route = Blueprint("update_data_route", __name__)


# after update is complete, it will send data to Firebase abou the changes, to push a notification to ReactAPP
@update_data_route.route("/flight/<flight_number>", methods=["PATCH"])
@jwt_required()
def update_data(flight_number):
    from app import collection
    from app import topicCollection

    data = request.json
    current_user = get_jwt_identity()

    if current_user:
        result = collection.update_one({"flight_number": flight_number}, {"$set": data})
        registered_emails = topicCollection.find_one(
            {"flight_number": flight_number}, {"users": 1}
        )
        if result.matched_count:
            from .user.push.send_email import send_mail

            for user in registered_emails["users"]:
                print(type(data["status"]))
                if data["status"] == "On Time":
                    status = data["status"]
                    receiver = user
                    data = f"""
                    <p>Hi</p>
                    <p>Your flight <strong>{flight_number}</strong> is running on time. We will notify you once boarding starts! </p>
                    <p>Thanks</p>"""
                    send_mail(receiver, status, data)
                    

                elif data["status"] == "Rescheduled" and (
                    "dept" in data or "arr" in data
                ):
                    status = data["status"]
                    receiver = user

                    departure_info = (
                        f" <strong>Departure time is {data['dept']}.</strong>"
                        if "dept" in data
                        else ""
                    )
                    arrival_info = (
                        f"<strong>Arrival time is {data['arr']}.</strong>"
                        if "arr" in data
                        else ""
                    )

                    data = f"""
                    <p>Hi,</p>
                    <p>Your flight <strong>{flight_number}</strong> is Rescheduled.{departure_info}. {arrival_info} We will notify you once boarding starts!</p>
                    <p>Thanks</p>
                    """
                    send_mail(receiver, status, data)

                elif data["status"] == "Cancelled":
                    status = data["status"]
                    receiver = user
                    data = f"""
                    <p>Hi</p>
                    <p>Your Flight <strong>{flight_number}</strong> is cancelled. Please contact ticket counter for alternatives.</p>
                    <p>Thanks</p>
                    """
                    send_mail(receiver, status, data)

                elif data["status"] == "Boarding" and ("gate" in data):
                    status = data["status"]
                    receiver = user
                    data = f"""
                    <p>Hi</p>
                    <p>Boarding for your Flight <strong>{flight_number}</strong> has started. Please proceed to <strong>{data["gate"]}</strong> for boarding.</p>
                    <p>Thanks</p>
                    """
                    send_mail(receiver, status, data)

                elif data["status"] == "Gate Change" and ("gate" in data):
                    status = data["status"]
                    receiver = user
                    data = f"""
                    <p>Hi</p>
                    <p>Gate for your flight <strong>{flight_number}</strong> has changed. Please proceed to <strong>{data["gate"]}</strong> for boarding.</p>
                    <p>Thanks</p>
                    """
                    send_mail(receiver, status, data)

    else:
        return jsonify({"auth_err": "Authentication error"})
    return jsonify({"message": "Success"})
