# models for the sql alchemy database 

# get the db instance from current package, and other dependencies 
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model): 
    id = db.Column(db.Integer, primary_key = True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())

    # this requires a foreign key to set up the relationship
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    

# creating the models (from which tables will be created)
class User(db.Model, UserMixin):
    # following attributes will be converted into columns of the table 
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150))

    # unique makes sure that an email can appear only once in the column, but the field can be null (unlike primary key)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))

    # creating the one to many relationship
    notes = db.relationship('Note')

    
