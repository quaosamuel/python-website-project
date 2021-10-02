##### initialize flask #############

from flask import Flask as fl

#### function to setup and create flask ###########

def create_app():
    app = fl(__name__) ## __name__ is just how flask is initialized
    app.config['SECRET_KEY'] = 'Sweety12@' ## SECRET_KEY ecryptys cookies and session data##

    return app

    