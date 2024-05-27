from flask_restx import Namespace, Resource, fields
from model import User
from flask import request, jsonify, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from config import db
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from marshmallow_schema import user_schema




auth_ns = Namespace('auth', description="A namespace for our Authentication")

signup_model = auth_ns.model(
    'SignUp',
    {
        "username": fields.String(),
        "email": fields.String(),
        "password": fields.String()
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
        data = request.json

        username = data.get('username')

        db_user = User.query.filter_by(username=username).first()

        if db_user:
            return jsonify({"message": f"User with username {username} already exists"}), 409

        new_user = User(
            username=data.get('username'),
            email=data.get('email'),
            password=generate_password_hash(data.get('password'))
        )

        db.session.add(new_user)
        db.session.commit()
        result = user_schema.dump(new_user)

        return  jsonify({"message": "User created successfully", "user": result}), 201

@auth_ns.route('/login')
class Login(Resource):
    @auth_ns.expect(login_model)
    def post(self):
        data = request.json

        username = data.get('username')
        password = data.get('password')

        db_user = User.query.filter_by(username=username).first()
        
        if db_user and check_password_hash(db_user.password, password):
            access_token = create_access_token(identity=db_user.username)

            return make_response(jsonify({"message": "Login successful", "tokens": {
                "access":access_token },
                "user": user_schema.dump(db_user)}), 200)
        
        return make_response(jsonify({"error":"Invalid username or password"}), 401)
               

@auth_ns.route('/refresh')
class RefreshResource(Resource):
    def post(self):
        current_user = get_jwt_identity()
        new_access_token = create_access_token(identity=current_user)
        return jsonify({"access_token": new_access_token,
                        "user":user_schema.dump(current_user)}), 200

