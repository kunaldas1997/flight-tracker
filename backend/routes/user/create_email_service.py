# This module gets the data from user via a form.
# After the data is passed to this interface, the data is saved to a topic db 
# which stores email id of the already existing topcs

from flask import Blueprint, request, jsonify


create_email_notif = Blueprint("create_email_notif", __name__)


@create_email_notif.route("/create_notif", methods=["POST"])
def create_notif():
    from app import topicCollection

    data = request.json
    flight_number = data["flight_number"]
    user_email = data["email"]
    if not flight_number or not user_email:
        return jsonify({"message": "Data Is Empty"})
    else:

        # Find the flight document
        flight = topicCollection.find_one({"flight_number": flight_number})

        # Check if the user email is already in the users array
        if flight and user_email in flight.get("users", []):
            return jsonify({"message": "Email already subscribed"})

        # Add the user to the flight's users array or create a new flight document
        topicCollection.update_one(
            {"flight_number": flight_number},
            {"$addToSet": {"users": user_email}},
            upsert=True,
        )

        return jsonify(
            {"message": "You will receive an email if there is any change to status"}
        )
