from CRUD.ICrud import ICrud
from model.Client import Client


class ImpCrudClient(ICrud):
    def create(**kwargs):
        return Client(**kwargs)
