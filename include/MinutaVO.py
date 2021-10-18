class MinutaVO:
    def __init__(self, id, nombreMinuta, texto, nombreCreador, fechaCreacion, frases ):
        self.__id = id
        self.__nombreMinuta = nombreMinuta
        self.__texto = texto
        self.__nombreCreador = nombreCreador
        self.__fechaCreacion = fechaCreacion
        self.__frases = frases
        
    def setAll(self, id, nombreMinuta, texto, nombreCreador, fechaCreacion, frases ):        
        self.__id = id
        self.__nombreMinuta = nombreMinuta
        self.__texto = texto
        self.__nombreCreador = nombreCreador
        self.__fechaCreacion = fechaCreacion
        self.__frases = frases


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
        return self.__frases   