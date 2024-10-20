# run this file as a script to get information out of the database / modify it as needed
# we're using relative imports, which means python3 should run this script as part of the website module
# to do this, use 
# python3 -m website.db_utility

# this script was written using https://www.perplexity.ai/search/run-this-file-as-a-script-to-g-Q.6XBr3eREmKlh_fqAdZIA
# security considerations for this utility script https://www.perplexity.ai/search/this-is-a-script-i-wrote-for-a-hh39j794QXC1YDW4iGEmXw

from .models import User, Note
from . import db 
from . import create_app

def get_user_info(input_email, make_app_function): 
    app = make_app_function()
    with app.app_context(): 
        user = User.query.filter_by(email=input_email).first()
        
        if user: 
            print(f"user id {user.id}")
            print(f"user email {user.email}")
            print(f"user first name {user.first_name}")
        else: 
            print(f"No user exists for the given email")
    


def main(): 
    get_user_info('tim@gmail.com', create_app)


if __name__ == '__main__': 
    main() 
