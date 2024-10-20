from flask import Blueprint, render_template
from flask_login import login_required 

# get the current_user variable from flask login 
# current_user is a proxy for the currently active user
# since this current_user is an object of User, it will have the UserMixin functions
from flask_login import current_user

views = Blueprint('views', __name__)

# the home view     
@views.route('/')
@login_required
def home():
    return render_template('home.html', user = current_user) 
