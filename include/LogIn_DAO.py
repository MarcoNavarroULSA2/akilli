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
            query_select=('SELECT Correo, Password FROM Login_Empleado WHERE Correo = %s') 
            values=(empleado.getCorreo()) 
            cursor.execute(query_select, values)
            data=cursor.fetchall()
            listaVO=[]
            for fila in data:
                #vo = LogInVO("", fila[0], fila[1], "")
                listaVO.append(fila[0])
                listaVO.append(fila[1])
            return listaVO
        except Exception as e:
            return json.dumps({'error':str(e)})
        finally: 
            cursor.close()
            conn.close()

    def insert(self, vo):
        try:
            conn=cnx.mysql.connect()
            cursor=conn.cursor()
            consulta=("INSERT INTO Login_Empleado (Correo,Password, sal)" "VALUES(%s,%s,%s)")          
            valores=(
            vo.getCorreo(),           
            vo.getPassword(),
            vo.getSal()
            )
            cursor.execute(consulta, valores)
            conn.commit()
            print(cursor.lastrowid)
            return {'message': "insert succesful", "id":cursor.lastrowid}
        except Exception as e:
            return json.dumps({'error':str(e)})  
        finally: 
            cursor.close()
            conn.close()  

    def existecorreo(self, vo):
        try:
            conn=cnx.mysql.connect()
            cursor=conn.cursor()
            query_select=('SELECT Correo FROM Login_Empleado WHERE Correo = %s LIMIT 1') 
            values=(vo.getCorreo()) 
            cursor.execute(query_select, values)
            data=cursor.fetchall()
            bandera= False 
            if len(data)> 0:
                bandera= True 
            return bandera              
        except Exception as e:
            return json.dumps({'error':str(e)})
        finally: 
            cursor.close()
            conn.close()          