# What we need to import
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

# Database initialization
@app.cli.command('db_create')
def db_create():
    db.create_all()
    print('Create a database')


@app.cli.command('db_drop')
def db_drop():
    db.drop_all()
    print('Drop a database!')

# Create a relationship

class Restaurant(db.Model):
    __tablename__ = 'Restaurant'


class Eater(db.Model):
    __tablename__ = 'Eater'
    eater_id = Column(Integer, primary_key=True)
    eater_name = Column(String)
    people_invited_count= Column(Integer)


class Staff(db.Model):
    __tablename__ = 'Staff'

# Error Handling

# Return a 404 page
@app.errorhandler(404)
def not_found(err):
    return render_template("404.html")

# Return a 503 error
@app.errorhandler(503)
def service_unavailable(err):
    return('503 Service Unavailable.')

#
if __name__ == '__main__':
    app.run()
