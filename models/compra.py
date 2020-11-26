from services.logger_conf import logger
from controllers.videojuego_dao import VideojuegoDao
from controllers.empleado_dao import EmpleadoDao


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
        return (f"{self.__id_compra:03d}" + "  "
                f"{self.__codigo_videojuego:25.24}"
                f"{self.__estado_compra:11}"
                f"{self.__codigo_empleado:24.23}"
                f"{self.__fecha_compra}  " 
                f"{self.__precio_compra:06.2f}")
    
    # To String
    def to_str(self):
        game_name = VideojuegoDao.buscar_nombre([self.__codigo_videojuego])
        employee_name = EmpleadoDao.buscar_nombre([self.__codigo_empleado])
        return (f" {self.__id_compra:03d}" + "  "
                f"{game_name[0]:25.24}"
                f"{self.__estado_compra:11}"
                f"{employee_name[0]:24.23}"
                f"{self.__fecha_compra}  "
                f"{self.__precio_compra:06.2f}")
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
