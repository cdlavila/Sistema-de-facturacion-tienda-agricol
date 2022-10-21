from ICrud import ICrud
from model.ControlFertilizer import ControlFertilizer


class ImpCrudControlFertilizer(ICrud):
    def create(self, **kwargs):
        return ControlFertilizer(**kwargs)
