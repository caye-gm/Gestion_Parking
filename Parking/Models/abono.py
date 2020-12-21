class abono():
    def __init__(self,cliente,num_tarjeta,tipo,fecha_activacion,fecha_cancelacion):
        self.__cliente=cliente
        self.__num_tarjeta=num_tarjeta
        self.__tipo=tipo
        self.__fecha_activacion=fecha_activacion
        self.__fecha_cancelacion=fecha_cancelacion

    def __str__(self):
        return f"{self.cliente} tipo de abono: {self.tipo} fecha inicio: {self.fecha_activacion} fecha fin: {self.fecha_cancelacion}"
    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, value):
        self.__cliente=value

    @property
    def num_tarjeta(self):
        return self.__num_tarjeta

    @num_tarjeta.setter
    def num_tarjeta(self, value):
        self.__num_tarjeta=value

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, value):
        self.__tipo =value
    @property
    def fecha_activacion(self):
        return self.__fecha_activacion

    @fecha_activacion.setter
    def fecha_activacion(self, value):
        self.__fecha_activacion=value
    @property
    def fecha_cancelacion(self):
        return self.__fecha_cancelacion

    @fecha_cancelacion.setter
    def fecha_cancelacion(self, value):
        self.__fecha_cancelacion=value


