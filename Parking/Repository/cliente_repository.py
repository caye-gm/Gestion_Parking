import pickle
class cliente_repository():
    def __init__(self,lista_clientes=[]):
        self.__lista_clientes=lista_clientes

    @property
    def lista_clientes(self):
        return self.__lista_clientes

    @lista_clientes.setter
    def lista_clientes(self, value):
        self.__lista_clientes=value



    def add_cliente(self,cliente):
        self.lista_clientes.append(cliente)
        pickle_url=open("./db/clientes","wb")
        pickle.dump(self.lista_clientes,pickle_url)
        pickle_url.close()

    def findAll(self):
        for i in self.lista_clientes:
            print(f"El cliente tiene dni: {i.dni}")

    def findByDni(self,dni):
        for cliente in self.lista_clientes:
            if cliente.dni==dni:
                return cliente
        return False

    def removeByDni(self,dni):
        cliente=self.findByDni(dni)
        if cliente != None:
            pickle_url=open("./db/clientes","wb")
            pickle.dump(self.lista_clientes,pickle_url)
            pickle_url.close()
