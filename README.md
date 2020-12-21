# Proyecto_Python_Parking
Proyecto sobre la gestión de un parking se realizara con javascript y node

# Programa


## Funciones:

### ZONA CLIENTE
En la zona cliente de la aplicación se pueden realizar básicamente las siguientes acciones:
Depositar vehículo
El sistema informa en todo momento del número de plazas libres que existen de cada tipo.
El cliente introduce la matrícula y el tipo (turismo, motocicleta o caravana). El sistema asigna una plaza de las posibles, si existen plazas libres. El cliente debe aparcar en la plaza asignada.
El sistema genera un ticket donde aparece la matrícula del vehículo, la fecha de depósito, el identificador de la plaza asignada y un pin de seis dígitos numéricos que servirá para retirar el vehículo posteriormente. Este ticket aparecerá en la consola del sistema. Esta información se debe guardar de forma persistente para poder ser consultada cuando el cliente proceda a la retirada del vehículo.
No es necesario guardar información de los clientes si se hace uso del parking sin abono.
Retirar vehículo
El cliente introduce la matrícula, el identificador de la plaza y el pin asociado. El sistema calcula el coste total a pagar e informa de la tarifa al cliente.
Una vez realizado el pago, el cliente puede recoger el vehículo y salir del parking. El sistema actualiza el número de plazas libres, así como la información relativa al coste final y fecha de salida del vehículo.
Los cobros realizados se deben guardar en una colección para, posteriormente, poder consultarlos desde la zona de administración. 
Depositar abonados
El cliente abonado introduce en el sistema la matrícula del vehículo y su DNI. Se supone que un cliente tiene un solo vehículo y un vehículo pertenece a un solo cliente.
El cliente aparca el vehículo en la plaza asignada al abono y el sistema actualiza el estado de la plaza para saber que el vehículo del abonado está en el parking. Asocia siempre el mismo pin para poder retirar el vehículo tantas veces como sea necesario. El PIN se genera al crear el abono del cliente.
De los clientes abonados es necesario saber su DNI, nombre, apellidos, número de tarjeta de crédito, tipo de abono que tienen y su email.
Retirar abonados
El cliente introduce la matrícula, el identificador de plaza asignada y el pin.
El sistema actualiza el estado de la plaza del parking, que no queda libre, sigue estando reservada, pero el vehículo del abonado no está en el parking.

### ZONA ADMINISTRADOR

La zona admin de la aplicación se encarga de:
Estado del parking
Controlar el estado del parking. Se debe mostrar por pantalla el estado de las plazas (libre, ocupada, abono ocupada y abono libre) y el identificador de cada plaza.
Facturación
Entre fechas. El sistema solicita dos fechas y horas concretas para saber los cobros realizados entre las mismas. Los abonos no se contemplan en esta opción.
Consulta de Abonados. 
El sistema informa de los abonos anuales, con los cobros realizados.
Abonos
Alta. El sistema solicita datos personales del abonado y un número de tarjeta donde se realizan los cargos mensuales del abono. El cliente debe elegir entre los distintos abonos: mensual (25€), trimestral (70€), semestral (130€) y anual (200€). Todos los abonos tienen una fecha de activación y una fecha de cancelación. La fecha de activación se actualiza con la fecha en la que se da de alta y la fecha de cancelación se calcula en función del tipo de abono.
Modificación. Existirá la opción de cambiar los datos personales del abonado o bien cambiar la fecha de cancelación del abono, porque el abono ha sido renovado.
Baja. Se eliminará el registro del abonado pero no se podrán borrar los datos asociados a su facturación.
Caducidad de abonos
Mes. El sistema solicita un mes y nos informa de los abonos que caducan en ese mes.
Consultar últimos 10 días. El programa informa por consola de los abonos que caducan en los siguientes 10 días a la fecha actual.



