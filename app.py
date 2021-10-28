from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float
import os
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from flask_mail import Mail, Message

app = Flask(__name__)

db = SQLAlchemy(app)
ma = Marshmallow(app)
jwt = JWTManager(app)
mail = Mail(app)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.cli.command('db_create')
def db_create():
    db.create_all()
    print('Create a database')


@app.cli.command('db_drop')
def db_drop():
    db.drop_all()
    print('Drop a database!')


if __name__ == '__main__':
    app.run()
