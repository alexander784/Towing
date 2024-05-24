from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from model import db
from dotenv import load_dotenv
# from flask_mail import Mail
import os


load_dotenv()


app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# mail = Mail(app)
migrate = Migrate(app,db)

db.init_app(app)






