class EmpleadoVO:
    def __init__(self, id, nombre, correo, password, telefono, puesto ):
        self.__id = id
        self.__nombre = nombre
        self.__correo = correo
        self.__password = password
        self.__telefono = telefono
        self.__puesto = puesto


    def setEmpleado(self, id, nombre, correo, password, telefono, puesto ):
        self.__id = id
        self.__nombre = nombre
        self.__correo = correo
        self.__password = password
        self.__telefono = telefono
        self.__puesto = puesto

    def getId(self):
        return self.__id
    def getNombre(self):
        return self.__nombre
    def getCorreo(self):
        return self.__correo
    def getPassword(self):
        return self.__password
    def getTelefono(self):
        return self.__telefono
    def getPuesto(self):
        return self.__puesto   