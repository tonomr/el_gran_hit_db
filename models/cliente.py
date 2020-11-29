# CLASE CLIENTE PARA LA ENTIDAD DE LA BASE DE DATOS

from services.logger_conf import logger


class Cliente:
    # METODO CONSTRUCTOR 
    def __init__(self, id_cliente=None, nombre_cliente="N/A", email_cliente="N/A", telefono_cliente="N/A", direccion_cliente="N/A"):
        self.__id_cliente = id_cliente
        self.__nombre_cliente = nombre_cliente
        self.__email_cliente = email_cliente
        self.__telefono_cliente = telefono_cliente
        self.__direccion_cliente = direccion_cliente

    # METODO TO_STRING
    def __str__(self):
        result =  '{:03d}'.format(self.__id_cliente) + "   "
        result += '{:25.24}'.format(self.__nombre_cliente)
        result += '{:22.21}'.format(self.__email_cliente)
        result += '{:20.19}'.format(self.__direccion_cliente)
        result += '{:10}'.format(self.__telefono_cliente)
        return result

    # METODOS GETTERS
    def get_id_cliente(self):
        return self.__id_cliente

    def get_nombre_cliente(self):
        return self.__nombre_cliente
    
    def get_email_cliente(self):
        return self.__email_cliente
    
    def get_telefono_cliente(self):
        return self.__telefono_cliente
    
    def get_direccion_cliente(self):
        return self.__direccion_cliente

    # METODOS SETTERS
    def set_id_cliente(self, id_cliente):
        self.__id_cliente = id_cliente

    def set_nombre_cliente(self, nombre_cliente):
        self.__nombre_cliente = nombre_cliente
    
    def set_email_cliente(self, email_cliente):
        self.__email_cliente = email_cliente
    
    def set_telefono_cliente(self, telefono_cliente):
        self.__telefono_cliente = telefono_cliente
    
    def set_direccion_cliente(self, direccion_cliente):
        self.__direccion_cliente = direccion_cliente


# SIMULACION (SOLO SE EJECUTARA CUANDO SE EJECUTE ESTE MODULO)
if __name__ == "__main__":
    cliente1 = Cliente(1, "Francisco Chamorro", "chamorro_paco@mail.com", "3378509182", "Calle Ocre #20")
    logger.debug(cliente1)
    cliente2 = Cliente(nombre_cliente="Antonio Magaña", direccion_cliente="Calle Libertad #45")
    logger.debug(cliente2)
