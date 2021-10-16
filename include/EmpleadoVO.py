class EmpleadoVO:
    def __init__(self, id, nombre, correo, telefono, empresa, idlogin, departamento ):
        self.__id = id
        self.__nombre = nombre
        self.__correo = correo
        self.__telefono = telefono
        self.__empresa = empresa
        self.__idlogin = idlogin
        self.__departamento = departamento


    def setAll(self, id, nombre, correo, telefono,empresa, idlogin, departamento ):        
        self.__id = id
        self.__nombre = nombre
        self.__correo = correo
        self.__telefono = telefono
        self.__empresa = empresa
        self.__idlogin = idlogin
        self.__departamento = departamento


    def getId(self):
        return self.__id
    def getNombre(self):
        return self.__nombre
    def getCorreo(self):
        return self.__correo
    def getTelefono(self):
        return self.__telefono
    def getEmpresa(self):
        return self.__empresa  
    def getIdLogin(self):
        return self.__idlogin
    def getDepartamento(self):
        return self.__departamento