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

lista_motocicletas=[]
lista_turismos=[]
lista_minusvalidos=[]
lista_clientes=[]
lista_vehiculos=[]
lista_recaudacion_cliente=[]
lista_factura=[]
lista_abonos=[]

#abono
bd_abono_repo_w= open("./db/abonos","wb")
pickle.dump(lista_abonos,bd_abono_repo_w)
bd_abono_repo_w.close()

bd_abono_repo_r= open("./db/abonos","rb")
lista_abonos_bd=pickle.load(bd_abono_repo_r)
bd_abono_repo_r.close()

abono_repository=abono_repository(lista_abonos_bd)
#factura
bd_factura_repo_w= open("./db/facturas","wb")
pickle.dump(lista_factura,bd_factura_repo_w)
bd_factura_repo_w.close()

bd_factura_repo_r= open("./db/facturas","rb")
lista_factura_bd=pickle.load(bd_factura_repo_r)
bd_factura_repo_r.close()

factura_repository=factura_repository(lista_factura_bd)
#cliente
bd_cliente_repo_w= open("./db/clientes","wb")
pickle.dump(lista_clientes,bd_cliente_repo_w)
bd_cliente_repo_w.close()

bd_cliente_repo_r= open("./db/clientes","rb")
lista_cliente_bd=pickle.load(bd_cliente_repo_r)
bd_cliente_repo_r.close()

cliente_repository=cliente_repository(lista_cliente_bd)
#vehiculos
bd_vehiculos_repo_w= open("./db/vehiculos","wb")
pickle.dump(lista_vehiculos,bd_vehiculos_repo_w)
bd_vehiculos_repo_w.close()

bd_vehiculos_repo_r= open("./db/vehiculos","rb")
lista_vehiculos_bd=pickle.load(bd_vehiculos_repo_r)
bd_vehiculos_repo_r.close()

vehiculo_repository=vehiculo_repository(lista_vehiculos_bd)



parking=parking(lista_turismos,lista_motocicletas,lista_minusvalidos)
parking_service=parking_service(parking,cliente_repository,vehiculo_repository)
abono_service=abono_service(cliente_repository,vehiculo_repository,factura_repository,parking_service,abono_repository)

parking_service.inicilizar_parking(30)

parking_service.depositar_turismo("2134F")
parking_service.depositar_motocicleta("1235F")
parking_service.depositar_motocicleta("7235K")
parking_service.depositar_minusvalido("6735J")



abono_service.crear_usuario_abonado_mensual("caye","2313213","231312",vehiculo("1232F","turismo",None,None,None,None),"mensual")
abono_service.crear_usuario_abonado_trimestral("caye","2323213","2318313",vehiculo("1234F","motocicleta",None,None,None,None),"trimestral")
abono_service.crear_usuario_abonado_semestral("caye","2323222","2318313",vehiculo("1234F","minusvalido",None,None,None,None),"semestral")


while True:

    while True:
        print("Bienvenido a CayeParking \nPulse 1 para depositar un vehiculo\nPulse 2 para retirar un vehiculo\nPulse 3 para "
      "abonarse\nPulse 4 en acceder como administrador\nPulse 0 para salir")
        op=int(input())
        if op==1:
            while True:
                print("Pulse 1 para depositar como cliente sin abono\nPulse 2 para depositar como cliente abonado\nPulse 0 para salir")
                op=int(input())
                if op == 1:
                    while True:
                        print("Pulse 1 para depositar turismo\nPulse 2 para depositar motocicleta\nPulse 3 para depositar en plazas minusvalido\nPulse 0 para salir")
                        op1 = int(input())
                        if op1 ==1:
                            print("Introduce la matricula")
                            parking_service.depositar_turismo(str(input()))
                        elif op1==2:
                            print("Introduce la matricula")
                            parking_service.depositar_motocicleta(str(input()))
                        elif op1==3:
                            print("Introduce la matricula")
                            parking_service.depositar_minusvalido(str(input()))
                        elif op1==0:
                            break
                if op == 2:
                    print("Introduce la matricula")
                    matricula=str(input())
                    print("Introduce el DNI")
                    dni = str(input())
                    parking_service.depositar_cliente_abonado(matricula,dni)
                if op == 0:
                    break

        if op==2:
            while True:
                print("Pulse 1 para retirar como cliente sin abono\nPulse 2 para retirar como cliente abonado\nPulse 0 para salir")
                op2 = int(input())
                if op2 ==1:
                    print("Introduce la matricula")
                    matricula=str(input())
                    print("Introduce la plaza")
                    numplaza=int(input())
                    print("Introduce el pin")
                    pin=int(input())
                    parking_service.retirar_vehiculo(matricula,numplaza,pin,lista_recaudacion_cliente)
                if op2 ==2:
                    print("Introduce la matricula")
                    matricula=str(input())
                    print("Introduce la plaza")
                    numplaza=int(input())
                    print("Introduce el pin")
                    pin=int(input())
                    parking_service.retirar_vehiculo_cliente_abonado(matricula,numplaza,pin)
                if op2 == 0:
                    break
        if op==3:
            while True:
                print("Pulse 1 para registrarse como usuario mensual\nPulse 2 para registrarse como usuario trimestral\nPulse 3 para registrarse como usuario semestral\n"
                      "Pulse 4 para registrarse como usuario anual\nPulse 0 para salir")
                op3=int(input())
                if op3 == 1:

                    print("Introduce tu nombre completo")
                    nombre=str(input())
                    print("Introduce tu DNI")
                    dni=str(input())
                    print("Introduce tu tarjeta bancaria")
                    tarjeta=str(input())
                    print("Introduce la matricula de tu vehiculo")
                    matricula=str(input())
                    while True:
                        print("Pulse 1 si es un turismo\nPulse 2 si es una motocicleta"
                            "\nPulse 3 si es un vehiculo con plaza minusválido")
                        op4=int(input())
                        if op4== 1:
                            tipo="turismo"
                            break
                        if op4== 2:
                            tipo="motocicleta"
                            break
                        if op4== 3:
                            tipo="minusvalido"
                            break
                    vehi=vehiculo(matricula,tipo,None,None,datetime.now(),None)
                    abono_service.crear_usuario_abonado_mensual(nombre,dni,tarjeta,vehi,"mensual")

                if op3 == 2:
                    print("Introduce tu nombre completo")
                    nombre=str(input())
                    print("Introduce tu DNI")
                    dni=str(input())
                    print("Introduce tu tarjeta bancaria")
                    tarjeta=str(input())
                    print("Introduce la matricula de tu vehiculo")
                    matricula=str(input())
                    while True:
                        print("Pulse 1 si es un turismo\nPulse 2 si es una motocicleta"
                            "\nPulse 3 si es un vehiculo con plaza minusválido")
                        op4=int(input())
                        if op4== 1:
                            tipo="turismo"
                            break
                        if op4== 2:
                            tipo="motocicleta"
                            break
                        if op4== 3:
                            tipo="minusvalido"
                            break
                    vehi=vehiculo(matricula,tipo,None,None,datetime.now(),None)
                    abono_service.crear_usuario_abonado_trimestral(nombre,dni,tarjeta,vehi,"trimestral")

                if op3 == 3:

                    print("Introduce tu nombre completo")
                    nombre=str(input())
                    print("Introduce tu DNI")
                    dni=str(input())
                    print("Introduce tu tarjeta bancaria")
                    tarjeta=str(input())
                    print("Introduce la matricula de tu vehiculo")
                    matricula=str(input())
                    while True:
                        print("Pulse 1 si es un turismo\nPulse 2 si es una motocicleta"
                            "\nPulse 3 si es un vehiculo con plaza minusválido")
                        op4=int(input())
                        if op4== 1:
                            tipo="turismo"
                            break
                        if op4== 2:
                            tipo="motocicleta"
                            break
                        if op4== 3:
                            tipo="minusvalido"
                            break
                    vehi=vehiculo(matricula,tipo,None,None,datetime.now(),None)
                    abono_service.crear_usuario_abonado_semestral(nombre,dni,tarjeta,vehi,"semestral")

                if op3 == 4:
                    print("Introduce tu nombre completo")
                    nombre=str(input())
                    print("Introduce tu DNI")
                    dni=str(input())
                    print("Introduce tu tarjeta bancaria")
                    tarjeta=str(input())
                    print("Introduce la matricula de tu vehiculo")
                    matricula=str(input())
                    while True:
                        print("Pulse 1 si es un turismo\nPulse 2 si es una motocicleta"
                            "\nPulse 3 si es un vehiculo con plaza minusválido")
                        op4=int(input())
                        if op4== 1:
                            tipo="turismo"
                            break
                        if op4== 2:
                            tipo="motocicleta"
                            break
                        if op4== 3:
                            tipo="minusvalido"
                            break
                    vehi=vehiculo(matricula,tipo,None,None,datetime.now(),None)
                    abono_service.crear_usuario_abonado_anual(nombre,dni,tarjeta,vehi,"anual")
                if op3 == 0:
                    break
        if op==4:
            while True:
                print("Pulse 1 para ver el estado del parking\nPulse 2 para ver la facturación total de usuarios sin abonos\nPulse 3 para acceder al menu de abonados\nPulse 0 para salir")
                op5=int(input())
                if op5==1:
                    print(parking)
                if op5==2:
                    total=0
                    for i in lista_recaudacion_cliente:
                        total+=i
                    print(f"El total recaudado es de :{total} asi que atrae a clientes!!!!")
                if op5==3:
                    print()

                if op5==0:
                    break
        if op==5:
            print(parking)
