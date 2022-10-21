class Antibiotic:
    def __init__(self, name, animal_type, dose, price):
        self.__name = name
        self.__animal_type = animal_type
        self.__dose = dose
        self.__price = price

    @property
    def name(self):
        return self.__name

    @property
    def animal_type(self):
        return self.__animal_type

    @property
    def dose(self):
        return self.__dose

    @property
    def price(self):
        return self.__price
