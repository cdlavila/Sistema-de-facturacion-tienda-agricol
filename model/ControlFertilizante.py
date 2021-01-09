from model import ProductoControl as pc


class ControlFertilizante(pc.ProductoControl):
    def __init__(self, nombre, registroICA, frecuenciaAplicacion, precio, ultimaAplicacion):
        super().__init__(nombre, registroICA, frecuenciaAplicacion, precio)
        self.__ultimaAplicacion = ultimaAplicacion

    @property
    def ultimaAplicacion(self):
        return self.__ultimaAplicacion
