from config import app
from flask_restful import Api,Resource
from flask import Flask, jsonify,make_response
from flasgger import Swagger


api = Api(app)
swagger = Swagger(app)




class Index(Resource):
    def get(self):
        return "Welcome to Towing "
    
api.add_resource(Index, "/")


if __name__ == "__main__":
    app.run(port=5555, debug=True)