from model.ControlProduct import ControlProduct


class ControlFertilizer(ControlProduct):
    def __init__(self, name, ica_registration, application_frequency, price, last_application):
        super().__init__(name, ica_registration, application_frequency, price)
        self.__last_application = last_application

    @property
    def last_application(self):
        return self.__last_application
