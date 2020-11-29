# CLASE DESARROLLADORA PARA LA ENTIDAD DE LA BASE DE DATOS

from services.logger_conf import logger


class Desarrolladora:
    # METODO CONSTRUCTOR 
    def __init__(self, id_desarrolladora=None, nombre_desarrolladora="N/A", telefono_desarrolladora="N/A", direccion_desarrolladora="N/A"):
        self.__id_desarrolladora = id_desarrolladora
        self.__nombre_desarrolladora = nombre_desarrolladora
        self.__telefono_desarrolladora = telefono_desarrolladora
        self.__direccion_desarrolladora = direccion_desarrolladora

    # METODO TO_STRING 
    def __str__(self):
        return (f"{self.__id_desarrolladora:03d}" + "  "
                f"{self.__nombre_desarrolladora:24.23}"
                f"{self.__telefono_desarrolladora:15.10}"
                f"{self.__direccion_desarrolladora:21.30}")

    # METODOS GET DE LA CLASE
    def get_id_desarrolladora(self):
        return self.__id_desarrolladora

    def get_nombre_desarrolladora(self):
        return self.__nombre_desarrolladora

    def get_telefono_desarrolladora(self):
        return self.__telefono_desarrolladora

    def get_direccion_desarrolladora(self):
        return self.__direccion_desarrolladora

    # METODOS SET DE LA CLASE
    def set_id_desarrolladora(self, id_desarrolladora):
        self.__id_desarrolladora = id_desarrolladora

    def set_nombre_desarrolladora(self, nombre_desarrolladora):
        self.__nombre_desarrolladora = nombre_desarrolladora

    def set_telefono_desarrolladora(self, telefono_desarrolladora):
        self.__telefono_desarrolladora = telefono_desarrolladora

    def set_direccion_desarrolladora(self, direccion_desarrolladora):
        self.__direccion_desarrolladora = direccion_desarrolladora


# SIMULACION (SOLO SE EJECUTARA CUANDO SE EJECUTE ESTE MODULO)
if __name__ == "__main__":
    desarrolladora1 = Desarrolladora(1, "Sega", "9341156600", "Avenida Delproud #20")
    logger.debug(desarrolladora1)
    desarrolladora2 = Desarrolladora(nombre_desarrolladora="Dell Games", direccion_desarrolladora="Calle Oñacle #51")
    logger.debug(desarrolladora2)
