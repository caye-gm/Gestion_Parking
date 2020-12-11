
class cliente_repository():
    def __init__(self,lista_clientes):
        self.__lista_clientes=lista_clientes

    @property
    def lista_clientes(self):
        return self.__lista_clientes

    @lista_clientes.setter
    def lista_clientes(self, value):
        self.__lista_clientes=value

    def findAll(self):
        for i in self.lista_clientes:
            print(f"El cliente tiene dni: {i.dni}")

    def findByDni(self,dni):
        for i in self.lista_clientes:
            if i.dni==dni:
                return i
        return False

    def removeByDni(self,dni):
        for i in self.lista_clientes:
            if i.dni==dni:
                return self.lista_clientes.remove(i)
        return False
