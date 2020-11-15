from services.logger_conf import logger

class Compra:
    # CONSTRUCTOR
    def __init__(self, id_compra=None, estado_compra=None, fecha_compra=None, precio_compra=None, codigo_videojuego=None, codigo_empleado=None):
        self.__id_compra = id_compra
        self.__estado_compra = estado_compra
        self.__fecha_compra = fecha_compra
        self.__precio_compra = precio_compra
        self.__codigo_videojuego = codigo_videojuego
        self.__codigo_empleado = codigo_empleado
    
    # TO_STRING
    def __str__(self):
        return (f"ID: {self.__id_compra}, "
                f"Estado: {self.__estado_compra}, "
                f"Fecha de la compra: {self.__fecha_compra}, "
                f"Precio final: {self.__precio_compra}, "
                f"Nombre del videojuego: {self.__codigo_videojuego}, "
                f"Nombre del empleado: {self.__codigo_empleado}")
    
    # METODOS GET
    def getIdCompra(self):
        return self.__id_compra
    
    def getEstadoCompra(self):
        return self.__estado_compra
    
    def getFechaCompra(self):
        return self.__fecha_compra
    
    def getPrecioCompra(self):
        return self.__precio_compra
    
    def getCodigoVideojuego(self):
        return self.__codigo_videojuego
    
    def getCodigoEmpleado(self):
        return self.__codigo_empleado
    
    # METODOS SET
    def setIdCompra(self, id_compra):
        self.__id_compra = id_compra
    
    def setEstadoCompra(self, estado_compra):
        self.__estado_compra = estado_compra
    
    def setFechaCompra(self, fecha_compra):
        self.__fecha_compra = fecha_compra
    
    def setPrecioCompra(self, precio_compra):
        self.__precio_compra = precio_compra
    
    def setCodigoVideojuego(self, codigo_videojuego):
        self.__codigo_videojuego = codigo_videojuego
    
    def setCodigoEmpleado(self, codigo_empleado):
        self.__codigo_empleado = codigo_empleado
    
if __name__ == "__main__":
    compra1 = Compra(2, "Nuevo", "14/11/2020", 500.00, 1, 1)
    logger.debug(compra1)
    compra2 = Compra(estado_compra="Usado", precio_compra=250.00)
    logger.debug(compra2)
