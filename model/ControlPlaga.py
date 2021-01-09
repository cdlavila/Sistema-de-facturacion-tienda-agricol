from model import ProductoControl as pc


class ControlPlaga(pc.ProductoControl):
    def __init__(self, nombre, registroICA, frecuenciaAplicacion, precio, periodoCarencia):
        super().__init__(nombre, registroICA, frecuenciaAplicacion, precio)
        self.__periodoCarencia = periodoCarencia

    @property
    def periodoCarencia(self):
        return self.__periodoCarencia
