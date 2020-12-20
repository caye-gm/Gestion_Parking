import pickle
class factura_repository():
    def __init__(self,lista_factura=[]):
        self.__lista_factura=lista_factura

    @property
    def lista_factura(self):
        return self.__lista_factura

    @lista_factura.setter
    def lista_factura(self, value):
        self.__lista_factura=value


    def add_factura(self,factura):
        self.lista_factura.append(factura)
        pickle_url=open("./db/facturas","wb")
        pickle.dump(self.lista_factura,pickle_url)
        pickle_url.close()

    def factura_findAll(self):
        for i in self.lista_factura:
            print(i)
