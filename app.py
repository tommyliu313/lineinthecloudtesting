# What we need to import
from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float
import os
import sqlite3
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from flask_mail import Mail, Message
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField , BooleanField , SubmitField
from wtforms.validators import DataRequired

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

# Convert to JSON
def changetojson():
    return

# Automatically DB action
def createdb(name,):
    return 

# Cookies Settings
# create
def create_cookies():
  i = setcookie(name)
#delete
def delete_cookies():    

#Data Import


# Information loaded into json format file
@app.route('x',methods=['GET','POST'])
def FunctionName(args):
    if request.method == 'POST':

        if os.path.exists('.json'):
            with open('.json') as :
                = json.load()

   
#HTTP Redirection    


if __name__ == '__main__':
    app.run()

#Input


#Page Navigation

#Console test/ HTTP Testing status
def itisok():
    return jsonify(message =''),200 # output msg , relative status code
    


//