from flask import Blueprint, jsonify, make_response,request
from flask_restful import Api,Resource
from model import User,db
from marshmallow_schema import user_schema, users_schema




user_bp = Blueprint("user_bp", __name__)
api = Api(user_bp)

class Users(Resource):
    def get(self):
        users = User.query.all()
        return make_response(jsonify(users_schema.dump(users)), 200)
    

class UserById(Resource):
    def get(self,user_id):
        user = User.query.filter_by(id=user_id).first()

        if not user:
            return make_response(jsonify({"error":"User not found"}), 400)
        
        return make_response(jsonify(user_schema.dump(user)), 200)

    def patch(self, user_id):
        user = User.query.filter_by(id=user_id).first()

        if not user:
            return make_response(jsonify({"error":"User not found"}), 400)
        
        try:
             data = request.get_json()

             for attr in data:
                 setattr(user, attr, data.get(attr))

             db.session.commit()
             return make_response(jsonify(user_schema.dump(user)), 200)
        
        except ValueError as e:
            return make_response(jsonify({"error": [str(e)]}))
        
    def delete(self, user_id):
        user = User.query.filter_by(id=user_id).first()

        if not user:
            return make_response(jsonify({"error":"USer not found"}), 400)
        db.session.delete(user)
        db.session.commit()

        return make_response(jsonify ({
            "success":True,
            "message": "USer deleted successfully"
        }), 204)
    
api.add_resource(Users, "/users")
api.add_resource(UserById, "/users/<int:user_id>")

    