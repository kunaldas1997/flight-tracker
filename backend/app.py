from flask import Flask
from pymongo import MongoClient
import datetime
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_socketio import SocketIO


app = Flask(__name__)
jwt = JWTManager(app)
CORS(app)
socket = SocketIO(app, cors_allowed_origins="*")

# DB Setup
client = MongoClient("mongodb://localhost:27017/")
db = client["flightdb"]
collection = db["flightcollection"]
usercollection = db["user"]
topicCollection = db["topic"]

# JWT setup for admin purpose.
app.config["SECRET_KEY"] = "7ba009efe5675421daf82121d6131fe9"
app.config["TOKEN_EXP"] = datetime.timedelta(days=1)
# routes
from routes.setter import set_data_route
from routes.getter import get_data_route
from routes.get_single import get_single_route
from routes.updater import update_data_route

# import user routes
from routes.user.create_user import create_user
from routes.user.get_user import get_user
from routes.user.create_email_service import create_email_notif

# register
app.register_blueprint(set_data_route)
app.register_blueprint(get_data_route)
app.register_blueprint(get_single_route)
app.register_blueprint(update_data_route)
app.register_blueprint(create_user)
app.register_blueprint(get_user)
app.register_blueprint(create_email_notif)



if __name__ == "__main__":
    app.run(debug=True)
