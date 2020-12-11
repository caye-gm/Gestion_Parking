class parking():
    def __init__(self, lista_turismos,lista_motocicletas,  lista_minusvalidos):
        self.__listaMotocicletas=lista_motocicletas
        self.__listaTurismos=lista_turismos
        self.__lista_minusvalidos=lista_minusvalidos


    @property
    def lista_turismos(self):
        return self.__listaTurismos

    @lista_turismos.setter
    def lista_turismos(self, value):
        self.__lista_turismos=value
    @property
    def lista_motocicletas(self):
        return self.__listaMotocicletas

    @lista_motocicletas.setter
    def lista_motocicletas(self, value):
        self.__lista_motocicletas= value
    @property
    def lista_minusvalidos(self):
        return self.__lista_minusvalidos

    @lista_minusvalidos.setter
    def lista_minusvalidos(self, value):
        self.__lista_minusvalidos=value
