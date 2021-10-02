from flask import json
import include.conexion as cnx 
from include.EmpleadoVO import EmpleadoVO

class EmpleadoDAO:
    def __init__(self):
        self.__tabla = "Empleado"

    def findEmail(self, email):
        try:
            print(email)
            conn=cnx.mysql.connect()
            cursor=conn.cursor()
            query_select=('SELECT Correo FROM Login_Empleado WHERE Correo = %s') 
            values=(email) 
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

            
    def insert(self, vo):
        try:
            conn=cnx.mysql.connect()
            cursor=conn.cursor()
            consulta=("INSERT INTO Empleado (Nombre, Telefono, Empresa, ID_LoginEmpleado)" "VALUES(%s,%s,%s,%s)")          
            valores=(
            vo.getNombre(),
            vo.getTelefono(),
            vo.getEmpresa(),
            vo.getIdLogin()
            )
            cursor.execute(consulta, valores)
            conn.commit()
            return{
                'message': "insert succesful"
            }
        except Exception as e:
            return json.dumps({'error':str(e)})  
        finally: 
            cursor.close()
            conn.close()    

