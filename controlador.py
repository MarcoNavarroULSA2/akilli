from flask import Flask, app, render_template, json, request, redirect, url_for

from include.EmpleadoVO import EmpleadoVO
from include.EmpleadoDAO import EmpleadoDAO
from include.LogIn_VO import LogInVO
from include.LogIn_DAO import LogInDAO
import uuid, hashlib
import smtplib 

app = Flask(__name__, static_url_path='')
app.static_folder = 'static'

@app.route("/")
def index():
    return render_template("index.html")

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
    return render_template("login.html")

@app.route("/login",methods=["POST"])
def login2():
    #try:
    DAO= LogInDAO()  
    data=request.form
    VO = LogInVO(99,data['email'], data['password'],'' )
    listaVO = DAO.selectALL(VO)
    #print(listaVO.__len__())
    if listaVO.__len__() == 0:
        return render_template('login.html', msg='Wrong user or password')
    
    return redirect(url_for('menu'))
    #except Exception as e:
     #  return json.dumps({'error':str(e)})


@app.route("/registrarse")
def registrarse():
    return render_template("registrarse.html")

@app.route("/registrarse",methods=["POST"])
def registrarse_2():
    try:
        DAOE = EmpleadoDAO()
        DAOL = LogInDAO()            
        data=request.form
        print(data)
        sal = uuid.uuid4().hex
        VO2 = LogInVO(99, data['email'], data['password'], sal)
        #VO.setEmpleado( data['nombrecompleto'], data['email'], data['password'], data['tel'], data['empresa'])
        mensaje=DAOL.insert(VO2)
        #print("Mensaje")
        #print(mensaje['id'])
        VO = EmpleadoVO(99, data['nombrecompleto'], data['email'], data['tel'], data['empresa'], mensaje['id'], data['departamento']) 
        #print("Va el Empleado con id "+ str(VO.getIdLogin()))
        DAOE.insert(VO)
        return redirect(url_for('login'))
    except Exception as e:
     return json.dumps({'error':str(e)})       

@app.route("/menu")
def menu():
    return render_template("dashboard/menu.html")

@app.route("/settings")
def settings():
    return render_template("settings.html")

@app.route("/recuperarc",methods=["POST", "GET"])
def recuperar():
    if request.method== "POST":
        print("")
        #RECUPERAR CONTRASENA
        #recuperar correo del usuario    
        _correo= request.form["email"] 
        print(_correo)
        _DAO= LogInDAO()
        _VO= LogInVO(99, _correo,"","")      
        _bandera= _DAO.existecorreo(_VO)
        if _bandera:
            remitente = "Desde gnucita <ebahit@member.fsf.org>" 
            destinatario = "edianadecm.9@gmail.com"
            asunto = "E-mal HTML enviado desde Python" 
            mensaje = """Hola!<br/> <br/> 
            Este es un <b>e-mail</b> enviando desde <b>Python</b> 
            """

            email = """From: %s 
            To: %s 
            MIME-Version: 1.0 
            Content-type: text/html 
            Subject: %s 

            %s
            """ % (remitente, destinatario, asunto, mensaje) 
            try: 
                smtp = smtplib.SMTP('localhost') 
                smtp.sendmail(remitente, destinatario, email) 
                print("Correo enviado")
            except: 
                print("""Error: el mensaje no pudo enviarse. 
                Compruebe que sendmail se encuentra instalado en su sistema""")

        #buscar correo en BD/smpt nemonico
        #si lo encuentro, 
        #enviar correo con la liga de la forma/heroku/ variable(_correo) tenga el correo/
        #otra forma/permite restablecer contrasena 
        #si no existe

        return render_template("recuperar.html",  msg='Si tu usuario existe, revisa tu correo')  
    else: 
        return render_template("recuperar.html")  


@app.route("/resetpassword",methods=["POST", "GET"])
def resetpassword():
    if request.method == "POST":
        #recuperar contra 1 y 2(forma), argscorreo/url
        #validar que sean iguales
        #si son iguales cambiar password/ DAO actualizar password
        #si no, mostrar error 
        
     return render_template("cambiocontrasena.html")    
    else:
     return render_template("cambiocontrasena.html")    

    

if __name__ == "__main__":
    app.run()