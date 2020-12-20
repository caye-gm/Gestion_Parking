from Models.cliente import *
from Repository.cliente_repository import *
from Repository.factura_repository import *
from Models.Parking import *
from Service.parking_service import *
from Repository.abono_repository import *
from Repository.cliente_repository import *
from Repository.vehiculo_repository import *
import pickle
from Service.AbonoService import *

#abono



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

a=datetime.now()
x = datetime(2020, 5, 17)
print(x)
x += timedelta(days=20)

print(x)

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

print("Bienvenido a CayeParking \nPulse 1 para depositar un vehiculo\nPulse 2 para retirar un vehiculo\Pulse 3 para "
      "abonarse\nPulse 4 en acceder como administrador\nPulse 5 para salir")


op=int(input())
if op==1:
    print("Pulse 1 para depositar como cliente sin abono\nPulse 2 para depositar como cliente abonado\nPulse 3 para depositar abonado\nPulse 0 para salir")
    op=int(input())
    if op == 1:
        print("Pulse 1 para depositar turismo\nPulse 2 para depositar vehiculo\nPulse 3 para depositar en plazas minusvalido")
        op = int(input())
        if op ==1:
            print("Introduce la matricula")
            parking_service.depositar_turismo(input())
        if op==2:
            print("Introduce la matricula")
            parking_service.depositar_motocicleta(input())
        if op==3:
            print("Introduce la matricula")
            parking_service.depositar_minusvalido(input())
    if op == 2:
            print("Introduce la matricula")
            matricula=input()
            print("Introduce el numero de plaza")
            numero_plaza = input()
            print("Introduce el pin")
            pin = input()

            parking_service.retirar_vehiculo(matricula,numero_plaza,pin,lista_recaudacion_cliente)


