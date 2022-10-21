from ICrud import ICrud
from model.Invoice import Invoice


class ImpCrudInvoice(ICrud):
    def create(self, **kwargs):
        return Invoice(**kwargs)
