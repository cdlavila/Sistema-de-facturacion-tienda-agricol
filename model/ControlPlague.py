from model.ControlProduct import ControlProduct


class ControlPlague(ControlProduct):
    def __init__(self, name, ica_registration, application_frequency, price, waiting_period):
        super().__init__(name, ica_registration, application_frequency, price)
        self.__waiting_period = waiting_period

    @property
    def waiting_period(self):
        return self.__waiting_period
