# CLASE CLIENTE PARA LA ENTIDAD DE LA BASE DE DATOS

# DE NUESTRA CONFIGURACION DE LOGGER IMPORTAMOS LA DEFINICION
from services.logger_conf import logger

class Cliente:
    # CONSTRUCTOR DE LA CLASE
    def __init__(self, id_cliente=None, nombre_cliente=None, email=None, direccion_cliente=None, telefono_cliente=None):
        self.__id_cliente = id_cliente
        self.__nombre_cliente = nombre_cliente
        self.__email = email
        self.__direccion_cliente = direccion_cliente
        self.__telefono_cliente = telefono_cliente

    # METODO STR DE LA CLASE
    def __str__(self):
        result =  '{:03d}'.format(self.__id_cliente) + "   "
        result += '{:25.24}'.format(self.__nombre_cliente)
        result += '{:22.21}'.format(self.__email)
        result += '{:20.19}'.format(self.__direccion_cliente)
        result += '{:10}'.format(self.__telefono_cliente)
        return result

    # METODOS GET DE LA CLASE
    def getIdCliente(self):
        return self.__id_cliente

    def getNombreCliente(self):
        return self.__nombre_cliente
    
    def getEmail(self):
        return self.__email
    
    def getDireccionCliente(self):
        return self.__direccion_cliente

    def getTelefonoCliente(self):
        return self.__telefono_cliente

    # METODOS SET DE LA CLASE
    def setIdCliente(self, id_cliente):
        self.__id_cliente = id_cliente

    def setNombreCliente(self, nombre_cliente):
        self.__nombre_cliente = nombre_cliente
    
    def setEmail(self, email):
        self.__email = email
    
    def setDireccionCliente(self, direccion_cliente):
        self.__direccion_cliente = direccion_cliente

    def setTelefonoCliente(self, telefono_cliente):
        self.__telefono_cliente = telefono_cliente

# SIMULACION (SOLO SE EJECUTARA CUANDO SE EJECUTE ESTE MODULO)
if __name__ == "__main__":
    cliente1 = Cliente(1, "Francisco Chamorro", "chamorro_paco@mail.com", "Puntasvergas 20", "3378509182")
    logger.debug(cliente1)
    cliente2 = Cliente(nombre_cliente="Antonio Magaña", direccion_cliente="Libertad 45")
    logger.debug(cliente2)
