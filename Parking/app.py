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
while True:
    print("Antes de empezar seleciona las plazas que tiene tu parking recuerda que el 70% sera de coches y un 15% motocicletas y 15% turismos")
    print("El minimo sera de 10 plazas y maximo a tu gusto pero se recomienda 30 plazas!")
    try:
        plazas_totales=int(input())

        if plazas_totales<10:
            raise ValueError
        if plazas_totales>=10:
            break
    except ValueError:
        print("Error de exepcion: Introduzca un valor de 10 en adelante")


parking_service.inicilizar_parking(plazas_totales)

parking_service.depositar_turismo("2134FDF")
parking_service.depositar_motocicleta("1235F")
parking_service.depositar_minusvalido("6735JJK")

abono_service.crear_usuario_abonado_mensual("Pablo Diaz Silva","49388230A","2132231213123",vehiculo("9576KAA","turismo",None,None,datetime.now(),None),"mensual")
abono_service.crear_usuario_abonado_trimestral("Juan Perez Perez","90057429Z","2318313213",vehiculo("7245JDP","motocicleta",None,None,datetime.now(),None),"trimestral")
abono_service.crear_usuario_abonado_semestral("Cayetano García Gomez","64241849Y","6876878768",vehiculo("2756FDJ","minusvalido",None,None,datetime.now(),None),"semestral")
abono_service.crear_usuario_abonado_anual("Pepe García Rubio","32456709A","213213213213",vehiculo("7566DAA","turismo",None,None,datetime.now(),None),"anual")
parking_service.depositar_turismo("3242DXD")
parking_service.depositar_turismo("9334JKD")
parking_service.depositar_turismo("7242HVH")

while True:


      print("Bienvenido a CayeParking \nPulse 1 para depositar un vehiculo\nPulse 2 para retirar un vehiculo\nPulse 3 para "
      "abonarse\nPulse 4 en acceder como administrador\nPulse 0 para salir")
      try:
        op=int(input())
        if op!=1 and op!=2 and op!=3 and op!=4 and op!=0:
            raise ValueError
        if op==1:
            while True:
                try:
                    print("Pulse 1 para depositar como cliente sin abono\nPulse 2 para depositar como cliente abonado\nPulse 0 para salir")
                    op7=int(input())
                    if op7!=1 and op7!=2 and op7!=0:
                        raise ValueError
                    if op7 == 1:
                        while True:
                            try:
                                print("Pulse 1 para depositar turismo\nPulse 2 para depositar motocicleta\nPulse 3 para depositar en plazas minusvalido\nPulse 0 para salir")
                                op1 = int(input())
                                if op1!=1 and op1!=2 and op1!=3 and op1!=0:
                                    raise ValueError
                                if op1 ==1:
                                    print("Introduce la matricula")
                                    if parking_service.depositar_turismo(str(input())) == True:
                                        print("Añadido con existo")
                                    else:
                                        print("El parking esta lleno")

                                elif op1==2:
                                    print("Introduce la matricula")
                                    if parking_service.depositar_motocicleta(str(input())) == True:
                                        print("Añadido con existo")
                                    else:
                                        print("El parking esta lleno")

                                elif op1==3:
                                    print("Introduce la matricula")
                                    if parking_service.depositar_minusvalido(str(input())) == True:
                                        print("Añadido con existo")
                                    else:
                                        print("El parking esta lleno")

                                elif op1==0:
                                    break

                            except ValueError:
                                print("Error de exepcion: Introduzca un valor adecuado")

                    if op7 == 2:
                        print("Introduce la matricula")
                        matricula=str(input())
                        print("Introduce el DNI")
                        dni = str(input())
                        parking_service.depositar_cliente_abonado(matricula,dni)
                    if op7 == 0:
                        break
                except ValueError:
                    print("Error de exepcion: Introduzca un valor adecuado")
        if op==2:
            while True:
                try:
                    print("Pulse 1 para retirar como cliente sin abono\nPulse 2 para retirar como cliente abonado\nPulse 0 para salir")
                    op2 = int(input())
                    if op2!=1 and op2!=2 and op1!=0:
                        raise ValueError

                    if op2 ==1:
                        print("Introduce la matricula")
                        matricula=str(input())
                        print("Introduce la plaza")
                        numplaza=int(input())
                        print("Introduce el pin")
                        pin=int(input())
                        if parking_service.retirar_vehiculo(matricula,numplaza,pin,lista_recaudacion_cliente)== True:
                            print("retirado con exito")
                        else:
                            print("Error datos erroneos")
                    if op2 ==2:
                        print("Introduce la matricula")
                        matricula=str(input())
                        print("Introduce la plaza")
                        numplaza=int(input())
                        print("Introduce el pin")
                        pin=int(input())

                        if parking_service.retirar_vehiculo_cliente_abonado(matricula,numplaza,pin)==True:
                            print("Retirado con exito")
                        else:
                            print("Error datos erroneos")

                    if op2 == 0:
                        break
                except ValueError:
                    print("Error de exepcion: Introduzca un valor adecuado")
        if op==3:
            while True:
                try:
                    print("Pulse 1 para registrarse como usuario mensual\nPulse 2 para registrarse como usuario trimestral\nPulse 3 para registrarse como usuario semestral\n"
                          "Pulse 4 para registrarse como usuario anual\nPulse 0 para salir")
                    op3=int(input())
                    if op3!=1 and op3!=2 and op3!=3 and op3!=4 and op3!=0:
                        raise ValueError
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
                        if abono_service.crear_usuario_abonado_semestral(nombre,dni,tarjeta,vehi,"semestral") == True:
                            print("aboando con exito")
                        else:
                            print("error")


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
                except ValueError:
                            print("Error de exepcion: Introduzca un valor adecuado")
            if op==4:
                while True:
                    try:
                        print("Pulse 1 para ver el estado del parking\nPulse 2 para ver la facturación total de usuarios sin abonos\nPulse 3 para acceder al menu de abonados\nPulse 0 para salir")
                        op5=int(input())
                        if op5!=1 and op5!=2 and op5!=3 and op5!=0:
                            raise ValueError
                        if op5==1:
                            print(parking)
                        if op5==2:
                            total=0
                            for i in lista_recaudacion_cliente:
                                total+=i
                            print(f"El total recaudado es de :{total} asi que atrae a clientes!!!!")
                        if op5==3:
                            while True:
                                try:
                                    print("Pulse 1 para ver todos los abonado activos\nPulse 2 para ver la facturación total\nPulse 3 para modificar el plan del abonado\nPulse 4 para dar de baja a un abonado\nPulsa 5 para consultar los abonos"
                                          "que caducan los proximos 10 dias\nPulsa 6 para consultar los abonos que caducan en un mes\nPulse 0 para salir")
                                    op6=int(input())
                                    if op6!=1 and op6!=2 and op6!=3 and op6!=4 and op6!=5 and op6!=6 and op6!=0:
                                        raise ValueError
                                    if op6==1:
                                        print("hola")
                                        print(abono_repository.find_all())
                                    if op6==2:
                                        print(f"El total recaudado es : {factura_repository.calcular_total()} €")
                                    if op6==3:
                                        print("Introduce el DNI de el usuario")
                                        dni=str(input())
                                        print("Seleciona a que tipo de abono quiere seleccionar recuerda q2ue se le ejecutara un cobro en la tarjeta")
                                        while True:
                                            try:
                                                print("Pulse 1 para actualizar el abono a mensual\nPulse 2 para actualizar el abono a trimestral\nPulse 3 para actualizar el abono a semestral"
                                                "\nPulse 4 para actualizar el abono a anual")

                                                op7=int(input())
                                                if op7!=1 and op7!=2 and op7!=3 and op7!=4:
                                                    raise ValueError
                                                if op7 ==1:
                                                    tipo="mensual"
                                                if op7 ==2:
                                                    tipo="trimestral"
                                                if op7 ==3:
                                                    tipo="semestral"
                                                if op7 ==4:
                                                    tipo="anual"
                                            except ValueError:
                                                print("Error de exepcion: Introduzca un valor adecuado")
                                        abono_service.modificar_tiempo_abono(dni,tipo)

                                    if op6==4:
                                        print("Introduce el DNI de el usuario")
                                        dni = str(input())
                                        abono_service.dar_baja(dni)

                                    if op6==5:
                                        abono_service.obtener_caducidad_diez_dias()
                                    if op6==6:
                                        print("Introduce el mes || ejemplo: mes 8")
                                        mes = int(input())
                                        abono_service.obtener_abonos_mes(mes)
                                    if op6==0:
                                        break
                                except ValueError:
                                    print("Error de exepcion: Introduzca un valor adecuado")
                        if op5==0:
                            break
                    except ValueError:
                            print("Error de exepcion: Introduzca un valor adecuado")
        if op==0:
            break

      except ValueError:
        print("Error de exepcion: Introduzca un valor adecuado")
