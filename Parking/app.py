from Models.cliente import *
from Repository.cliente_repository import *
from Models.Parking import *
from Service.parking_service import *
from Repository.cliente_repository import *
from Repository.vehiculo_repository import *
lista_motocicletas=[]
lista_turismos=[]
lista_minusvalidos=[]
lista_clientes=[]
lista_vehiculos=[]

cliente_repository=cliente_repository(lista_clientes)
vehiculo_repository=vehiculo_repository(lista_vehiculos)
parking=parking(lista_turismos,lista_motocicletas,lista_minusvalidos)
parking_service=parking_service(parking,cliente_repository,vehiculo_repository)

parking_service.inicilizar_parking(30)

parking_service.depositar_turismo("2134F")
parking_service.depositar_motocicleta("1235F")
parking_service.depositar_motocicleta("7235K")
parking_service.depositar_minusvalido("6735J")

print(parking)



