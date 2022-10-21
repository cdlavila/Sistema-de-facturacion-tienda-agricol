from ICrud import ICrud
from model.Antibiotic import Antibiotic


class ImpCrudAntibiotic(ICrud):
    def create(self, **kwargs):
        return Antibiotic(**kwargs)

