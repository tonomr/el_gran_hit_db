# CLASE EMPLEADO PARA LA ENTIDAD DE LA BASE DE DATOS

# DE NUESTRA CONFIGURACION DE LOGGER IMPORTAMOS LA DEFINICION
from services.logger_conf import logger

class Empleado:
    # METODO CONSTRUCTOR 
    def __init__(self, id_empleado=None, nombre_empleado="N/A", telefono_empleado="N/A", direccion_empleado="N/A"):
        self.__id_empleado = id_empleado
        self.__nombre_empleado = nombre_empleado
        self.__telefono_empleado = telefono_empleado
        self.__direccion_empleado = direccion_empleado

    # METODO TO_STRING
    def __str__(self):
        result =  '{:03d}'.format(self.__id_empleado) + "   "
        result += '{:32.31}'.format(self.__nombre_empleado)
        result += '{:32.31}'.format(self.__direccion_empleado)
        result += '{:10}'.format(self.__telefono_empleado)
        
        return result
        
    # METODOS GET DE LA CLASE
    def get_id_empleado(self):
        return self.__id_empleado

    def get_nombre_empleado(self):
        return self.__nombre_empleado

    def get_telefono_empleado(self):
        return self.__telefono_empleado

    def get_direccion_empleado(self):
        return self.__direccion_empleado

    # METODOS SET DE LA CLASE
    def set_id_empleado(self, id_empleado):
        self.__id_empleado = id_empleado

    def set_nombre_empleado(self, nombre_empleado):
        self.__nombre_empleado = nombre_empleado

    def set_telefono_empleado(self, telefono_empleado):
        self.__telefono_empleado = telefono_empleado

    def set_direccion_empleado(self, direccion_empleado):
        self.__direccion_empleado = direccion_empleado

# SIMULACION (SOLO SE EJECUTARA CUANDO SE EJECUTE ESTE MODULO)
if __name__ == "__main__":
    empleado1 = Empleado(1, "Francisco Chamorro", "3378509182", "Calle Ocre #20")
    logger.debug(empleado1)
    empleado2 = Empleado(nombre_empleado="Antonio Magaña", direccion_empleado="Calle Libertad #45")
    logger.debug(empleado2)
