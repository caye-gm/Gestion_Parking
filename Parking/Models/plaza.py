class plaza():
    def __init__(self,num_plaza,vehiculo,ocupada,reservado):
        self.__num_plaza=num_plaza
        self.__vehiculo=vehiculo
        self.__ocupada=ocupada
        self.__reservado=reservado
    def __str__(self):
        return f"número de plaza: {self.num_plaza}, vehiculo :  {self.vehiculo} , ocupada: {self.ocupada}, reservada:{self.reservado}"
    @property
    def num_plaza(self):
        return self.__num_plaza

    @num_plaza.setter
    def num_plaza(self, value):
        self.__num_plaza=value

    @property
    def vehiculo(self):
        return self.__vehiculo

    @vehiculo.setter
    def vehiculo(self, value):
        self.__vehiculo=value
    @property
    def ocupada(self):
        return self.__ocupada

    @ocupada.setter
    def ocupada(self, value):
        self.__ocupada=value

    @property
    def reservado(self):
        return self.__reservado

    @reservado.setter
    def reservado(self, value):
        self.__reservado=value
