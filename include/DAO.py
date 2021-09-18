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
            cursor.execute('INSERT INTO Empleado (ID_Empleado, NombreCompleto, Correo,Password, Telefono, Puesto) VALUES(' + vo.getNombre + vo.getCorreo + vo.getPassword + vo.getTelefono + vo.getPuesto+')')
            return{
                'message': "succesfull"
            }
        except Exception as e:
            return json.dumps({'error':str(e)})  
        finally: 
            cursor.close()
            conn.close()        
