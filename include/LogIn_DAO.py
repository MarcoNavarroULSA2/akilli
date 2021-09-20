from flask import json
import include.conexion as cnx 
from include.LogIn_VO import LogInVO

class LogInDAO:
    def __init__(self):
        self.__tabla = "Login_Empleado"

    def selectALL(self, empleado):
        try:
            conn=cnx.mysql.connect()
            cursor=conn.cursor()
            query_select=('SELECT Correo, Password FROM Login_Empleado WHERE Correo = %s AND Password = %s') 
            values=(empleado.getCorreo(), empleado.getPassword()) 
            cursor.execute(query_select, values)
            data=cursor.fetchall()
            listaVO=[]
            for fila in data:
                vo = LogInVO(fila[0], fila[1])
                listaVO.append(vo)
            return listaVO
        except Exception as e:
            return json.dumps({'error':str(e)})
        finally: 
            cursor.close()
            conn.close()