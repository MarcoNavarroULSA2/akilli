from flask import Flask, app, render_template, json, request, redirect, url_for, session

from include.MinutaVO import MinutaVO
from include.MinutaDAO import MinutaDAO
from include.EmpleadoVO import EmpleadoVO
from include.EmpleadoDAO import EmpleadoDAO
from include.LogIn_VO import LogInVO
from include.LogIn_DAO import LogInDAO
import datetime
import uuid, hashlib
import smtplib 
import json
from werkzeug.security import generate_password_hash, check_password_hash
from key import key_phrase_extraction_example, authenticate_client
from include.eventoDAO import EventoDAO
from include.eventoVO import EventoVO

app = Flask(__name__, static_url_path='')
app.secret_key = "1234"
app.static_folder = 'static'

def esAdministrador():
    departamento = getEmpleadoInfo()["_EmpleadoVO__departamento"]
    return departamento == "Admin" 


def getEmpleadoInfo():
    empleadoJson = session["user_info"]
    empleado_object = json.loads(empleadoJson)
    return empleado_object

def checarusuario():
 try:
    user = session["user"]
    auth = session["auth"] 
    return auth, user
 except:
    user = "unknown"
    auth = 0
    return auth, user
    

@app.before_request
def session_management():
  session.permanent = True

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
    
    usuario = listaVO[0]
    
    checarContra = check_password_hash (usuario.getPassword(), data['password'] )
    #print(listaVO.__len__())
    if listaVO.__len__() == 0 or checarContra == False:
        return render_template('login.html', msg='Wrong user or password')
    
    #Traer info usuario
    empleadoDAO = EmpleadoDAO() 
    empleadosLista = empleadoDAO.finUser(usuario.getId())
    empleado = empleadosLista[0]
    empleadoJson = json.dumps(empleado.__dict__)
    
    session.clear()
    session["user"] = usuario.getCorreo()
    session["user_info"] = empleadoJson
    session["auth"] = 1
    eventoDAO = EventoDAO()
    evento = "Iniciar Sesion"
    eventoVO = EventoVO(evento, usuario.getId())
    eventoDAO.insertEvento(eventoVO)
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
        contrasena=data ['password']
        sal = uuid.uuid4().hex
        pimienta = "SEGURIDAD1235"        
        contraHash = generate_password_hash(contrasena, method= "sha256")
        print(contraHash)
        VO2 = LogInVO(99, data['email'], contraHash, sal)        
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
    auth, user = checarusuario()
    print (auth)
    if auth == 0:
        return redirect(url_for('login'))    
    return render_template("dashboard/menu.html",  nombreUsuario=getEmpleadoInfo()["_EmpleadoVO__nombre"], admin = esAdministrador())  

@app.route("/settings")
def settings():
    auth = checarusuario() 
    if auth == 0:
        return redirect(url_for('login'))
    return render_template("settings.html", nombreUsuario=getEmpleadoInfo()["_EmpleadoVO__nombre"], empleado=getEmpleadoInfo(), admin = esAdministrador())

@app.route("/settings",methods=["POST"])
def settings_2():
    try:
        empleadoDAO = EmpleadoDAO()       
        data=request.form        
        #Actualizar usuario
        empleadoDAO.updateUser(data['nombre'], data['telefono'], getEmpleadoInfo()["_EmpleadoVO__idlogin"])

        #Actualizar session
        empleadoDAO = EmpleadoDAO() 
        empleadosLista = empleadoDAO.finUser(getEmpleadoInfo()["_EmpleadoVO__idlogin"])
        empleado = empleadosLista[0]
        empleadoJson = json.dumps(empleado.__dict__)
        session["user_info"] = empleadoJson

        return redirect(url_for('settings'))
    except Exception as e:
     return json.dumps({'error':str(e)})      

@app.route("/minutas")
def minutas():
    auth = checarusuario() 
    if auth == 0:
        return redirect(url_for('login'))
    try:
        minutaDAO = MinutaDAO()       
        listado=minutaDAO.getMinutas(getEmpleadoInfo()["_EmpleadoVO__departamento"])      
        print('Len')
        print(listado.__len__())
        #print(listado[0]) 
        return render_template("minutas.html", minutas=listado, nombreUsuario=getEmpleadoInfo()["_EmpleadoVO__nombre"], admin = esAdministrador())
    except Exception as e:
     return json.dumps({'error':str(e)}) 
    
@app.route("/minuta")
def minuta():
    auth = checarusuario() 
    if auth == 0:
        return redirect(url_for('login'))
    id = request.args.get('id', '')    
    minutaDAO = MinutaDAO()       
    listado=minutaDAO.getMinuta(id)      
    minuta=listado[0]
    return render_template("minuta.html",minuta=minuta, nombreUsuario=getEmpleadoInfo()["_EmpleadoVO__nombre"], admin = esAdministrador()) 

@app.route("/CrearMinuta")
def Minuta():
    auth = checarusuario() 
    if auth == 0:
        return redirect(url_for('login'))
    return render_template("CrearMinuta.html", nombreUsuario=getEmpleadoInfo()["_EmpleadoVO__nombre"], admin = esAdministrador())

@app.route("/CrearMinuta",methods=["POST"])
def crearMinuta_2():
    try:
        minutaDAO = MinutaDAO()       
        data=request.form        
        empleadoJson = session["user_info"]
        empleado_object = json.loads(empleadoJson)
        texto = data["texto"]
        cliente = authenticate_client()
        frases = key_phrase_extraction_example(cliente, texto)
        
        VO = MinutaVO(1, data['nombreMinuta'], data['texto'], empleado_object['_EmpleadoVO__nombre'], datetime.datetime.now(), frases,  empleado_object['_EmpleadoVO__departamento']) 
        #print("Va el Empleado con id "+ str(VO.getIdLogin()))
        minutaDAO.insert(VO)
        eventoDAO = EventoDAO()
        evento = "Crear Minuta"
        eventoVO = EventoVO(evento, empleado_object['_EmpleadoVO__idlogin'])
        eventoDAO.insertEvento(eventoVO)
        return redirect(url_for('menu'))
    except Exception as e:
     return json.dumps({'error':str(e)})  

@app.route("/administracionDepartamento")
def administracionDepartamento():
    auth = checarusuario() 
    if auth == 0:
        return redirect(url_for('login'))
    try:
        departamento = getEmpleadoInfo()["_EmpleadoVO__departamento"]
        usuario = getEmpleadoInfo()
        print (usuario)
        print (departamento)
        minutaDAO = MinutaDAO()         
        listado=minutaDAO.selectALL()  
        print('Len')
        print(listado.__len__())
        #print(listado[0]) 
        return render_template("administracionDepartamento.html", minutas=listado, nombreUsuario=getEmpleadoInfo()["_EmpleadoVO__nombre"], admin = departamento == "Admin")
    except Exception as e:
     return json.dumps({'error':str(e)}) 

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

    
@app.route("/logout")
def logout():
    empleadoJson = session["user_info"]
    empleado_object = json.loads(empleadoJson)
    eventoDAO = EventoDAO()
    evento = "Cerrar Sesion"
    eventoVO = EventoVO(evento, empleado_object['_EmpleadoVO__idlogin'])
    eventoDAO.insertEvento(eventoVO)
    session.clear()
    session["user"] = "unknown"
    session["auth"] = 0
  
    return redirect(url_for('index'))




if __name__ == "__main__":
    app.run()