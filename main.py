import random
from ui import interface
from datetime import datetime
from CRUD.ImpCrudClient import ImpCrudClient
from CRUD.ImpCrudAntibiotic import ImpCrudAntibiotic
from CRUD.ImpCrudControlPlague import ImpCrudControlPlague
from CRUD.ImpCrudControlFertilizer import ImpCrudControlFertilizer
from CRUD.ImpCrudInvoice import ImpCrudInvoice

if __name__ == '__main__':
    print(interface.welcome_message())

    invoices = list()
    leave = False

    while not leave:
        client_data = interface.read_client()
        client = ImpCrudClient.create(client_data)
        product_type = interface.read_product_type()
        product_data = None
        product = None
        if product_type == 'control de plagas':
            product_data = interface.read_product_control()
            product_data['waiting_period'] = interface.read_product_control_plague()
            product = ImpCrudControlPlague.create(product_data)
        elif product_type == 'fertilizante':
            product_data = interface.read_product_control()
            product_data['last_application'] = interface.read_product_control_fertilizer()
            product = ImpCrudControlFertilizer.create(product_data)
        elif product_type == 'antibiotico':
            product_data = interface.read_product_antibiotic()
            product = ImpCrudAntibiotic.create(product_data)

        invoice_data = {
            'number': str(random.randint(1, 1000)),
            'date': str(datetime.now().date()),
            'time': str(datetime.now().time()),
            'total_value': product.price
        }

        invoice = ImpCrudInvoice.create(invoice_data)
        invoice.associate_client(client)
        invoice.associate_product(product)

        interface.print_invoice(invoice)

        invoices.append(invoice)
        leave = input(interface.leave_message())
