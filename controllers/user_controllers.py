from flask import Blueprint, jsonify, make_response,request
from flask_restful import Api,Resource
from model import User




user_bp = Blueprint("user_bp", __name__)


class Users(Resource):
    def get(self):
        users = User.query.all()
        return make_response(jsonify(users))
