class factura():
    def __init__(self,abono,total_pago):
        self.__abono=abono
        self.__total_pago=total_pago

    def __str__(self):
        return f"{self.abono} y precio total: {self.total_pago}"

    @property
    def abono(self):
        return self.__abono

    @abono.setter
    def abono(self, value):
        self.__abono=value
    @property
    def total_pago(self):
        return self.__total_pago

    @total_pago.setter
    def total_pago(self, value):
        self.__total_pago=value

