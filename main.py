import random
from ui import interface
from datetime import datetime
from crud.ImpCrudClient import ImpCrudClient
from crud.ImpCrudAntibiotic import ImpCrudAntibiotic
from crud.ImpCrudControlPlague import ImpCrudControlPlague
from crud.ImpCrudControlFertilizer import ImpCrudControlFertilizer
from crud.ImpCrudInvoice import ImpCrudInvoice

if __name__ == '__main__':
    print(interface.welcome_message())

    invoices = list()
    leave = False

    while not leave:
        client_data = interface.read_client()
        client = ImpCrudClient.create(name=client_data['name'], cc=client_data['cc'])
        product_type = interface.read_product_type()
        product_data = None
        product = None
        if product_type == 'control de plagas':
            product_data = interface.read_product_control()
            product_data['waiting_period'] = interface.read_product_control_plague()
            product = ImpCrudControlPlague.create(name=product_data['name'],
                                                  ica_registration=product_data['ica_registration'],
                                                  application_frequency=product_data['application_frequency'],
                                                  price=product_data['price'],
                                                  waiting_period=product_data['waiting_period'])
        elif product_type == 'fertilizante':
            product_data = interface.read_product_control()
            product_data['last_application'] = interface.read_product_control_fertilizer()
            product = ImpCrudControlFertilizer.create(name=product_data['name'],
                                                      ica_registration=product_data['ica_registration'],
                                                      application_frequency=product_data['application_frequency'],
                                                      price=product_data['price'],
                                                      last_application=product_data['last_application'])
        elif product_type == 'antibiotico':
            product_data = interface.read_product_antibiotic()
            product = ImpCrudAntibiotic.create(name=product_data['name'],
                                               animal_type=product_data['animal_type'],
                                               dose=product_data['dose'],
                                               price=product_data['price'])

        invoice_data = {
            'number': str(random.randint(1, 1000)),
            'date': str(datetime.now().date()),
            'time': str(datetime.now().time()),
            'total_value': product.price
        }

        invoice = ImpCrudInvoice.create(number=invoice_data['number'], date=invoice_data['date'],
                                        time=invoice_data['time'])
        invoice.associate_client(client)
        invoice.associate_product(product)

        interface.print_invoice(invoice)

        invoices.append(invoice)
        leave = input(interface.leave_message())
