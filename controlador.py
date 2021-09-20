from flask import Flask, app, render_template, json, request, redirect

from include.VO import EmpleadoVO
from include.DAO import EmpleadoDAO
from include.LogIn_VO import LogInVO
from include.LogIn_DAO import LogInDAO

app = Flask(__name__, static_url_path='', static_folder='static/')

@app.route("/")
def index():
    return "<h1>Inicio MVC</h1>"

@app.route("/index")
def iniciar():
    return render_template("index.html")
    
    
#@app.route("/index",methods=["POST"])
#def iniciar2():
 #   if request.form["iniciar_s"]:
  #      return redirect("/login")
  #  return redirect("")


@app.route("/login")
def login():
    return render_template("index_login.html")

@app.route("/login",methods=["POST"])
def login2():
    try:
        DAO= LogInDAO()  
        data=request.form
        VO = LogInVO( data['email'], data['password'])
        listaVO = DAO.selectALL(VO)
        print(listaVO.__len__())
        return {
            "message": "login2 succeful"
        }    
    except Exception as e:
       return json.dumps({'error':str(e)})


@app.route("/registrarse")
def registrarse():
    return render_template("registrarse.html")

@app.route("/registrarse",methods=["POST"])
def registrarse_2():
    try:
        DAO= EmpleadoDAO()            
        data=request.form
        print(data)
        VO = EmpleadoVO( data['nombrecompleto'], data['email'], data['password'], data['tel'], data['empresa'])
        #VO.setEmpleado( data['nombrecompleto'], data['email'], data['password'], data['tel'], data['empresa'])
        DAO.insertALL(VO)
        return {
            "message": "registrarse_2 succeful"
        }    
    except Exception as e:
     return json.dumps({'error':str(e)})       


if __name__ == "__main__":
    app.run()