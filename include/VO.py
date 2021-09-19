class EmpleadoVO:
    def __init__(self, nombre, correo, password, telefono, empresa ):
        self.__nombre = nombre
        self.__correo = correo
        self.__password = password
        self.__telefono = telefono
        self.__empresa = empresa


    def setEmpleado(self, nombre, correo, password, telefono,empresa ):        
        self.__nombre = nombre
        self.__correo = correo
        self.__password = password
        self.__telefono = telefono
        self.__empresa = empresa

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
    def getEmpresa(self):
        return self.__empresa  