from flask import json
import include.conexion as cnx 
from include.MinutaVO import MinutaVO

class MinutaDAO:
    def __init__(self):
        self.__tabla = "Minutas"
    
    def getMinuta(self, id):
        try:
            print('getMinutas')
            conn=cnx.mysql.connect()
            cursor=conn.cursor()
            query_select=('SELECT id, nombreMinuta, texto, nombreCreador, fechaCreacion FROM Minutas WHERE id =%s') 
            values=(id) 
            cursor.execute(query_select, values)
            data=cursor.fetchall()
            listaVO=[]
            for fila in data:
                vo = MinutaVO(fila[0], fila[1], fila[2], fila[3], fila[4])
                listaVO.append(vo)
            return listaVO
        except Exception as e:
            return json.dumps({'error':str(e)})
        finally: 
            cursor.close()
            conn.close()


    def getMinutas(self):
        try:
            print('getMinutas')
            conn=cnx.mysql.connect()
            cursor=conn.cursor()
            query_select=('SELECT id, nombreMinuta, texto, nombreCreador, fechaCreacion FROM Minutas') 
            values=('') #empleado.getCorreo()
            cursor.execute(query_select)
            data=cursor.fetchall()
            listaVO=[]
            for fila in data:
                vo = MinutaVO(fila[0], fila[1], fila[2], fila[3], fila[4])
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
            consulta=("INSERT INTO Minutas (nombreMinuta, texto, nombreCreador, fechaCreacion)" "VALUES(%s,%s,%s,%s)")          
            valores=(
            vo.getNombreMinuta(),
            vo.getTexto(),
            vo.getNombreCreador(),
            vo.getFechaCreacion(),
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

