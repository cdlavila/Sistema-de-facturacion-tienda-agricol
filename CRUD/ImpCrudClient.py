from ICrud import ICrud
from model.Client import Client


class ImpCrudClient(ICrud):
    def create(self, **kwargs):
        return Client(**kwargs)
