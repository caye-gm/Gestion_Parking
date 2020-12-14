class factura_repository():
    def __init__(self,lista_factura):
        self.__lista_factura=lista_factura

    @property
    def lista_factura(self):
        return self.__lista_factura

    @lista_factura.setter
    def lista_factura(self, value):
        self.__lista_factura=value


    def add_factura(self,factura):
        self.lista_factura.append(factura)

