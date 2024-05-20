from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)
app.config['SQLACHEMY_DATABASE)URI'] = 'sqlite:///app.db'



migrate = Migrate(app,db)

db.init_app(app)


if __name__ == '__main__':
    app.run(port=5000)




