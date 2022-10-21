class ControlProduct:
    def __init__(self, name, ica_registration, application_frequency, price):
        self.__name = name
        self.__ica_registration = ica_registration
        self.__application_frequency = application_frequency
        self.__price = price

    @property
    def name(self):
        return self.__name

    @property
    def ica_registration(self):
        return self.__ica_registration

    @property
    def application_frequency(self):
        return self.__application_frequency

    @property
    def price(self):
        return self.__price
