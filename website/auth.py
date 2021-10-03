from flask import Blueprint 

## blueprint means it has a bunch of url's defined. seperate output ###

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return "<p>Login</p"

@auth.route('/logout')
def logout():
    return "<p>logout</p"

@auth.route('/sign-up')
def sign_up():
    return "<p>Sign Up</p"