from model import Antibiotico as a
from model import ProductoControl as pc


class Factura:
    def __init__(self, numeroFactura, fecha, hora):
        self.__numeroFactura = numeroFactura
        self.__fecha = fecha
        self.__hora = hora
        self.__antibioticos = list()
        self.__productosControl = list()
        self.__valorTotalCompra = 0

    @property
    def numeroFactura(self):
        return self.__numeroFactura

    @property
    def fecha(self):
        return self.__fecha

    @property
    def hora(self):
        return self.__hora

    @property
    def antibioticos(self):
        return self.__antibioticos

    @property
    def productosControl(self):
        return self.__productosControl

    @property
    def valorTotalCompra(self):
        return self.__valorTotalCompra

    def asociar(self, producto):
        if isinstance(producto, a.Antibiotico):
            self.__antibioticos.append(producto)
            self.__valorTotalCompra += producto.precio
        elif isinstance(producto, pc.ProductoControl):
            self.__productosControl.append(producto)
            self.__valorTotalCompra += producto.precio
        else:
            print('Error')

    def mostrarProductos(self):
        productos = self.__antibioticos + self.__productosControl
        numeroProducto = 1
        print('Productos comprados:')
        for prod in productos:
            print(f'\tProducto No.{numeroProducto}: {prod.nombre}, precio: {prod.precio}')
            numeroProducto += 1
        print(f'Valor total de la Compra: {self.valorTotalCompra}')

    def mostrarDatos(self):
        print(f'Factura No. {self.numeroFactura}')
        print(f'Fecha: {self.fecha}')
        print(f'Hora: {self.hora}')
