class Ticket():
    def __init__(self,fecha_entrada,fecha_salida,matricula,plaza,coste):
        self.__fecha_entrada=fecha_entrada
        self.__fecha_salida=fecha_salida
        self.__matricula=matricula
        self.__plaza=plaza
        self.__coste=coste

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
    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, value):
        self.__matricula=value
    @property
    def plaza(self):
        return self.__plaza

    @plaza.setter
    def plaza(self, value):
        self.__plaza =value
    @property
    def coste(self):
        return self.__coste

    @coste.setter
    def coste(self, value):
        self.__coste=value
