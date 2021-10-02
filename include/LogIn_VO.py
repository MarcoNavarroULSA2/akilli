class LogInVO:
    def __init__(self, id, correo, password, sal):
        self.__id = id
        self.__correo = correo
        self.__password = password
        self.__sal = sal

    def getId(self):
        return self.__id
    def getCorreo(self):
        return self.__correo
    def getPassword(self):
        return self.__password
    def getSal(self):
        return self.__sal

    def setId(self, valor):
        self.__id = valor
    def setCorreo(self, valor):
        self.__correo = valor
    def setPassword(self, valor):
        self.__password = valor
    def setSal(self, valor):
        self.__sal = valor