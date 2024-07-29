# This is just for admin purpose
# This a new user can be created.

from flask import Blueprint, request, jsonify
import hashlib
create_user = Blueprint("create_user", __name__)

@create_user.route("/signup", methods=['POST'])
def create():
    from app import usercollection
    data  = request.json
    
    if data:
        user_exist_in_db = usercollection.find_one({'user':data['user']})
        if not user_exist_in_db:
            data['password'] = hashlib.sha256(data['password'].encode("utf-8")).hexdigest()
            usercollection.insert_one(data)
            return jsonify({'info': "User added"}), 200
        return jsonify({'error': 'user exists'}), 409
    return jsonify({'message': "Empty Data passed"}), 404