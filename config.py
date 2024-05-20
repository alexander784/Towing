from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from model import db



app = Flask(__name__)
app.config['SQLACHEMY_DATABASE)URI'] = 'sqlite:///app.db'



migrate = Migrate(app,db)

db.init_app(app)






