from model.Antibiotic import Antibiotic
from model.ControlProduct import ControlProduct


class Invoice:
    def __init__(self, number, date, time):
        self.__number = number
        self.__date = date
        self.__time = time
        self.__antibiotics = list()
        self.__control_products = list()
        self.__client = None
        self.__total_value = 0

    @property
    def number(self):
        return self.__number

    @property
    def date(self):
        return self.__date

    @property
    def time(self):
        return self.__time

    @property
    def antibiotics(self):
        return self.__antibiotics

    @property
    def control_products(self):
        return self.__control_products

    @property
    def client(self):
        return self.__client

    @property
    def total_value(self):
        return self.__total_value

    def associate_product(self, product):
        if isinstance(product, Antibiotic):
            self.__antibiotics.append(product)
            self.__total_value += product.price
        elif isinstance(product, ControlProduct):
            self.__control_products.append(product)
            self.__total_value += product.price
        else:
            print('Error')

    def associate_client(self, client):
        self.__client = client

    def print_products(self):
        products = self.__antibiotics + self.__control_products
        product_number = 1
        print('Productos comprados:')
        for product in products:
            print(f'\tProducto No.{product_number}: {product.name}, precio: {product.precio}')
            product_number += 1
        print(f'Valor total de la Compra: {self.total_value}')

    def print(self):
        print(f'Factura No. {self.number}')
        print(f'Fecha: {self.date}')
        print(f'Hora: {self.time}')
