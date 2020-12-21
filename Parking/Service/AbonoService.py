from Models.factura import *
from  Models.abono import *
from Models.cliente import *
from datetime import datetime, timedelta
import random
class abono_service():
    def __init__(self,cliente_repositorio,vehiculo_repositorio,factura_repository,parking_service,abono_repository):
        self.__cliente_repositorio=cliente_repositorio
        self.__vehiculo_repositorio=vehiculo_repositorio
        self.__factura_repository=factura_repository
        self.__parking_service=parking_service
        self.__abono_repository=abono_repository
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
    @property
    def abono_repository(self):
        return self.__abono_repository

    @abono_repository.setter
    def abono_repository(self, value):
        self.__abono_repository=value
    #segun el tipo de abono calcula la fecha de ahora mas su tiempo
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

    #este metodo lo explico en turismos pero als 3 condiciones son iguales pero apra distintos tipos de vehiculos
    def crear_usuario_abonado_mensual(self,nombre,dni,tarjeta,vehiculo,tipo_bono):
        if tipo_bono == "mensual":
            #comprobamos que es del tipo turismo y hay plaza disponible
            if vehiculo.tipo=="turismo" and self.parking_service.plaza_turismo_disponible()!=-1:
                #generamos un pin para el vehiculo que sera siempre el mismo
                vehiculo.pin=random.randrange(1000,9999)
                #plaza que se le va a asignar al abonado
                plaza=self.parking_service.parking.lista_turismos[self.parking_service.plaza_turismo_disponible()]
                #aqui ponemos la plaza en reservada y le asignamos el coche del cliente
                plaza.reservado=True
                plaza.vehiculo=vehiculo
                #al igual que al vehiculo le asignamos su plaza
                vehiculo.plaza=plaza
                #creamos al cliente
                c1=cliente(vehiculo,dni,nombre,None)
                #creamos el abono
                cliente_abono=abono(c1,tarjeta,"mensual",datetime.now(),self.sumar_fechas_meses("mensual"))
                #le asignamos el abono al cliente
                c1.abono=cliente_abono

                #guardamos en nuestros repositorios
                self.vehiculo_repositorio.add_vehiculo(vehiculo)
                self.cliente_repositorio.add_cliente(c1)
                self.abono_repository.add_abono(cliente_abono)

            if vehiculo.tipo=="motocicleta" and self.parking_service.plaza_motocicleta_disponible()!=-1:
                vehiculo.pin=random.randrange(1000,9999)
                plaza=self.parking_service.parking.lista_motocicletas[self.parking_service.plaza_motocicleta_disponible()]
                plaza.reservado=True
                vehiculo.plaza=plaza
                plaza.vehiculo=vehiculo
                c1=cliente(vehiculo,dni,nombre,None)
                cliente_abono=abono(c1,tarjeta,"mensual",datetime.now(),self.sumar_fechas_meses("mensual"))
                c1.abono=cliente_abono
                self.vehiculo_repositorio.add_vehiculo(vehiculo)
                self.cliente_repositorio.add_cliente(c1)
                self.abono_repository.add_abono(cliente_abono)

            if vehiculo.tipo=="minusvalido" and self.parking_service.plaza_minusvalido_disponible()!=-1:
                vehiculo.pin=random.randrange(1000,9999)
                plaza=self.parking_service.parking.lista_minusvalidos[self.parking_service.plaza_minusvalido_disponible()]
                plaza.reservado=True
                vehiculo.plaza=plaza
                plaza.vehiculo=vehiculo

                c1=cliente(vehiculo,dni,nombre,None)
                cliente_abono=abono(c1,tarjeta,"mensual",datetime.now(),self.sumar_fechas_meses("mensual"))
                c1.abono=cliente_abono

                self.vehiculo_repositorio.add_vehiculo(vehiculo)
                self.cliente_repositorio.add_cliente(c1)
                self.abono_repository.add_abono(cliente_abono)
            #si cliente abono noe sta vacio esos ignifica e que en algun momento se ha creado en otro if
            if cliente_abono!=None:
                #crea la factura
                fact=factura(cliente_abono,25)
                #la guarda
                self.factura_repository.add_factura(fact)
                return True
        return




    #este metodo lo explico en turismos pero als 3 condiciones son iguales pero apra distintos tipos de vehiculos
    def crear_usuario_abonado_trimestral(self,nombre,dni,tarjeta,vehiculo,tipo_bono):
        if tipo_bono == "trimestral":
            #comprobamos que es del tipo turismo y hay plaza disponible
            if vehiculo.tipo=="turismo" and self.parking_service.plaza_turismo_disponible()!=-1:
                #generamos un pin para el vehiculo que sera siempre el mismo
                vehiculo.pin=random.randrange(1000,9999)
                #plaza que se le va a asignar al abonado
                plaza=self.parking_service.parking.lista_turismos[self.parking_service.plaza_turismo_disponible()]
                #aqui ponemos la plaza en reservada y le asignamos el coche del cliente
                plaza.reservado=True
                plaza.vehiculo=vehiculo
                #al igual que al vehiculo le asignamos su plaza
                vehiculo.plaza=plaza
                #creamos al cliente
                c1=cliente(vehiculo,dni,nombre,None)
                #creamos el abono
                cliente_abono=abono(c1,tarjeta,"trimestral",datetime.now(),self.sumar_fechas_meses("trimestral"))
                #le asignamos el abono al cliente
                c1.abono=cliente_abono

                #guardamos en nuestros repositorios
                self.vehiculo_repositorio.add_vehiculo(vehiculo)
                self.cliente_repositorio.add_cliente(c1)
                self.abono_repository.add_abono(cliente_abono)

            if vehiculo.tipo=="motocicleta" and self.parking_service.plaza_motocicleta_disponible()!=-1:
                vehiculo.pin=random.randrange(1000,9999)
                plaza=self.parking_service.parking.lista_motocicletas[self.parking_service.plaza_motocicleta_disponible()]
                plaza.reservado=True
                vehiculo.plaza=plaza
                plaza.vehiculo=vehiculo
                c1=cliente(vehiculo,dni,nombre,None)
                cliente_abono=abono(c1,tarjeta,"trimestral",datetime.now(),self.sumar_fechas_meses("trimestral"))
                c1.abono=cliente_abono
                self.vehiculo_repositorio.add_vehiculo(vehiculo)
                self.cliente_repositorio.add_cliente(c1)
                self.abono_repository.add_abono(cliente_abono)

            if vehiculo.tipo=="minusvalido" and self.parking_service.plaza_minusvalido_disponible()!=-1:
                vehiculo.pin=random.randrange(1000,9999)
                plaza=self.parking_service.parking.lista_minusvalidos[self.parking_service.plaza_minusvalido_disponible()]
                plaza.reservado=True
                vehiculo.plaza=plaza
                plaza.vehiculo=vehiculo

                c1=cliente(vehiculo,dni,nombre,None)
                cliente_abono=abono(c1,tarjeta,"trimestral",datetime.now(),self.sumar_fechas_meses("trimestral"))
                c1.abono=cliente_abono

                self.vehiculo_repositorio.add_vehiculo(vehiculo)
                self.cliente_repositorio.add_cliente(c1)
                self.abono_repository.add_abono(cliente_abono)
            #si cliente abono noe sta vacio esos ignifica e que en algun momento se ha creado en otro if
            if cliente_abono!=None:
                #crea la factura
                fact=factura(cliente_abono,70)
                #la guarda
                self.factura_repository.add_factura(fact)
                return True
        return False


    #este metodo lo explico en turismos pero als 3 condiciones son iguales pero apra distintos tipos de vehiculos
    def crear_usuario_abonado_semestral(self,nombre,dni,tarjeta,vehiculo,tipo_bono):
        if tipo_bono == "semestral":
            #comprobamos que es del tipo turismo y hay plaza disponible
            if vehiculo.tipo=="turismo" and self.parking_service.plaza_turismo_disponible()!=-1:
                #generamos un pin para el vehiculo que sera siempre el mismo
                vehiculo.pin=random.randrange(1000,9999)
                #plaza que se le va a asignar al abonado
                plaza=self.parking_service.parking.lista_turismos[self.parking_service.plaza_turismo_disponible()]
                #aqui ponemos la plaza en reservada y le asignamos el coche del cliente
                plaza.reservado=True
                plaza.vehiculo=vehiculo
                #al igual que al vehiculo le asignamos su plaza
                vehiculo.plaza=plaza
                #creamos al cliente
                c1=cliente(vehiculo,dni,nombre,None)
                #creamos el abono
                cliente_abono=abono(c1,tarjeta,"semestral",datetime.now(),self.sumar_fechas_meses("semestral"))
                #le asignamos el abono al cliente
                c1.abono=cliente_abono

                #guardamos en nuestros repositorios
                self.vehiculo_repositorio.add_vehiculo(vehiculo)
                self.cliente_repositorio.add_cliente(c1)
                self.abono_repository.add_abono(cliente_abono)

            if vehiculo.tipo=="motocicleta" and self.parking_service.plaza_motocicleta_disponible()!=-1:
                vehiculo.pin=random.randrange(1000,9999)
                plaza=self.parking_service.parking.lista_motocicletas[self.parking_service.plaza_motocicleta_disponible()]
                plaza.reservado=True
                vehiculo.plaza=plaza
                plaza.vehiculo=vehiculo
                c1=cliente(vehiculo,dni,nombre,None)
                cliente_abono=abono(c1,tarjeta,"semestral",datetime.now(),self.sumar_fechas_meses("semestral"))
                c1.abono=cliente_abono
                self.vehiculo_repositorio.add_vehiculo(vehiculo)
                self.cliente_repositorio.add_cliente(c1)
                self.abono_repository.add_abono(cliente_abono)

            if vehiculo.tipo=="minusvalido" and self.parking_service.plaza_minusvalido_disponible()!=-1:
                vehiculo.pin=random.randrange(1000,9999)
                plaza=self.parking_service.parking.lista_minusvalidos[self.parking_service.plaza_minusvalido_disponible()]
                plaza.reservado=True
                vehiculo.plaza=plaza
                plaza.vehiculo=vehiculo

                c1=cliente(vehiculo,dni,nombre,None)
                cliente_abono=abono(c1,tarjeta,"semestral",datetime.now(),self.sumar_fechas_meses("semestral"))
                c1.abono=cliente_abono

                self.vehiculo_repositorio.add_vehiculo(vehiculo)
                self.cliente_repositorio.add_cliente(c1)
                self.abono_repository.add_abono(cliente_abono)
            #si cliente abono noe sta vacio esos ignifica e que en algun momento se ha creado en otro if
            if cliente_abono!=None:
                #crea la factura
                fact=factura(cliente_abono,130)
                #la guarda
                self.factura_repository.add_factura(fact)
                return True
        return False



    #este metodo lo explico en turismos pero als 3 condiciones son iguales pero apra distintos tipos de vehiculos
    def crear_usuario_abonado_anual(self,nombre,dni,tarjeta,vehiculo,tipo_bono):
        if tipo_bono == "anual":
            #comprobamos que es del tipo turismo y hay plaza disponible
            if vehiculo.tipo=="turismo" and self.parking_service.plaza_turismo_disponible()!=-1:
                #generamos un pin para el vehiculo que sera siempre el mismo
                vehiculo.pin=random.randrange(1000,9999)
                #plaza que se le va a asignar al abonado
                plaza=self.parking_service.parking.lista_turismos[self.parking_service.plaza_turismo_disponible()]
                #aqui ponemos la plaza en reservada y le asignamos el coche del cliente
                plaza.reservado=True
                plaza.vehiculo=vehiculo
                #al igual que al vehiculo le asignamos su plaza
                vehiculo.plaza=plaza
                #creamos al cliente
                c1=cliente(vehiculo,dni,nombre,None)
                #creamos el abono
                cliente_abono=abono(c1,tarjeta,"anual",datetime.now(),self.sumar_fechas_meses("anual"))
                #le asignamos el abono al cliente
                c1.abono=cliente_abono

                #guardamos en nuestros repositorios
                self.vehiculo_repositorio.add_vehiculo(vehiculo)
                self.cliente_repositorio.add_cliente(c1)
                self.abono_repository.add_abono(cliente_abono)

            if vehiculo.tipo=="motocicleta" and self.parking_service.plaza_motocicleta_disponible()!=-1:
                vehiculo.pin=random.randrange(1000,9999)
                plaza=self.parking_service.parking.lista_motocicletas[self.parking_service.plaza_motocicleta_disponible()]
                plaza.reservado=True
                vehiculo.plaza=plaza
                plaza.vehiculo=vehiculo
                c1=cliente(vehiculo,dni,nombre,None)
                cliente_abono=abono(c1,tarjeta,"anual",datetime.now(),self.sumar_fechas_meses("anual"))
                c1.abono=cliente_abono
                self.vehiculo_repositorio.add_vehiculo(vehiculo)
                self.cliente_repositorio.add_cliente(c1)
                self.abono_repository.add_abono(cliente_abono)

            if vehiculo.tipo=="minusvalido" and self.parking_service.plaza_minusvalido_disponible()!=-1:
                vehiculo.pin=random.randrange(1000,9999)
                plaza=self.parking_service.parking.lista_minusvalidos[self.parking_service.plaza_minusvalido_disponible()]
                plaza.reservado=True
                vehiculo.plaza=plaza
                plaza.vehiculo=vehiculo

                c1=cliente(vehiculo,dni,nombre,None)
                cliente_abono=abono(c1,tarjeta,"anual",datetime.now(),self.sumar_fechas_meses("anual"))
                c1.abono=cliente_abono

                self.vehiculo_repositorio.add_vehiculo(vehiculo)
                self.cliente_repositorio.add_cliente(c1)
                self.abono_repository.add_abono(cliente_abono)
            #si cliente abono noe sta vacio esos ignifica e que en algun momento se ha creado en otro if
            if cliente_abono!=None:
                #crea la factura
                fact=factura(cliente_abono,130)
                #la guarda
                self.factura_repository.add_factura(fact)
                return True
        return False

    def dar_baja(self,dni):
        cliente=self.cliente_repositorio.findByDni(dni)

        if cliente!=None:
            self.parking_service.plaza_vacia(cliente.vehiculo.plaza)
            self.abono_repository.delete_abono(cliente.abono)
            self.vehiculo_repositorio.delete_vehiculo(cliente.vehiculo)
            self.cliente_repositorio.removeByDni(cliente.dni)
            print("Realizado con exito :D")
            return True
        return print("Error")


    def obtener_abonos_mes(self,mes):
        abonos=self.abono_repository.lista_abonos
        for i in abonos:
            if i.fecha_cancelacion.month == mes:
                print(i)

    def obtener_caducidad_diez_dias(self):
        abonos=self.abono_repository
        date=datetime.now()
        date += timedelta(days=10)
        for i in abonos:
            if i.fecha_cancelacion < date and i.fecha_cancelacion > datetime.now():
                print(i)

    def renovar_mensual(self,tipo,cliente):
        if cliente != None and tipo=="mensual":
            cliente_abono = cliente.abono
            cliente_abono.tipo = tipo
            cliente_abono.fecha_activacion = datetime.now()
            cliente_abono.fecha_cancelacion = self.sumar_fechas_meses(tipo)

            fact = factura(cliente_abono, 25)
            self.factura_repository.add_factura(fact)
            return True
        return False

    def renovar_trimestral(self,tipo,cliente):
        if tipo=="trimestral":
            cliente_abono = cliente.abono
            cliente_abono.tipo = tipo
            cliente_abono.fecha_activacion = datetime.now()
            cliente_abono.fecha_cancelacion = self.sumar_fechas_meses(tipo)

            fact = factura(cliente_abono, 70)
            self.factura_repository.add_factura(fact)
            return True
        return False

    def renovar_semestral(self,tipo,cliente):
        if tipo=="semestral":
            cliente_abono = cliente.abono
            cliente_abono.tipo = tipo
            cliente_abono.fecha_activacion = datetime.now()
            cliente_abono.fecha_cancelacion = self.sumar_fechas_meses(tipo)

            fact = factura(cliente_abono, 130)
            self.factura_repository.add_factura(fact)
            return True
        return False

    def renovar_anual(self,tipo,cliente):
        if tipo=="anual":
            cliente_abono = cliente.abono
            cliente_abono.tipo = tipo
            cliente_abono.fecha_activacion = datetime.now()
            cliente_abono.fecha_cancelacion = self.sumar_fechas_meses(tipo)
            fact = factura(cliente_abono, 200)
            self.factura_repository.add_factura(fact)
            return True
        return False


    def modificar_tiempo_abono(self,dni,tipo):
        cliente = self.cliente_repositorio.findByDni(dni)
        if cliente != None:
            self.renovar_mensual(tipo,cliente)
            self.renovar_trimestral(tipo,cliente)
            self.renovar_semestral(tipo,cliente)
            self.renovar_anual(tipo, cliente)
            print("Realizado con exito")
            return True
        return print("Ha habido un error , el cliente no se encuentra")
