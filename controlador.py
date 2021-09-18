from flask import Flask, app, render_template, json, request, redirect
from include.DAO import EmpleadoDAO

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
        data=request.form
        print (data)
        
    except Exception as e:
       return json.dumps({'error':str(e)})


@app.route("/registrarse")
def registrarse():
    return render_template("registrarse.html")

#@app.route("/login",methods=["POST"])
#def login2():
  #  try:
 #       data=request.form
   #     print (data)
        
  #  except Exception as e:
 #      return json.dumps({'error':str(e)})       




if __name__ == "__main__":
    app.run()