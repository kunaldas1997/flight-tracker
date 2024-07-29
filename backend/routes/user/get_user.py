# This is for admin purpose only
# This returns an access token, which will be used to insert
# flight data


from flask import Blueprint, request, jsonify
import hashlib

from flask_jwt_extended import create_access_token
get_user = Blueprint("get_user", __name__)

@get_user.route("/signin", methods=['POST'])
def get():
    from app import usercollection
    data  = request.json
    user = usercollection.find_one({"user": data["user"]})
    
    if user:
        enc_pass = hashlib.sha256(data['password'].encode("utf-8")).hexdigest()
        if(enc_pass == user['password']):
            access_token = create_access_token(identity=data['user'])
            return jsonify(access_token = access_token), 200

        return jsonify({'error': "Creds are wrong"})
    return jsonify({'error': "User not found"})