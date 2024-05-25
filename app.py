from config import app
from flask_restful import Api,Resource
from flask import Flask, jsonify,make_response
from flasgger import Swagger
from controllers import auth_controller
from controllers import user_controller



api = Api(app)
swagger = Swagger(app)

api.add_resource(auth_controller)
api.add_resource(user_controller)





class Index(Resource):
    def get(self):
        return "Welcome to Towing "
    
api.add_resource(Index, "/")


if __name__ == "__main__":
    app.run(port=5555, debug=True)