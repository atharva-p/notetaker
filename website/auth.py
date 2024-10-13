from flask import Blueprint 

auth = Blueprint('auth', __name__)

# defining the auth blueprint 
@auth.route('/auth')
def authentication(): 
    return "<h1><u> this will hold the authentication page</u></h1>"