#import SQLAlchemy from flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy

#create SQLAlchemy instance
db=SQLAlchemy()


#Create a 'Fact' Class
class Fact(db.Model):
    #set table name
    __tablename__ = 'facts'
    
    #set columns with data types
    id = db.Column(db.Integer, primary_key=True)
    submitter = db.Column(db.String(250))
    fact = db.Column(db.TEXT)
