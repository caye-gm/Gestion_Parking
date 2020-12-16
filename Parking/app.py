from Models.cliente import *
from Repository.cliente_repository import *
from Repository.factura_repository import *
from Models.Parking import *
from Service.parking_service import *
from Repository.abono_repository import *
from Repository.cliente_repository import *
from Repository.vehiculo_repository import *
from datetime import datetime
from Service.AbonoService import *
lista_motocicletas=[]
lista_turismos=[]
lista_minusvalidos=[]
lista_clientes=[]
lista_vehiculos=[]
lista_recaudacion_cliente=[]
lista_factura=[]
lista_abonos=[]

abono_repository=abono_repository(lista_abonos)
factura_repository=factura_repository(lista_factura)
cliente_repository=cliente_repository(lista_clientes)
vehiculo_repository=vehiculo_repository(lista_vehiculos)
parking=parking(lista_turismos,lista_motocicletas,lista_minusvalidos)
parking_service=parking_service(parking,cliente_repository,vehiculo_repository)
abono_service=abono_service(cliente_repository,vehiculo_repository,factura_repository,parking_service,abono_repository)

parking_service.inicilizar_parking(30)

parking_service.depositar_turismo("2134F")
parking_service.depositar_motocicleta("1235F")
parking_service.depositar_motocicleta("7235K")
parking_service.depositar_minusvalido("6735J")

print(parking)
print(lista_vehiculos)
print(parking_service.retirar_vehiculo("2134F",0,int(input()),lista_recaudacion_cliente))


abono_service.crear_usuario_abonado_mensual("caye","2313213","231312",vehiculo("1232F","turismo",None,None,None,None),"mensual")
abono_service.crear_usuario_abonado_trimestral("caye","2323213","2318313",vehiculo("1234F","motocicleta",None,None,None,None),"trimestral")
abono_service.crear_usuario_abonado_semestral("caye","2323222","2318313",vehiculo("1234F","minusvalido",None,None,None,None),"semestral")


print(parking)

print(lista_factura[0])
print(lista_factura[1])
print(lista_vehiculos[6])

abono_service.dar_baja("2323222")
print(parking)
print(lista_factura[2])

