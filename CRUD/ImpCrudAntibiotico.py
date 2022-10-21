from ICrud import ICrud
from model.Antibiotico import Antibiotico


class ImpCrudAntibiotico(ICrud):

    def crear(self):
        nombre = input('\tIngrese el nombre del antibiótico: ')
        tipoAnimal = input('\tIngrese el tipo del animal: ')
        dosis = input('\tIngrese la dosis: ')
        precio = float(input('\tIngrese el precio: '))
        return Antibiotico(nombre, tipoAnimal, dosis, precio)
