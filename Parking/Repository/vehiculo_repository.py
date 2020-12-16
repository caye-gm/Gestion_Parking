from Models.vehiculo import *
class vehiculo_repository():
    def __init__(self,lista_vehiculos):
        self.__lista_vehiculos=lista_vehiculos

    @property
    def lista_vehiculos(self):
        return self.__lista_vehiculos

    @lista_vehiculos.setter
    def lista_vehiculos(self, value):
        self.__lista_vehiculos=value


    def add_vehiculo(self,vehiculo):
        self.lista_vehiculos.append(vehiculo)

    def findAll(self):
        for i in self.lista_vehiculos:
            print(i)

    def find_by_matricula(self,matricula):
        for i in self.lista_vehiculos:
            if i.matricula==matricula:
                return i
        return False
    def delete_vehiculo(self,vehiculo):
        self.lista_vehiculos.remove(vehiculo)
