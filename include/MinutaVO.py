class MinutaVO:
    def __init__(self, id, nombreMinuta, texto, nombreCreador, fechaCreacion, frases, departamento ):
        self.__id = id
        self.__nombreMinuta = nombreMinuta
        self.__texto = texto
        self.__nombreCreador = nombreCreador
        self.__fechaCreacion = fechaCreacion
        self.__frases = frases
        self.__departamento = departamento
        
    def setAll(self, id, nombreMinuta, texto, nombreCreador, fechaCreacion, frases, departamento ):        
        self.__id = id
        self.__nombreMinuta = nombreMinuta
        self.__texto = texto
        self.__nombreCreador = nombreCreador
        self.__fechaCreacion = fechaCreacion
        self.__frases = frases
        self.__departamento = departamento


    def getId(self):
        return self.__id
    def getNombreMinuta(self):
        return self.__nombreMinuta
    def getTexto(self):
        return self.__texto
    def getNombreCreador(self):
        return self.__nombreCreador
    def getFechaCreacion(self):
        return self.__fechaCreacion  
    def getFrases(self):
        return self.__frases.replace('[', '').replace(']', '').replace('\\u00c1', 'Á').replace("\\u00e1", 'á').replace('\\u00c9', 'É').replace('\\u00e9', 'é').replace('\\u00cd', 'Í').replace('\\u00ed', 'í').replace('\\u00d3', 'Ó').replace('\\u00f3', 'ó').replace('\\u00da', 'Ú').replace('\\u00fa', 'ú').replace('\\u00dc', 'Ü').replace('\\u00fc', 'ü').replace('\\u00d1', 'Ṅ').replace('\\u00f1', 'ñ')
    def getDepartamento(self):
        return self.__departamento  