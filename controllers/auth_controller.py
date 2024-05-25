from flask import jsonify,make_response
from flask_restful import Resource,request
# from flask_mail import Message
from config import mail
from model import User,db
from werkzeug.security import generate_password_hash,check_password_hash
from marshmallow_schema import user_schema
from flask_jwt_extended import create_access_token,create_refresh_token







class Index(Resource):
    def get(self):
        msg = Message(
            'Hello',
            sender = 'alexander77@gmail.com',
            recipients=['lucy@gmail.com']
        )

        msg.body = 'Welcome to Towing'
        mail.send(msg)

        return "Hello World", 200
    
class Register(Resource):
    def post(self):
        data = request.get_json()
        username = data.get("username")
        user = User.query.filter_by(username=username).first()

        if user is not None:
           return jsonify({"message":f"User with username already exists"})
        
        new_user=User(
            username = data.get("username"),
            email=data.get("email"),
            password=generate_password_hash(data.get("password"))
        )

        db.session.add(new_user)
        db.session.commit()

        return make_response(jsonify(user_schema.dump(new_user)), 201)
    

class login(Resource):
    def post(self):
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")

        user =User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):

            access_token = create_access_token(identity=user.username)
            refresh_token= create_fresh_token(identity=user.username)

            return make_response(jsonify(
                {"message": "Login successful", "tokens": {
                  "access_token": access_token,
                  "refresh_token" : refresh_token },
                  "user":user_schema.dump(user)}), 200)
        






            