# CLASE VIDEOJUEGO PARA LA ENTIDAD DE LA BASE DE DATOS

# DE NUESTRA CONFIGURACION DE LOGGER IMPORTAMOS LA DEFINICION
from services.logger_conf import logger
from controllers.desarrolladora_dao import DesarrolladoraDao


class Videojuego:
    # CONSTRUCTOR DE LA CLASE
    def __init__(self, id_juego=None, nombre_juego=None, estado=None, cantidad=None, clasificacion=None, descripcion=None, precio=None, fecha_publicacion=None, codigo_desarrolladora=None):
        self.__id_juego = id_juego
        self.__nombre_juego = nombre_juego
        self.__estado = estado
        self.__cantidad = cantidad
        self.__clasificacion = clasificacion
        self.__descripcion = descripcion
        self.__precio = precio
        self.__fecha_publicacion = fecha_publicacion
        self.__codigo_desarrolladora = codigo_desarrolladora

    # METODO STR DE LA CLASE
    def __str__(self):
        nombre_desarrolladora = DesarrolladoraDao.buscarNombre(self.__codigo_desarrolladora)
        return (f"ID: {self.__id_juego}, "
                f"Nombre: {self.__nombre_juego}, "
                f"Estado: {self.__estado}, "
                f"Cantidad: {self.__cantidad}, "
                f"Clasificacion: {self.__clasificacion}, "
                f"Descripcion: {self.__descripcion}, "
                f"Precio: {self.__precio}, "
                f"Fecha de publicacion: {self.__fecha_publicacion}, "
                f"Nombre de la desarrolladora: {nombre_desarrolladora}")

    # METODOS GET DE LA CLASE
    def getIdJuego(self):
        return self.__id_juego

    def getNombreJuego(self):
        return self.__nombre_juego

    def getEstado(self):
        return self.__estado

    def getCantidad(self):
        return self.__cantidad

    def getClasificacion(self):
        return self.__clasificacion

    def getDescripcion(self):
        return self.__descripcion

    def getPrecio(self):
        return self.__precio

    def getFechaPublicacion(self):
        return self.__fecha_publicacion

    def getCodigoDesarrolladora(self):
        return self.__codigo_desarrolladora

    # METODOS SET DE LA CLASE
    def setIdJuego(self, id_juego):
        self.__id_juego = id_juego

    def setNombreJuego(self, nombre_juego):
        self.__nombre_juego = nombre_juego

    def setEstado(self, estado):
        self.__estado = estado

    def setCantidad(self, cantidad):
        self.__cantidad = cantidad

    def setClasificacion(self, clasificacion):
        self.__clasificacion = clasificacion

    def setDescripcion(self, descripcion):
        self.__descripcion = descripcion

    def setPrecio(self, precio):
        self.__precio = precio

    def setFechaPublicacion(self, fecha_publicacion):
        self.__fecha_publicacion = fecha_publicacion

    def setCodigoDesarrolladora(self, codigo_desarrolladora):
        self.__codigo_desarrolladora = codigo_desarrolladora


# SIMULACION (SOLO SE EJECUTARA CUANDO SE EJECUTE ESTE MODULO)
if __name__ == "__main__":
    videojuego1 = Videojuego(2, "Bioshock", "Nuevo", 100, "M",
                             "Juego de disparos en primera persona submarino.", 499.99, "9/4/2008", 1)
    logger.debug(videojuego1)
    videojuego2 = Videojuego(
        nombre_juego="Age of Empires", codigo_desarrolladora=1)
    logger.debug(videojuego2)
