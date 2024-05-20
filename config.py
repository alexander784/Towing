from flask import Flask




app = Flask(__name__)
app.config['SQLACHEMY_DATABASE)URI'] = 'sqlite:///app.db'



