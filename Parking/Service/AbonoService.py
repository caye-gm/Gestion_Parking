from Models.factura import *
from  Models.abono import *
from Models.cliente import *
from datetime import datetime
import random
class abono_service():
    def __init__(self,cliente_repositorio,vehiculo_repositorio,factura_repository,parking_service):
        self.__cliente_repositorio=cliente_repositorio
        self.__vehiculo_repositorio=vehiculo_repositorio
        self.__factura_repository=factura_repository
        self.__parking_service=parking_service

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
    @property
    def factura_repository(self):
        return self.__factura_repository

    @factura_repository.setter
    def factura_repository(self, value):
        self.__factura_repository=value
    @property
    def parking_service(self):
        return self.__parking_service

    @parking_service.setter
    def parking_service(self, value):
        self.__parking_service=value


    def sumar_fechas_meses(self,tipo):
        fecha=datetime.now()

        if tipo == "mensual":
            if fecha.month==12:
                fecha=fecha.replace(year=(fecha.year+1))
                fecha=fecha.replace(month=1)
            else:
                fecha = fecha.replace(month=(fecha.month+1))

        if "trimestral" == tipo:

            if fecha.month==12:
                fecha=fecha.replace(year=(fecha.year+1))
                fecha=fecha.replace(month=3)
            if fecha.month==11:
                fecha=fecha.replace(year=(fecha.year+1))
                fecha=fecha.replace(month=2)
            if fecha.month==10:
                fecha=fecha.replace(year=(fecha.year+1))
                fecha=fecha.replace(month=1)
            else:
                fecha = fecha.replace(month=(fecha.month+1))

        if "semestral" == tipo:
            if(fecha.month >= 7):
                fecha = fecha.replace(month=(fecha.month-6))
                fecha = fecha.replace(year=(fecha.year+1))
            else:
                fecha = fecha.replace(month=(fecha.month+6))

        if "anual" == tipo:

            fecha=fecha.replace(year=(fecha.year+1))

        return fecha


    def crear_usuario_abonado_mensual(self,nombre,dni,tarjeta,vehiculo,tipo_bono):
        if tipo_bono == "mensual":
            if vehiculo.tipo=="turismo" and self.parking_service.plaza_turismo_disponible()!=-1:
                vehiculo.pin=random.randrange(1000,9999)
                plaza=self.parking_service.parking.lista_turismos[self.parking_service.plaza_turismo_disponible()]
                plaza.reservado=True
                plaza.vehiculo=vehiculo

                c1=cliente(vehiculo,dni,nombre,None)
                cliente_abono=abono(c1,tarjeta,"mensual",datetime.now(),self.sumar_fechas_meses("mensual"))
                c1.abono=cliente_abono
                self.cliente_repositorio.add_cliente(c1)

            if vehiculo.tipo=="motocicletas" and self.parking_service.plaza_motocicleta_disponible()!=-1:
                vehiculo.pin=random.randrange(1000,9999)
                plaza=self.parking_service.parking.lista_motocicletas[self.parking_service.plaza_motocicleta_disponible()]
                plaza.reservado=True
                plaza.vehiculo=vehiculo

                c1=cliente(vehiculo,dni,nombre,None)
                cliente_abono=abono(c1,tarjeta,"mensual",datetime.now(),self.sumar_fechas_meses("mensual"))
                c1.abono=cliente_abono
                self.cliente_repositorio.add_cliente(c1)

            if vehiculo.tipo=="minusvalido" and self.parking_service.plaza_minusvalido_disponible()!=-1:
                vehiculo.pin=random.randrange(1000,9999)
                plaza=self.parking_service.parking.lista_minusvalidos[self.parking_service.plaza_minusvalido_disponible]
                plaza.reservado=True
                plaza.vehiculo=vehiculo

                c1=cliente(vehiculo,dni,nombre,None)
                cliente_abono=abono(c1,tarjeta,"mensual",datetime.now(),self.sumar_fechas_meses("mensual"))
                c1.abono=cliente_abono
                self.cliente_repositorio.add_cliente(c1)

            fact=factura(cliente_abono,25)
            self.factura_repository.add_factura(fact)
