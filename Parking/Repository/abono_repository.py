import pickle
class abono_repository():
    def __init__(self,lista_abonos=[]):
        self.__lista_abonos=lista_abonos

    @property
    def lista_abonos(self):
        return self.__lista_abonos

    @lista_abonos.setter
    def lista_abonos(self, value):
        self.__lista_abonos=value

    def add_abono(self,abono):
        self.lista_abonos.append=abono

    def find_all(self):
        for i in self.lista_abonos:
            print(i)

    def add_abono(self,abono):
        self.lista_abonos.append(abono)
        pickle_url=open("./db/abonos","wb")
        pickle.dump(self.lista_abonos,pickle_url)
        pickle_url.close()

    def delete_abono(self,abono):
        self.lista_abonos.remove(abono)
        pickle_url=open("./db/abonos","wb")
        pickle.dump(self.lista_abonos,pickle_url)
        pickle_url.close()
