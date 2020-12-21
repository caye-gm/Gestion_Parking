from Models.plaza import *
from Models.vehiculo import *
from Models.ticket import *
from datetime import datetime

import random

class parking_service():
    def __init__(self,parking,cliente_repositorio,vehiculo_repositorio):
        self.__parking=parking
        self.__cliente_repositorio=cliente_repositorio
        self.__vehiculo_repositorio=vehiculo_repositorio
    @property
    def parking(self):
        return self.__parking

    @parking.setter
    def parking(self, value):
        self.__parking=value
    @property
    def cliente_repositorio(self):
        return self.__cliente_repositorio

    @cliente_repositorio.setter
    def cliente_repositorio(self, value):
        self.__cliente_repositorio=value

    @property
    def vehiculo_repositorio(self):
        return self.__vehiculo_repositorio

    @vehiculo_repositorio.setter
    def vehiculo_repositorio(self, value):
        self.__vehiculo_repositorio=value

    def inicilizar_parking(self,tamArray):
        plazaTurismo=round(tamArray*70/100)
        plazaMoto=round(tamArray*15/100)
        plazaMinus=round(tamArray*15/100)
        total=plazaTurismo+plazaMoto+plazaMinus

        while tamArray!=total:
            if total < tamArray:
                calc=tamArray-total
                plazaTurismo+=calc
                total+=1

            if total > tamArray:

                calc=total-tamArray
                plazaTurismo-=calc
                total-=1



        suma1=plazaMoto+plazaTurismo
        suma2=plazaMoto+plazaTurismo+plazaMinus

        for i in range(0,plazaTurismo):
            lista=[]
            plazaT =plaza(i,None,False,False)
            self.parking.lista_turismos.append(plazaT)
        for i in range(plazaTurismo,suma1):
            lista=[]
            plazaMoto =plaza(i,None,False,False)
            self.parking.lista_motocicletas.append(plazaMoto)

        for i in range(suma1, suma2):
            lista=[]
            plazaMinus =plaza(i,None,False,False)
            self.parking.lista_minusvalidos.append(plazaMinus)

    def plaza_vacia(self,plaza):
        plaza.vehiculo=None
        plaza.ocupada=False
        plaza.reservado=False

    def plaza_turismo_disponible(self):
        count=0
        for i in self.parking.lista_turismos:
            if i.ocupada==False and i.reservado==False:
                return count
            count+=1
        return -1

    def depositar_turismo(self,matricula):
        if self.plaza_turismo_disponible!=-1:
            pin=random.randrange(1000,9999)
            valor=self.plaza_turismo_disponible()
            v= vehiculo(matricula,"turismo",self.parking.lista_turismos[valor],pin,datetime.now(),None)
            self.parking.lista_turismos[valor].vehiculo=v
            self.parking.lista_turismos[valor].ocupada=True
            self.vehiculo_repositorio.add_vehiculo(v)

            return True

        return False

    def plaza_motocicleta_disponible(self):
        count=0
        for i in self.parking.lista_motocicletas:
            if i.ocupada==False and i.reservado==False:
                return count
            count+=1
        return -1

    def depositar_motocicleta(self,matricula):
        if self.plaza_motocicleta_disponible()!=-1:
            pin=random.randrange(1000,9999)
            valor=self.plaza_motocicleta_disponible()
            v= vehiculo(matricula,"motocicleta",self.parking.lista_motocicletas[valor],pin,datetime.now(),None)
            self.parking.lista_motocicletas[valor].vehiculo=v
            self.parking.lista_motocicletas[valor].ocupada=True
            self.vehiculo_repositorio.add_vehiculo(v)
            return True

        return False
    def plaza_minusvalido_disponible(self):
        count=0
        for i in self.parking.lista_minusvalidos:
            if i.ocupada==False and i.reservado==False:
                return count
            count+=1
        return -1

    def depositar_minusvalido(self,matricula):
        if self.plaza_minusvalido_disponible()!=-1:
            pin=random.randrange(1000,9999)
            valor=self.plaza_minusvalido_disponible()
            v= vehiculo(matricula,"minusvalido",self.parking.lista_minusvalidos[valor],pin,datetime.now(),None)
            self.parking.lista_minusvalidos[valor].vehiculo=v
            self.parking.lista_minusvalidos[valor].ocupada=True
            self.vehiculo_repositorio.add_vehiculo(v)

            #ticket_vehiculo=ticket(v.fecha_entrada,None,v.matricula,v.plaza.num_plaza,v.pin,None)

            return True

        return False


    def tiempo_minutos(self,fecha1,fecha2):
        tiempo = (fecha1 - fecha2)
        total_seconds = tiempo.total_seconds()
        minutes = total_seconds/60
        return minutes



    def retirar_vehiculo(self,matrícula,numplaza,pin,listaRetirada):
        vehiculo=self.vehiculo_repositorio.find_by_matricula(matrícula)
        if vehiculo !=None and vehiculo.plaza.num_plaza==numplaza and vehiculo.pin==pin:
            if vehiculo.tipo=="turismo":
                precio=0.12
                vehiculo.fecha_salida=datetime.now()
                total=self.tiempo_minutos(vehiculo.fecha_salida,vehiculo.fecha_entrada)*precio
                vehiculo.plaza.ocupada=False
                vehiculo.plaza.vehiculo=None
                vehiculo.plaza=None
                self.vehiculo_repositorio.lista_vehiculos.delete_vehiculo(vehiculo)
                listaRetirada.append(total)
                return round(total,2)
            if vehiculo.tipo=="motocicleta":
                precio=0.08
                vehiculo.fecha_salida=datetime.now()
                total=self.tiempo_minutos(vehiculo.fecha_salida,vehiculo.fecha_entrada)*precio
                vehiculo.plaza.ocupada=False
                vehiculo.plaza.vehiculo=None
                vehiculo.plaza=None
                self.vehiculo_repositorio.delete_vehiculo(vehiculo)
                listaRetirada.append(total)
                return total
            if vehiculo.tipo=="minusvalido":
                precio=0.10
                vehiculo.fecha_salida=datetime.now()
                total=self.tiempo_minutos(vehiculo.fecha_salida,vehiculo.fecha_entrada)*precio
                vehiculo.plaza.ocupada=False
                vehiculo.plaza.vehiculo=None
                vehiculo.plaza=None
                self.vehiculo_repositorio.delete_vehiculo(vehiculo)
                listaRetirada.append(total)
                return total

    def depositar_cliente_abonado(self,matrícula,dni):
        vehiculo=self.vehiculo_repositorio.find_by_matricula(matrícula)
        cliente=self.cliente_repositorio.findByDni(dni)
        if vehiculo != None and cliente != None:
            if cliente.vehiculo == vehiculo and vehiculo.plaza.ocupada==False and vehiculo.plaza.reservado==True:
                vehiculo.plaza.ocupada=True
                return True
        return "Hemos tenido un error , comprueba que tus datos sean correctos"

    def retirar_vehiculo_cliente_abonado(self,matricula,numPlaza,pin):
        vehiculo=self.vehiculo_repositorio.find_by_matricula(matricula)
        if vehiculo!=None:
            if vehiculo.plaza.ocupada==True and vehiculo.plaza.reservado==True and vehiculo.plaza.num_plaza==numPlaza and vehiculo.pin==pin:
                vehiculo.plaza.ocupada=False
                return True
        return False
