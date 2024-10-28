from flask import Blueprint, render_template, request, flash
from flask_login import login_required
# get the current_user variable from flask login 
# current_user is a proxy for the currently active user
# since this current_user is an object of User, it will have the UserMixin functions
from flask_login import current_user
from json import loads

from .models import User, Note
from . import db

views = Blueprint('views', __name__)


# the home view for the notes 
@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST': 
        # get the note from the form 
        note_data = request.form['note']


        if len(note_data) < 1: 
            flash('note is too short', category="error")
        else:
            # insert the note into the database, but we need the user_id so that we can set up the foreign key 
            # association
            # we can use the get_id() function that we inherited from the UserMixIn class
            note = Note(data = note_data, user_id = current_user.id)
            db.session.add(note)

            # DO NOT FORGET TO COMMIT WHEN YOU MAKE CHANGES TO THE DATABASE!!! 
            db.session.commit()

    

    return render_template('home.html', user = current_user) 


@views.route('/delete-note', methods=['POST'])
@login_required
def delete_note(): 
    # get the note_id from the request data (this will be in string since we're using the stringify function
    # so we will use the loads method)
    req = loads(request.data)
    note_id = req['noteId']

    # get the note from the database 
    note = Note.query.get(note_id)

    if note: 
        # only delete if belonging to the current user 
        if note.user_id == current_user.id: 
            db.session.delete(note)
            db.session.commit()
        else: 
            flash('note does not belong to you, error', category='error')
    
