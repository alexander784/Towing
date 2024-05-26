from flask import request,jsonify
from flask_restx import Namespace,Resource,fields


tow_ns = Namespace("tow", description="Namespace for Tow Request")


tow_request_model = tow_ns.model(
    "Towrequest",
    {
        "location_id": fields.Integer(required=True, description="The ID location where the tow is requested"),

    }
)


    