from config import app
from flask_restx import Api, Resource
from flasgger import Swagger
from controllers.auth_controller import auth_ns
from controllers.tow_request import tow_ns

swagger = Swagger(app)

api = Api(app)
api.add_namespace(auth_ns, path="/auth")
api.add_namespace(tow_ns, path="/tow")

class Index(Resource):
    def get(self):
        return "Welcome to Towing"

api.add_resource(Index, "/")

if __name__ == "__main__":
    app.run(port=5555, debug=True)
