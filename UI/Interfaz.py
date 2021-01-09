from model import Cliente, Factura, ControlPlaga, ControlFertilizante, Antibiotico
from datetime import datetime


def leerFacturas(listaClientes):

    print('\n\tNUEVA FACTURA')
    nombreCliente = input('Ingrese el nombre del cliente: ')
    cedulaCliente = input('Ingrese la cédula del cliente: ')

    respuestaClienteNuevo = clienteEsNuevo(nombreCliente, cedulaCliente, listaClientes)
    if respuestaClienteNuevo:
        factura = crearFactura(len(listaClientes) + 1)
        montoRecibido = float(input('Ingrese el monto con el que va a pagar: '))
        cliente = Cliente.Cliente(nombreCliente, cedulaCliente)
        cliente.asociar(factura)
        listaClientes.append(cliente)
        mostrarFactura(factura, cliente, montoRecibido)
        mostrarFormulacion(factura)
    elif not respuestaClienteNuevo:
        factura = crearFactura(len(listaClientes) + 1)
        montoRecibido = float(input('Ingrese el monto con el que va a pagar: '))
        posicionCliente = posicionClienteAntiguo(nombreCliente, cedulaCliente, listaClientes)
        listaClientes[posicionCliente].asociar(factura)
        mostrarFactura(factura, listaClientes[posicionCliente], montoRecibido)
        mostrarFormulacion(factura)
    else:
        print('Conflicto de identidad, verifique los datos e intente de nuevo')
    return listaClientes


def clienteEsNuevo(nombre, cedula, listaClientes):
    respuesta = None
    if len(listaClientes) >= 1:
        for c in listaClientes:
            if nombre == c.nombre and cedula == c.cedula:
                respuesta = False
            elif cedula == c.cedula:
                respuesta = 'conflicto'
            else:
                respuesta = True
    else:
        respuesta = True
    return respuesta


def posicionClienteAntiguo(nombre, cedula, listaClientes):
    for c in listaClientes:
        if nombre == c.nombre and cedula == c.cedula:
            return listaClientes.index(c)


def crearFactura(numeroFactura):
    fecha = str(datetime.now().date())  # Fecha actual
    hora = str(datetime.now().time())  # Hora actual
    factura = Factura.Factura(numeroFactura, fecha, hora)
    respuesta = 'si'
    while respuesta == 'si':
        print('Añada un producto a su compra (antibiotico, control de plagas o fertilizante)')
        tipoProducto = input('\tIngrese el tipo del producto: ')

        if tipoProducto == 'antibiotico':
            factura.asociar(crearAntibiotico())
        elif tipoProducto == 'control de plagas':
            factura.asociar(crearControlPlaga())
        elif tipoProducto == 'fertilizante':
            factura.asociar(crearFertilizante())
        else:
            print('\tError en el tipo de producto, intente de nuevo')
        respuesta = input('Desea agregar otro producto?(si/no): ')
    return factura


def crearAntibiotico():
    nombre = input('\tIngrese el nombre del antibiótico: ')
    tipoAnimal = input('\tIngrese el tipo del animal: ')
    dosis = input('\tIngrese la dosis: ')
    precio = float(input('\tIngrese el precio: '))
    return Antibiotico.Antibiotico(nombre, tipoAnimal, dosis, precio)


def crearControlPlaga():
    nombre = input('\tIngrese el nombre del control de plagas: ')
    registroICA = input('\tIngrese el registro ICA: ')
    frecuenciaAplicacion = input('\tIngrese la frecuencia de aplicación: ')
    periodoCarencia = input('\tIngrese el periodo de carencia: ')
    precio = float(input('\tIngrese el precio: '))
    return ControlPlaga.ControlPlaga(nombre, registroICA, frecuenciaAplicacion, precio, periodoCarencia)


def crearFertilizante():
    nombre = input('\tIngrese el nombre del fertilizante: ')
    registroICA = input('\tIngrese el registro ICA: ')
    frecuenciaAplicacion = input('\tIngrese la frecuencia de aplicación: ')
    ultimaAplicacion = input('\tIngrese la fecha de la última aplicación: ')
    precio = float(input('\tIngrese el precio: '))
    return ControlFertilizante.ControlFertilizante(nombre, registroICA, frecuenciaAplicacion, precio, ultimaAplicacion)


def mostrarFactura(factura, cliente, montoRecibido):
    print('\n________________________________________________')
    print('TIENDA AGRÍCOLA')
    factura.mostrarDatos()
    cliente.mostrarCliente()
    print(f'Compras realizadas últimamente: {len(cliente.facturas)}')
    factura.mostrarProductos()
    print(f'Recibido: {montoRecibido}')
    print(f'Cambio: {montoRecibido - factura.valorTotalCompra}')
    print('GRACIAS POR SU COMPRA')
    print('VUELVA PRONTO')
    print('________________________________________________')


def mostrarFormulacion(factura):
    print('FORMULACIÓN')
    print('Siga todos los pasos para garantizar el buen', 'funcionamiento de los productos', sep="\n")
    productos = factura.productosControl + factura.antibioticos
    for p in productos:
        if isinstance(p, Antibiotico.Antibiotico):
            print(f'\n*{p.nombre} (Antibiótico)')
            print(f'\tSolo aplicar a animales del tipo {p.tipoAnimal}')
            print(f'\tSuministrar en dosis de {p.dosis}')
        elif isinstance(p, ControlPlaga.ControlPlaga):
            print(f'\n*{p.nombre} (Control de plagas)')
            print(f'\tAplicar cada {p.frecuenciaAplicacion}')
            print(f'\tPeriodo de carencia: {p.periodoCarencia}')
        else:
            print(f'\n*{p.nombre} (Fertilizante)')
            print(f'\tAplicar cada {p.frecuenciaAplicacion}')
            print(f'\tFecha de la última aplicación: {p.ultimaAplicacion}')
    print('________________________________________________')
