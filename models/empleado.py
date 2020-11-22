# CLASE EMPLEADO PARA LA ENTIDAD DE LA BASE DE DATOS

# DE NUESTRA CONFIGURACION DE LOGGER IMPORTAMOS LA DEFINICION
from services.logger_conf import logger

class Empleado:
    # CONSTRUCTOR DE LA CLASE
    def __init__(self, id_empleado=None, nombre_empleado=None, direccion_empleado=None, telefono_empleado=None):
        self.__id_empleado = id_empleado
        self.__nombre_empleado = nombre_empleado
        self.__direccion_empleado = direccion_empleado
        self.__telefono_empleado = telefono_empleado

    # METODO STR DE LA CLASE
    def __str__(self):
        result =  '{:03d}'.format(self.__id_empleado) + "   "
        result += '{:32.31}'.format(self.__nombre_empleado)
        result += '{:32.31}'.format(self.__direccion_empleado)
        result += '{:10}'.format(self.__telefono_empleado)
        
        return result
        
    # METODOS GET DE LA CLASE
    def getIdEmpleado(self):
        return self.__id_empleado

    def getNombreEmpleado(self):
        return self.__nombre_empleado
    
    def getDireccionEmpleado(self):
        return self.__direccion_empleado

    def getTelefonoEmpleado(self):
        return self.__telefono_empleado

    # METODOS SET DE LA CLASE
    def setIdEmpleado(self, id_empleado):
        self.__id_empleado = id_empleado

    def setNombreEmpleado(self, nombre_empleado):
        self.__nombre_empleado = nombre_empleado
    
    def setDireccionEmpleado(self, direccion_empleado):
        self.__direccion_empleado = direccion_empleado

    def setTelefonoEmpleado(self, telefono_empleado):
        self.__telefono_empleado = telefono_empleado

# SIMULACION (SOLO SE EJECUTARA CUANDO SE EJECUTE ESTE MODULO)
if __name__ == "__main__":
    empleado1 = Empleado(1, "Francisco Chamorro", "Puntasvergas 20", "3378509182")
    logger.debug(empleado1)
    empleado2 = Empleado(nombre_empleado="Antonio Magaña", direccion_empleado="Libertad 45")
    logger.debug(empleado2)
