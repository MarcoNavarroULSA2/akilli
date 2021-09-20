# init.py

from flask import Flask, app, render_template, json, request, redirect
#from flask_login import LoginManager 
from include.EmpleadoDAO import EmpleadoDAO

def create_app():
    app = Flask(__name__, static_url_path='', static_folder='../static/')

    #login_manager = LoginManager()
    #login_manager.login_view = 'auth.login'
    #login_manager.init_app(app)

    #from .models import Empleado

    #@login_manager.user_loader
    #def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        #return Empleado.query.get(int(user_id))

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

if __name__ == "__main__":
    app.run()