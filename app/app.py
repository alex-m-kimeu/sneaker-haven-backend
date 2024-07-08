from flask import Flask, request, make_response, jsonify, flash
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity, create_access_token, create_refresh_token
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from datetime import timedelta
from dotenv import load_dotenv
import os
import cloudinary
import cloudinary.uploader
import cloudinary.api

from models import db

app = Flask(__name__)
load_dotenv()
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=int(os.getenv('JWT_ACCESS_TOKEN_EXPIRES_DAYS')))
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(days=int(os.getenv('JWT_REFRESH_TOKEN_EXPIRES_DAYS')))

cloudinary.config(
    cloud_name = os.getenv('CLOUDINARY_CLOUD_NAME'),
    api_key = os.getenv('CLOUDINARY_API_KEY'),
    api_secret = os.getenv('CLOUDINARY_API_SECRET')
)

migrate = Migrate(app, db)
db.init_app(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
api = Api(app)
CORS(app, resources={r"/*": {"origins": "*"}})

# Routes


# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=5500)