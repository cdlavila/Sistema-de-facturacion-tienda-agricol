from crud.ICrud import ICrud
from model.ControlFertilizer import ControlFertilizer


class ImpCrudControlFertilizer(ICrud):
    def create(**kwargs):
        return ControlFertilizer(**kwargs)
