class Cliente:
    def __init__(self, nombre, cedula):
        self.__nombre = nombre
        self.__cedula = cedula
        self.__facturas = list()

    @property
    def nombre(self):
        return self.__nombre

    @property
    def cedula(self):
        return self.__cedula

    @property
    def facturas(self):
        return self.__facturas

    def asociar(self, factura):
        self.facturas.append(factura)

    def mostrarCliente(self):
        print(f'Nombre: {self.nombre}')
        print(f'Cédula: {self.cedula}')
