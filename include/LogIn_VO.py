class LogInVO:
    def __init__(self, correo, password):
        self.__correo = correo
        self.__password = password

    def getCorreo(self):
        return self.__correo
    def getPassword(self):
        return self.__password