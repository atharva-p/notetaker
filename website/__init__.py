from flask import Flask 

def create_app(): 
    app = Flask(__name__.split('.')[0])
    app.config['SECRET KEY'] = 'sldfj234ljf$%23((23))'

    # get the blueprints here first 
    from .views import views
    from .auth import auth

    # registering the blueprints from views 
    app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(auth, url_prefix='/')

    return app
