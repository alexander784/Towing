from config import app
from flask_restful import Api

api = Api(app)



if __name__ == "__main__":
    app.run(port=5000, debug=True)