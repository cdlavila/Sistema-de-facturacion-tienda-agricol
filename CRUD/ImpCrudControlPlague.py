from ICrud import ICrud
from model.ControlPlague import ControlPlague


class ImpCrudControlPlague(ICrud):
    def create(self, **kwargs):
        return ControlPlague(**kwargs)
