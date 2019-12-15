""" Database models file. 
Insert all tables, models and schemas for the database here."""
from flask_sqlaclhemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()


