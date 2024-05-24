from flask import Blueprint, jsonify, make_response,request
from flask_restful import Api,Resource
from model import User




user_bp = Blueprint("user_bp", __name__)
api = Api(user_bp)

class Users(Resource):
    def get(self):
        users = User.query.all()
        return make_response(jsonify(users))
    

class UserById(Resource):
    def get(self,user_id):
        user = User.query.filter_by(id=user_id).first()

        if not user:
            return make_response(jsonify({"error":"User not found"}), 400)
        
        return make_response(jsonify())
    
        
    