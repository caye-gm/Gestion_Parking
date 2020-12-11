from Models.cliente import *
from Repository.cliente_repository import *
from Models.Parking import *
from Service.parking_service import *

lista_motocicletas=[]
lista_turismos=[]
lista_minusvalidos=[]

parking=parking(lista_turismos,lista_motocicletas,lista_minusvalidos)
parking_service=parking_service(parking)
parking_service.inicilizar_array(30)

for i in parking.lista_minusvalidos:
    print(i)

c1= cliente(None,"12312",None)
lista_cliente=[c1]

cliente_repository=cliente_repository(lista_cliente)



