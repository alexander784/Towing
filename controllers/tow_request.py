from flask import request,jsonify
from flask_restx import Namespace,Resource,fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from config import db
from model import User,Location,TowRequest
from marshmallow_schema import Tow_schema


tow_ns = Namespace("tow", description="Namespace for Tow Request")


tow_request_model = tow_ns.model(
    "Towrequest",
    {
        "location_id": fields.Integer(required=True, description="The ID location where the tow is requested"),

    }
)

@tow_ns.route("/request")
class TowRequestResource(Resource):
    @tow_ns.expect(tow_request_model)
    @jwt_required()
    def post(self):
        data = request.json
        location_id = data.get("location_id")

        user_identity = get_jwt_identity()
        user = User.query.filter_by(username=user_identity).first()

        if not user:
            return jsonify({"message":"User not found"}), 404
        
        location = Location.query.get(location_id)
        if not location:
            return jsonify({"message":"Invalid location ID"}), 400
        
        new_tow_request = TowRequest(location_id=location_id,user_id=user.id)
        db.session.add(new_tow_request)
        db.session.commit()

        result = Tow_schema.dump(new_tow_request)


        return jsonify({"message":"Tow request submitted successfully"}),201
        


    