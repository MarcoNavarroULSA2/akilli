from flask import json
import include.conexion as cnx 
from include.EmpleadoVO import EmpleadoVO
from include.LogIn_VO import LogInVO

class EmpleadoDAO:
    def __init__(self):
        self.__tabla = "Empleado"

    def updateUser(self, nombre, telefono, id):
        try:
            conn=cnx.mysql.connect()
            cursor=conn.cursor()
            query_select=('Update Empleado SET Nombre = %s, Telefono = %s  WHERE ID_LoginEmpleado = %s') 
            values=(nombre, telefono, id) 
            cursor.execute(query_select, values)
            conn.commit()
            print(cursor.rowcount, "record(s) affected")
        except Exception as e:
            return json.dumps({'error':str(e)})
        finally: 
            cursor.close()
            conn.close()

    def finUser(self, idEmpleado):
        try:
            conn=cnx.mysql.connect()
            cursor=conn.cursor()
            query_select=('SELECT Nombre, Telefono, Empresa, ID_LoginEmpleado, departamento FROM Empleado WHERE ID_LoginEmpleado = %s') 
            values=(idEmpleado) 
            cursor.execute(query_select, values)
            data=cursor.fetchall()
            listaVO=[]
            for fila in data:
                vo = EmpleadoVO(1, fila[0], '', fila[1], fila[2], fila[3], fila[4])
                listaVO.append(vo)
            return listaVO
        except Exception as e:
            return json.dumps({'error':str(e)})
        finally: 
            cursor.close()
            conn.close()



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
            consulta=("INSERT INTO Empleado (Nombre, Telefono, Empresa, ID_LoginEmpleado, departamento)" "VALUES(%s,%s,%s,%s,%s)")          
            valores=(
            vo.getNombre(),
            vo.getTelefono(),
            vo.getEmpresa(),
            vo.getIdLogin(),
            vo.getDepartamento()
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

