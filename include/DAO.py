from flask import json
import include.conexion as cnx 
from include.VO import EmpleadoVO

class EmpleadoDAO:
    def __init__(self):
        self.__tabla = "Empleado"

    def selectALL(self):
        try:
            conn=cnx.mysql.connect()
            cursor=conn.cursor()
            cursor.execute('SELECT * FROM '+ self.__tabla +' ORDER BY IdUsuario DESC')
            data=cursor.fetchall()
            listaVO=[]
            for fila in data:
                vo = EmpleadoVO(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5] )
                listaVO.append(vo)
            return listaVO
        except Exception as e:
            return json.dumps({'error':str(e)})
        finally: 
            cursor.close()
            conn.close()

            
    def insertALL(self):
        try:
            conn=cnx.mysql.connect()
            cursor=conn.cursor()
            vo = EmpleadoVO()
            query_empleado=("INSERT INTO Empleado" "(NombreCompleto,Telefono, Empresa)" "VALUES(%(NombreCompleto)s,%(Telefono)s,%(Empresa)s)")  
            query_empleadologin=("INSERT INTO Login_Empleado" "(Correo,Password)" "VALUES(%(Correo)s,%(Password)s)")          
            values={
            "NombreCompleto": str(vo.getNombre),
            "Telefono": str(vo.getTelefono),
            "Empresa": str(vo.getEmpresa)}
            valuesLogin={
            "Correo": str(vo.getCorreo),           
            "Password": str(vo.getPassword)}
            cursor.execute(query_empleado,values)
            cursor.execute(query_empleadologin,valuesLogin)
            conn.commit()
            return{
                'message': "succesfull"
            }
        except Exception as e:
            return json.dumps({'error':str(e)})  
        finally: 
            
            cursor.close()
            conn.close()    

