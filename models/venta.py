from services.logger_conf import logger

class Venta:
    # METODO CONSTRUCTOR
    def __init__(self, id_venta=None, fecha_venta="N/A", cantidad_venta=0, subtotal_venta=0.0, total_venta=0.0, direccion_envio="N/A", codigo_videojuego=None, codigo_cliente=None):
        self.__id_venta = id_venta
        self.__fecha_venta = fecha_venta
        self.__cantidad_venta = cantidad_venta
        self.__subtotal_venta = subtotal_venta
        self.__total_venta = total_venta
        self.__direccion_envio = direccion_envio
        self.__codigo_videojuego = codigo_videojuego
        self.__codigo_cliente = codigo_cliente
    
    # METODO TO_STRING
    def __str__(self):                
        return (f"{self.__id_venta:03d}" + "   "
                f"{self.__fecha_venta}" + "   "
                f"{self.__cantidad_venta:02d}" + "   "
                f"{self.__subtotal_venta:06.2f}" + "   "
                f"{self.__total_venta:06.2f}" + "   "
                f"{self.__direccion_envio:24.23}"
                f"{self.__codigo_videojuego:03d}" + "       "
                f"{self.__codigo_cliente:03d}")
    
    # METODOS GETTERS
    def get_id_venta(self):
        return self.__id_venta
    
    def get_fecha_venta(self):
        return self.__fecha_venta
    
    def get_cantidad_venta(self):
        return self.__cantidad_venta
    
    def get_subtotal_venta(self):
        return self.__subtotal_venta
    
    def get_total_venta(self):
        return self.__total_venta
    
    def get_direccion_envio(self):
        return self.__direccion_envio
    
    def get_codigo_videojuego(self):
        return self.__codigo_videojuego
    
    def get_codigo_cliente(self):
        return self.__codigo_cliente

    # METODOS SETTERS
    def set_id_venta(self, id_venta):
        self.__id_venta = id_venta

    def set_fecha_venta(self, fecha_venta):
        self.__fecha_venta = fecha_venta

    def set_cantidad_venta(self, cantidad_venta):
        self.__cantidad_venta = cantidad_venta

    def set_subtotal_venta(self, subtotal_venta):
        self.__subtotal_venta = subtotal_venta

    def set_total_venta(self, total_venta):
        self.__total_venta = total_venta

    def set_direccion_envio(self, direccion_envio):
        self.__direccion_envio = direccion_envio

    def set_codigo_videojuego(self, codigo_videojuego):
        self.__codigo_videojuego = codigo_videojuego

    def set_codigo_cliente(self, codigo_cliente):
        self.__codigo_cliente = codigo_cliente

if __name__ == "__main__":
    venta1 = Venta(1, "14/11/2020", 5, 100.00, 500.00, "Libertad #45", 1, 1)
    logger.debug(venta1)
    venta2 = Venta(fecha_venta="6/12/2019", total_venta=1000.00)
    logger.debug(venta2)
