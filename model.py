from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from config import db
from werkzeug.security import check_password_hash,generate_password_hash


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    _password_hash = db.Column(db.String(120),unique=True, nullable=False)
    tow_requests = db.relationship('TowRequest', backref='author', lazy=True)

    def verify_password(self, password):
        return check_password_hash(self._password_hash, password)
    def set_password(self, password):
            self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @classmethod
    def get_user_by_username(cls, username):
        return cls.query.filter_by(username=username).first()
        
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(100), nullable=False)
    model = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    color = db.Column(db.String(50), nullable=False)

class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    place_name = db.Column(db.String(200), nullable=False)
    tow_requests = db.relationship('TowRequest', backref='location', lazy=True)

class TowRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'), nullable=False)
    date_requested = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
