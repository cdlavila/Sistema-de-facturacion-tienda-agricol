class Antibiotico:
    def __init__(self, nombre, tipoAnimal, dosis, precio):
        self.__nombre = nombre
        self.__tipoAnimal = tipoAnimal
        self.__dosis = dosis
        self.__precio = precio

    @property
    def nombre(self):
        return self.__nombre

    @property
    def tipoAnimal(self):
        return self.__tipoAnimal

    @property
    def dosis(self):
        return self.__dosis

    @property
    def precio(self):
        return self.__precio
