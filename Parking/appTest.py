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




print(parking)
print(vehiculo_repository.lista_vehiculos)
print(parking_service.retirar_vehiculo("2134F",0,int(input()),lista_recaudacion_cliente))


abono_service.crear_usuario_abonado_mensual("caye","2313213","231312",vehiculo("1232F","turismo",None,None,None,None),"mensual")
abono_service.crear_usuario_abonado_trimestral("caye","2323213","2318313",vehiculo("1234F","motocicleta",None,None,None,None),"trimestral")
abono_service.crear_usuario_abonado_semestral("caye","2323222","2318313",vehiculo("1234F","minusvalido",None,None,None,None),"semestral")


print(parking)

factura_repository.factura_findAll()



abono_service.dar_baja("2323222")
print(parking)


