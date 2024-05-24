from flask import jsonify
from flask_restful import Resource
# from flask_mail import Message
from config import mail





class Index(Resource):
    def get(self):
        msg = Message(
            'Hello',
            sender = 'alexander77@gmail.com',
            recipients=['lucy@gmail.com']
        )

        msg.body = 'Welcome to Towing'
        mail.send(msg)

        return "Hello World", 200