from flask import Blueprint, render_template

views = Blueprint('views', __name__)

# you are at 20min in the youtube video 


# the home view     
@views.route('/')
def home():
    return render_template('home.html') 
