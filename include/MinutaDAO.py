from flask import json
import include.conexion as cnx 
from include.MinutaVO import MinutaVO

class MinutaDAO:
    def __init__(self):
        self.__tabla = "Minutas"

    def updateMinuta(self, nombreMinuta, texto, id):
        try:
            conn=cnx.mysql.connect()
            cursor=conn.cursor()
            query_select=('Update Minutas SET nombreMinuta = %s, texto = %s  WHERE id = %s') 
            values=(nombreMinuta, texto, id) 
            cursor.execute(query_select, values)
            conn.commit()
            print(cursor.rowcount, "record(s) affected")
        except Exception as e:
            return json.dumps({'error':str(e)})
        finally: 
            cursor.close()
            conn.close()
    
    def getMinuta(self, id):
        try:
            print('getMinutas')
            conn=cnx.mysql.connect()
            cursor=conn.cursor()
            query_select=('SELECT id, nombreMinuta, texto, nombreCreador, fechaCreacion, frases, departamento FROM Minutas WHERE id =%s') 
            values=(id) 
            cursor.execute(query_select, values)
            data=cursor.fetchall()
            listaVO=[]
            for fila in data:
                vo = MinutaVO(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6])
                listaVO.append(vo)
            return listaVO
        except Exception as e:
            return json.dumps({'error':str(e)})
        finally: 
            cursor.close()
            conn.close()


    def getMinutas(self, departamento):
        try:
            print('getMinutas')
            conn=cnx.mysql.connect()
            cursor=conn.cursor()
            query_select=('SELECT id, nombreMinuta, texto, nombreCreador, fechaCreacion, frases, departamento FROM Minutas WHERE departamento =%s') 
            values=(departamento) 
            cursor.execute(query_select, values)
            data=cursor.fetchall()
            listaVO=[]
            for fila in data:
                vo = MinutaVO(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6])
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
            consulta=("INSERT INTO Minutas (nombreMinuta, texto, nombreCreador, fechaCreacion, frases, departamento)" "VALUES(%s,%s,%s,%s,%s, %s)")          
            valores=(
            vo.getNombreMinuta(),
            vo.getTexto(),
            vo.getNombreCreador(),
            vo.getFechaCreacion(),
            vo.getFrases(),
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


    def selectALL(self):
        try:
            print('selectALL')
            conn=cnx.mysql.connect()
            cursor=conn.cursor()
            query_select=('SELECT id, nombreMinuta, texto, nombreCreador, fechaCreacion, frases, departamento FROM Minutas') 
            cursor.execute(query_select)
            data=cursor.fetchall()
            listaVO=[]
            for fila in data:
                vo = MinutaVO(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6])
                listaVO.append(vo)
            return listaVO
        except Exception as e:
            return json.dumps({'error':str(e)})
        finally: 
            cursor.close()
            conn.close()


