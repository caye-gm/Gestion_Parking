from Models.plaza import *
class parking_service():
    def __init__(self,parking):
        self.__parking=parking

    @property
    def parking(self):
        return self.__parking

    @parking.setter
    def parking(self, value):
        self.__parking=value

    def inicilizar_array(self,tamArray):
        plazaTurismo=round(tamArray*70/100)
        plazaMoto=round(tamArray*15/100)
        plazaMinus=round(tamArray*15/100)
        total=plazaTurismo+plazaMoto+plazaMinus

        if total < tamArray:
            plazaTurismo+=tamArray-total
        if total > tamArray:
            plazaTurismo-=total-tamArray

        print(plazaTurismo)
        print(plazaMoto)
        print(plazaMinus)

        for i in range(0,plazaTurismo):
            lista=[]
            plazaT =plaza(i,None,False,False)
            self.parking.lista_turismos.append(plazaT)
        for i in range(0,plazaMoto):
            lista=[]
            plazaMoto =plaza(i,None,False,False)
            self.parking.lista_motocicletas.append(plazaMoto)
        for i in range(0, plazaMinus):
            lista=[]
            plazaMinus =plaza(i,None,False,False)
            self.parking.lista_minusvalidos.append(plazaMinus)
