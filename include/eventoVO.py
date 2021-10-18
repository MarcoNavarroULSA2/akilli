class EventoVO:
    def __init__(self, nombreEvento, idUsuario):
       # self.__idEvento = idEvento
        self.__nombreEvento = nombreEvento
        self.__idUsuario = idUsuario
       # self.__tiempo = tiempo

    def setAll(self, idEvento, nombreEvento, idUsuario, tiempo ):        
        self.__idEvento = idEvento
        self.__nombreEvento = nombreEvento
        self.__idUsuario = idUsuario
        self.__tiempo = tiempo

    def getIdEvento(self):
        return self.__idEvento
    def getNombreEvento(self):
        return self.__nombreEvento
    def getIdUsuario(self):
        return self.__idUsuario
    def getTiempo(self):
        return self.__tiempo
    