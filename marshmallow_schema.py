from marshmallow import fields
from config import ma
from model import User, Car,Location


class UserSchema(ma.schema):
    class Meta:
        model = User

    id = fields.Int(dump_only=True)
    username = fields.Str(required=True, unique=True)
    email = fields.Email(required=True, unique=True)
    _password_hash = fields.Str(required=True)

user_schema = UserSchema()
users_schema = UserSchema(many=True)


class CarSchema(ma.Schema):
    class Meta:
        model = Car

        id = fields.Integer(dump_only=True)
        make = fields.String(required=True)
        model - fields.String(required=True)
        year = fields.Int(required=True)
        color = fields.String(required=True)
    

Car_schema = CarSchema()
cars_schema = CarSchema(many=True)

        
        
class LocationSchema(ma.Schema):
    class Meta:
        model = Location
        id = fields.Int(dump_only=True)
        place_name = fields.String(required=True)

Location_schema = LocationSchema()
Location_schema = LocationSchema(many=True)





        




