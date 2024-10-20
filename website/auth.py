from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User 
from werkzeug.security import check_password_hash, generate_password_hash 
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

# defining the login route 
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST': 
        # get the form data 
        email = request.form['email']
        password = request.form['password']

        # check if the user account exists by querying the email 
        user = User.query.filter_by(email = email).first()

        if user: 
            # check the password 
            authenticated  = check_password_hash(user.password, password)
            if authenticated:
                # login the user with flask login
                login_user(user, remember = True)

                flash('You have logged in', category='success')
                return redirect(url_for('views.home'))
            else: 
                flash('Incorrect password, try again', category='error')
        else: 
            flash("You do not have an account, please sign up", category='error')
            return redirect(url_for('auth.sign_up'))

    else:
        return render_template('login.html', user = current_user)


# defining the logout route 
@auth.route('/logout') 
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


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
            if User.query.filter_by(email=email).first():
                flash('user already exists, log in instead', category='error')
                return redirect(url_for('auth.login'))
            else:
                # making a user object instance
                new_user = User(first_name = first_name, email = email, password = generate_password_hash(password))

                # adding this new user to the user table
                db.session.add(new_user)
                db.session.commit()

                # login the user with flask login
                login_user(new_user, remember = True)

                flash('account created!!', category='success')

                # redirect to the home page 
                return redirect(url_for('views.home'))

        


    return render_template('sign_up.html', user = current_user)



