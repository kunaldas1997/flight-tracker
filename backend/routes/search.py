from bson import Regex
from flask import Blueprint, jsonify, request
from bson.objectid import ObjectId
from flask_jwt_extended import jwt_required, get_jwt_identity

search = Blueprint("search", __name__)


@search.route("/search", methods=["GET"])
def search_form():
    from app import collection

    query = request.args.get("query")
    if not query:
        return jsonify({"message": "Empty"}), 400

    regex_query = Regex(query)
    flights = list(collection.find({"flight_number": regex_query}))

    for flight in flights:
        flight["flight_number"] = str(flight["flight_number"])
        if "_id" in flight:
            del flight["_id"]

    print(flights)
    return jsonify(flights), 200
