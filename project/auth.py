# auth.py

from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from include.EmpleadoVO import EmpleadoVO
from include.EmpleadoDAO import EmpleadoDAO
from include.LogIn_VO import LogInVO
from include.LogIn_DAO import LogInDAO

auth = Blueprint('auth', __name__)

@auth.route("/")
def index():
    return "<h1>Inicio MVC</h1>"

@auth.route("/index")
def iniciar():
    return render_template("index.html")

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    
    email = request.form.get('email')
    password = request.form.get('password')
    #remember = True if request.form.get('remember') else False

    #user = Empleado.query.filter_by(email=email).first()
    user = LogInVO(email, password)
    
    loginDAO = LogInDAO()  
    listaVO = loginDAO.selectALL(user)
    print(listaVO.__len__())
    #Si es igual a cero no encontro el usuario
    if listaVO.__len__() == 0: 
        #flash('Please check your login details and try again.')
         return render_template('login.html', msg='Wrong user or password')#return redirect(url_for('auth.login')) # if user doesn't exist or password is wrong, reload the page
    # check if user actually exists
    # take the user supplied password, hash it, and compare it to the hashed password in database
    #if not user or not check_password_hash(user.password, password): 
     #   flash('Please check your login details and try again.')
      #  return redirect(url_for('auth.login')) # if user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    #login_user(user, remember=remember)
    return redirect(url_for('main.menu'))

@auth.route('/registrarse')
def registrarse():
    return render_template('registrarse.html')

@auth.route('/registrarse', methods=['POST'])
def registrarse_post():

    nombrecompleto = request.form.get('nombrecompleto')
    email = request.form.get('email')
    password = request.form.get('password')
    telefono = request.form.get('tel')
    empresa = request.form.get('empresa')


    empleadoDAO = EmpleadoDAO()   
    listaVO = empleadoDAO.findEmail(email)
    print(listaVO.__len__())
    #Si es igual a cero no encontro el usuario
    if listaVO.__len__() > 0: 
         return render_template('registrarse.html', msg='El email ya existe')

    #user = Empleado.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

    #if user: # if a user is found, we want to redirect back to signup page so user can try again  
        #flash('Email address already exists')
        #return redirect(url_for('auth.registrarse'))

    # create new user with the form data. Hash the password so plaintext version isn't saved.
    #password=generate_password_hash(password, method='sha256')
    new_user = EmpleadoVO(nombrecompleto, email, password, telefono, empresa)

    # add the new user to the database    
    empleadoDAO.insertALL(new_user)

    return redirect(url_for('auth.login'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))