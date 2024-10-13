from flask import Blueprint 

views = Blueprint('views', __name__)

# you are at 20min in the youtube video 


# making the first view 
@views.route('/')
def home():
    return "<h1> this is a flask application</h1>"
