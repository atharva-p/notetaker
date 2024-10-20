from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from os import path
from flask_login import LoginManager

# database should be created outside of the context of the create_app function
# initialize
db = SQLAlchemy()

# set database attributes 
DB_NAME = 'database.db'

def create_app(): 
    app = Flask(__name__.split('.')[0])
    app.config['SECRET_KEY'] = '\xf0?a\x9a\\\xff\xd4;\x0c\xcbHi'

    # configuring the database 
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_NAME}"
    db.init_app(app)

    # login manager to keep the login settings and use flask_login api 
    login_manager = LoginManager(app)

    # the default view (endpoint / route) to send the user to in case of unauthorized actions
    login_manager.login_view = 'auth.login'

    # get the blueprints here first 
    from .views import views
    from .auth import auth

    # registering the blueprints from views 
    app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(auth, url_prefix='/')

    # import to make sure that they are loaded and then call the create database function
    # sql alchemy knows about the user and the note tables (classes) since we're importing them and 
    # both of them inherit the db.Model class. when you import modules in python, all of the variables
    # classes and function definitions are initialised (but the functions themselves aren't run) 
    from .models import User, Note
    create_database(app)

    # to set up the login manager
    from .models import User, Note
    
    # set the user_loader so that we can restore the user login from the previous session
    @login_manager.user_loader
    def get_user(input_id):
        user = User.query.get(int(input_id))
        return user

    return app


# check if the database exists, if it doesn't make it. 
# we provide it the app instance so that it has context of the application
def create_database(app):
    if not path.exists('website/' + DB_NAME): 
        with app.app_context(): 
            db.create_all()
