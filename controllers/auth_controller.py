from flask_restx import Namespace, Resource, fields
from model import User
from flask import request, jsonify, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from config import db
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from marshmallow_schema import user_schema

auth_ns = Namespace('auth', description="A namespace for our Authentication")

signup_model = auth_ns.model(
    'SignUp',
    {
        "username": fields.String(),
        "email": fields.String(),
        "password": fields.String(),
        "confirm_password":fields.String()
    }
)

login_model = auth_ns.model(
    'Login',
    {
        "username": fields.String(),
        "password": fields.String()
    }
)

@auth_ns.route('/signup')
class Signup(Resource):
    @auth_ns.expect(signup_model)
    def post(self):
        try:
            data = request.json  
            password = data.get('password')
            confirm_password = data.get('confirm_password')

            if password == confirm_password:
                if isinstance(password, bytes):
                    password = password.decode('utf-8')
                
                new_user = User(
                    username=data.get('username'),
                    email=data.get('email'),
                    _password_hash=generate_password_hash(password)
                )
                db.session.add(new_user)
                db.session.commit()

                return make_response(jsonify(user_schema.dump(new_user)), 201)
            
            return make_response(jsonify({"error": "Passwords must match"}))
        except ValueError as e:
            return make_response(jsonify({"error": str(e)}))

            
@auth_ns.route('/login')
class Login(Resource):
    @auth_ns.expect(login_model)
    def post(self):
        try:
            data = request.json

            username = data.get('username')
            password = data.get('password')

            db_user = User.query.filter_by(username=username).first()
            
            if db_user and db_user.verify_password(password):
                access_token = create_access_token(identity=db_user.username)
                refresh_token = create_refresh_token(identity=db_user.username)

                return make_response(jsonify({"message": "Login successful", "tokens": {
                    "access": access_token,
                    "refresh": refresh_token },
                    "user": user_schema.dump(db_user)}), 200)
        
            return make_response(jsonify({"error":"Invalid username or password"}), 401)
        except ValueError as e:
            return make_response(jsonify({"error": str(e)}), 500)



@auth_ns.route('/refresh')
class RefreshResource(Resource):
    @jwt_required(refresh=True)
    def post(self):
        current_user = get_jwt_identity()
        new_access_token = create_access_token(identity=current_user)
        return jsonify({"access_token": new_access_token}), 200

