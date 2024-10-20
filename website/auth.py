from flask import Blueprint, render_template, request, flash

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
            # creating new user accounts
            

            flash('account created!!', category='success')


        


    return render_template('sign_up.html')



