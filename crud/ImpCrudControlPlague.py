from crud.ICrud import ICrud
from model.ControlPlague import ControlPlague


class ImpCrudControlPlague(ICrud):
    def create(**kwargs):
        return ControlPlague(**kwargs)
