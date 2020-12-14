class cliente():
    def __init__(self,vehiculo,dni,nombre,abono):
        self.__dni=dni
        self.__vehiculo=vehiculo
        self.__nombre=nombre
        self.__abono=abono
    def __str__(self):
        return f"El cliente tiene: nombre: {self.nombre}  dni: {self.dni}"
    @property
    def vehiculo(self):
        return self.__vehiculo

    @vehiculo.setter
    def vehiculo(self, value):
        self.__vehiculo=value
    @property
    def dni(self):
        return  self.__dni

    @dni.setter
    def dni(self, value):
         self.__dni=value
    @property
    def abono(self):
        return self.__abono

    @abono.setter
    def abono(self, value):
        self.__abono=value

    @property
    def nombre(self):
        return  self.__nombre

    @nombre.setter
    def nombre(self, value):
         self.__nombre=value

