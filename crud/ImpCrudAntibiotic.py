from crud.ICrud import ICrud
from model.Antibiotic import Antibiotic


class ImpCrudAntibiotic(ICrud):
    def create(**kwargs):
        return Antibiotic(**kwargs)

