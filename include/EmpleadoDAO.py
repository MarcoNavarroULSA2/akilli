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

            
    def insertALL(self, empleado):
        try:
            conn=cnx.mysql.connect()
            cursor=conn.cursor()
            query_empleado=("INSERT INTO Empleado (Nombre, Telefono, Empresa)" "VALUES(%s,%s,%s)")  
            query_empleadologin=("INSERT INTO Login_Empleado (Correo,Password)" "VALUES(%s,%s)")          
            #values query_empleado
            values=(
            empleado.getNombre(),
            empleado.getTelefono(),
            empleado.getEmpresa())
            #values query_empleadologin            
            valuesLogin=(
            empleado.getCorreo(),           
            empleado.getPassword())
            cursor.execute(query_empleado, values)
            cursor.execute(query_empleadologin, valuesLogin)
            conn.commit()
            return{
                'message': "insertALL succesful"
            }
        except Exception as e:
            return json.dumps({'error':str(e)})  
        finally: 
            cursor.close()
            conn.close()    

