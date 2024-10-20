from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User 
from werkzeug.security import check_password_hash, generate_password_hash 
from . import db

auth = Blueprint('auth', __name__)

# defining the login route 
@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

# defining the logout route 
@auth.route('/logout') 
def logout():
    return "<p> this is the log out page </p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST': 
        email = request.form['email']
        first_name = request.form['firstName']
        password = request.form['password']
        passwordConfirm = request.form['passwordConfirm']

        # error checking 
        if len(email) < 4: 
            flash('email too short', category='error')
        elif len(first_name) == 0: 
            flash('enter your first name', category='error') 
        elif password != passwordConfirm: 
            flash('passwords don\'t match', category='error')
        else: 
            # making a user object instance
            new_user = User(first_name = first_name, email = email, password = generate_password_hash(password))

            # adding this new user to the user table
            db.session.add(new_user)
            db.session.commit()

            flash('account created!!', category='success')

            # redirect to the home page 
            redirect(url_for('views.home'))

        


    return render_template('sign_up.html')



