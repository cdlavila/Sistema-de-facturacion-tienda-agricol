class ProductoControl:
    def __init__(self, nombre, registroICA, frecuenciaAplicacion, precio):
        self.__nombre = nombre
        self.__registroICA = registroICA
        self.__frecuenciaAplicacion = frecuenciaAplicacion
        self.__precio = precio

    @property
    def nombre(self):
        return self.__nombre

    @property
    def registroICA(self):
        return self.__registroICA

    @property
    def frecuenciaAplicacion(self):
        return self.__frecuenciaAplicacion

    @property
    def precio(self):
        return self.__precio
