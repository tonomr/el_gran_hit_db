# CLASE DESARROLLADORA PARA LA ENTIDAD DE LA BASE DE DATOS

# DE NUESTRA CONFIGURACION DE LOGGER IMPORTAMOS LA DEFINICION
from services.logger_conf import logger


class Desarrolladora:
    # CONSTRUCTOR DE LA CLASE
    def __init__(self, id_desarrolladora=None, nombre_desarrolladora=None, telefono_desarrolladora=None, direccion_desarrolladora=None):
        self.__id_desarrolladora = id_desarrolladora
        self.__nombre_desarrolladora = nombre_desarrolladora
        self.__telefono_desarrolladora = telefono_desarrolladora
        self.__direccion_desarrolladora = direccion_desarrolladora

    # METODO STR DE LA CLASE
    def __str__(self):
        return (f"ID: {self.__id_desarrolladora}, "
                f"Nombre: {self.__nombre_desarrolladora}, "
                f"Telefono: {self.__telefono_desarrolladora}, "
                f"Direccion: {self.__direccion_desarrolladora}")

    # METODOS GET DE LA CLASE
    def getIdDesarrolladora(self):
        return self.__id_desarrolladora

    def getNombreDesarrolladora(self):
        return self.__nombre_desarrolladora

    def getTelefonoDesarrolladora(self):
        return self.__telefono_desarrolladora

    def getDireccionDesarrolladora(self):
        return self.__direccion_desarrolladora

    # METODOS SET DE LA CLASE
    def setIdDesarrolladora(self, id_desarrolladora):
        self.__id_desarrolladora = id_desarrolladora

    def setNombreDesarrolladora(self, nombre_desarrolladora):
        self.__nombre_desarrolladora = nombre_desarrolladora

    def setTelefonoDesarrolladora(self, telefono_desarrolladora):
        self.__telefono_desarrolladora = telefono_desarrolladora

    def setDesarrolladora(self, id_desarrolladora):
        self.__id_desarrolladora = id_desarrolladora


# SIMULACION (SOLO SE EJECUTARA CUANDO SE EJECUTE ESTE MODULO)
if __name__ == "__main__":
    desarrolladora1 = Desarrolladora(
        1, "Sega", "9341156600", "544 Puntasvergas")
    logger.debug(desarrolladora1)
    desarrolladora2 = Desarrolladora(
        nombre_desarrolladora="Dell Games", direccion_desarrolladora="544 PuebloMagico")
    logger.debug(desarrolladora2)
