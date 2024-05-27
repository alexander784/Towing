from marshmallow import fields,Schema
from config import ma
from model import User, Car,Location,TowRequest


class UserSchema(ma.Schema):
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
        make = fields.Str(required=True)
        model = fields.Str(required=True)
        year = fields.Int(required=True)
        color = fields.Str(required=True)
    

Car_schema = CarSchema()
cars_schema = CarSchema(many=True)

        
        
class LocationSchema(ma.Schema):
    class Meta:
        model = Location
        id = fields.Int(dump_only=True)
        place_name = fields.Str(required=True)

Location_schema = LocationSchema()
Location_schema = LocationSchema(many=True)

class TowRequestSchema(ma.Schema):
    class Meta:
        Model = TowRequest
        id = fields.Int(dump_only=True)
        location_id = fields.Str(required=True)
        date_requested = fields.Int(required=True)

Tow_schema = TowRequestSchema()
Tow_schema = TowRequestSchema(many=True)






        




