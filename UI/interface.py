def welcome_message():
    return """
----------------------------------------------------------
BIENVENIDO AL SISTEMA DE FACTURACIÓN DE LA TIENDA AGRÍCOLA
----------------------------------------------------------
"""


def leave_message():
    return '\nDesea salir del sistema de facturación?(si/no): '


def new_invoice_message():
    return '\nNUEVA FACTURA'


def read_client():
    client_name = input('Ingrese el nombre del cliente: ')
    client_cc = input('Ingrese la cédula del cliente: ')
    return {'name': client_name, 'cc': client_cc}


def read_product_type():
    print('\nAñada un producto a su compra (antibiotico, control de plagas o fertilizante)')
    product_type = input('\tIngrese el tipo del producto: ')
    return product_type


def read_product_control():
    product_name = input('\tIngrese el nombre del producto: ')
    ica_registration = input('\tIngrese el registro ICA del producto: ')
    application_frequency = input('\tIngrese la frecuencia de aplicación del producto: ')
    product_price = float(input('\tIngrese el precio del producto: '))
    return {
        'name': product_name,
        'ica_registration': ica_registration,
        'application_frequency': application_frequency,
        'price': product_price
    }


def read_product_control_plague():
    waiting_period = input('\tIngrese el periodo de carencia: ')
    return waiting_period


def read_product_control_fertilizer():
    last_application = input('\tIngrese la fecha de la última aplicación: ')
    return last_application


def read_product_antibiotic():
    product_name = input('\tIngrese el nombre del producto: ')
    animal_type = input('\tIngrese el tipo de animal: ')
    product_dose = input('\tIngrese la dosis: ')
    product_price = float(input('\tIngrese el precio del producto: '))
    return {
        'name': product_name,
        'animal_type': animal_type,
        'dose': product_dose,
        'price': product_price
    }


def print_invoice(invoice):
    amount_received = float(input('\nIngrese el valor recibido: '))
    print('\n________________________________________________')
    print('TIENDA AGRÍCOLA')
    print('________________________________________________')
    invoice.print()
    invoice.client.print()
    invoice.print_products()
    print(f'Recibido: {amount_received}')
    print(f'Cambio: {amount_received - invoice.total_value}')
    print('GRACIAS POR SU COMPRA')
    print('VUELVA PRONTO')
    print('________________________________________________')
