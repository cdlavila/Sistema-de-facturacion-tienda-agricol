class Client:
    def __init__(self, name, cc):
        self.__name = name
        self.__cc = cc

    @property
    def name(self):
        return self.__name

    @property
    def cc(self):
        return self.__cc

    def print(self):
        print(f'Nombre: {self.name}')
        print(f'Cédula: {self.cc}')
