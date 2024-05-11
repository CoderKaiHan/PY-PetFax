#import flask
from flask import Flask

#import flask_migrate-Migrate
from flask_migrate import Migrate

#import load_env
from dotenv import load_dotenv
import os

load_dotenv()

#Flask app factory
def create_app():
    #create and configure the app(Flask instance)
    app = Flask(__name__)

    sql_string = os.getenv('SQL_STRING')

    app.config['SQLALCHEMY_DATABASE_URI'] = sql_string
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    #import models foler
    from .models import models
    #initialize database to be used by app
    models.db.init_app(app)
    #Set a variable called migrate to a new instance of the Migrate class
    migrate = Migrate(app, models.db)

    #index route
    @app.route('/')
    def index():
        return 'Hello, this is PetFax!!!'
    
    #import pet blueprint
    from .blueprints import pet

    #register blueprint
    app.register_blueprint(pet.bp)

    #import pet blueprint
    from .blueprints import fact

    #register blueprint
    app.register_blueprint(fact.bp)

    #return the app
    return app