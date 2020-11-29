# CLASE VIDEOJUEGO PARA LA ENTIDAD DE LA BASE DE DATOS

from services.logger_conf import logger
from controllers.desarrolladora_dao import DesarrolladoraDao


class Videojuego:
    # METODO CONSTRUCTOR
    def __init__(self, id_videojuego=None, nombre_videojuego="N/A", estado_videojuego="N/A", cantidad_videojuego=1, clasificacion_videojuego="N/A", descripcion_videojuego="N/A", precio_videojuego=0.0, publicacion_videojuego="24/11/2020", codigo_desarrolladora=None):
        self.__id_videojuego = id_videojuego
        self.__nombre_videojuego = nombre_videojuego
        self.__estado_videojuego = estado_videojuego
        self.__cantidad_videojuego = cantidad_videojuego
        self.__clasificacion_videojuego = clasificacion_videojuego
        self.__descripcion_videojuego = descripcion_videojuego
        self.__precio_videojuego = precio_videojuego
        self.__publicacion_videojuego = publicacion_videojuego
        self.__codigo_desarrolladora = codigo_desarrolladora

    # METODO TO_STRING
    def __str__(self):
        nombre_desarrolladora = DesarrolladoraDao.buscarNombre(self.__codigo_desarrolladora)
        result = " " + '{:03d}'.format(self.__id_videojuego) + "   "
        result += '{:32.30}'.format(self.__nombre_videojuego)
        result += '{:12}'.format(self.__estado_videojuego)
        result += '{:03d}'.format(self.__cantidad_videojuego) + "   "
        result += '{:6}'.format(self.__clasificacion_videojuego)
        result += '{:06.2f}'.format(self.__precio_videojuego) + "   "
        result += '{:16}'.format(nombre_desarrolladora)

        return result
        
    # METODOS GET DE LA CLASE
    def get_id_videojuego(self):
        return self.__id_videojuego

    def get_nombre_videojuego(self):
        return self.__nombre_videojuego

    def get_estado_videojuego(self):
        return self.__estado_videojuego

    def get_cantidad_videojuego(self):
        return self.__cantidad_videojuego

    def get_clasificacion_videojuego(self):
        return self.__clasificacion_videojuego

    def get_descripcion_videojuego(self):
        return self.__descripcion_videojuego

    def get_precio_videojuego(self):
        return self.__precio_videojuego

    def get_publicacion_videojuego(self):
        return self.__publicacion_videojuego

    def get_codigo_desarrolladora(self):
        return self.__codigo_desarrolladora

    # METODOS SET DE LA CLASE
    def set_id_videojuego(self, id_videojuego):
        self.__id_videojuego = id_videojuego

    def set_nombre_videojuego(self, nombre_videojuego):
        self.__nombre_videojuego = nombre_videojuego

    def set_estado_videojuego(self, estado_videojuego):
        self.__estado_videojuego = estado_videojuego

    def set_cantidad_videojuego(self, cantidad_videojuego):
        self.__cantidad_videojuego = cantidad_videojuego

    def set_clasificacion_videojuego(self, clasificacion_videojuego):
        self.__clasificacion_videojuego = clasificacion_videojuego

    def set_descripcion_videojuego(self, descripcion_videojuego):
        self.__descripcion_videojuego = descripcion_videojuego

    def set_precio_videojuego(self, precio_videojuego):
        self.__precio_videojuego = precio_videojuego

    def set_publicacion_videojuego(self, publicacion_videojuego):
        self.__publicacion_videojuego = publicacion_videojuego

    def set_codigo_desarrolladora(self, codigo_desarrolladora):
        self.__codigo_desarrolladora = codigo_desarrolladora


# SIMULACION (SOLO SE EJECUTARA CUANDO SE EJECUTE ESTE MODULO)
if __name__ == "__main__":
    videojuego1 = Videojuego(2, "Bioshock", "Nuevo", 100, "M", "Juego de disparos en primera persona submarino.", 499.99, "9/4/2008", 1)
    logger.debug(videojuego1)
    videojuego2 = Videojuego(nombre_videojuego="Age of Empires", codigo_desarrolladora=1)
    logger.debug(videojuego2)
