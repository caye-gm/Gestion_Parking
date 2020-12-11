class Admin():
    def __init__(self,usuario,contrasenya):
        self.__usuario=usuario
        self.__contrasenya=contrasenya

    @property
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self, value):
        self.__usuario=value
    @property
    def contrasenya(self):
        return self.__contrasenya

    @contrasenya.setter
    def contrasenya(self, value):
        self.__contrasenya=value
