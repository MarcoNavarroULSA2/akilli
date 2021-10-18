from flask import json
import include.conexion as cnx 
class EventoDAO:


 def __init__(self):
        self.__tabla = "Eventos"

 def insertEvento(self, vo):
        try:
            conn=cnx.mysql.connect()
            cursor=conn.cursor()
            consulta=("INSERT INTO Eventos (nombreEvento, idUsuario)" "VALUES(%s,%s)")          
            valores=(
            vo.getNombreEvento(),
            vo.getIdUsuario(),          
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

