from UI import Interfaz


print('\nBIENVENIDO AL SISTEMA DE FACTURACIÓN DE LA TIENDA AGRÍCOLA, INGRESE TODAS LAS FACTURAS QUE DESEE')
listaClientes = list()
salir = 'no'
while salir == 'no':
    # Actualiza la lista de clientes y al mismo tiempo muestra la factura
    listaClientes = Interfaz.leerFacturas(listaClientes)

    salir = input('\nDesea salir del sistema de facturación?(si/no): ')
