from CRUD.ICrud import ICrud
from model.Invoice import Invoice


class ImpCrudInvoice(ICrud):
    def create(**kwargs):
        return Invoice(**kwargs)
