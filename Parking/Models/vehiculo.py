class vehiculo():
    def __init__(self,matricula,tipo,plaza,pin,fecha_entrada,fecha_salida):
        self.__matricula=matricula
        self.__tipo=tipo
        self.__plaza=plaza
        self.__pin=pin
        self.__fecha_entrada=fecha_entrada
        self.__fecha_salida=fecha_salida

    def __str__(self):
        return f"Matricula: {self.__matricula},tipo : {self.__tipo} ,pin:{self.__pin}, " \
               f"fecha entrada:{self.__fecha_entrada}"
    @property
    def matricula(self):
        return self.__matricula
    @matricula.setter
    def matricula(self, value):
        self.__matricula=value

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, value):
        self.__tipo=value
    @property
    def plaza(self):
        return self.__plaza

    @plaza.setter
    def plaza(self, value):
        self.__plaza=value
    @property
    def pin(self):
        return self.__pin

    @pin.setter
    def pin(self, value):
        self.__pin=value
    @property
    def fecha_entrada(self):
        return self.__fecha_entrada

    @fecha_entrada.setter
    def fecha_entrada(self, value):
        self.__fecha_entrada=value
    @property
    def fecha_salida(self):
        return self.__fecha_salida

    @fecha_salida.setter
    def fecha_salida(self, value):
        self.__fecha_salida=value
