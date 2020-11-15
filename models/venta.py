from services.logger_conf import logger

class Venta:
    # CONSTRUCTOR
    def __init__(self, id_venta=None, fecha_venta=None, cantidad=None, subtotal=None, total=None, direccion_envio=None, codigo_videojuego=None, codigo_cliente=None):
        self.__id_venta = id_venta
        self.__fecha_venta = fecha_venta
        self.__cantidad = cantidad
        self.__subtotal = subtotal
        self.__total = total
        self.__direccion_envio = direccion_envio
        self.__codigo_videojuego = codigo_videojuego
        self.__codigo_cliente = codigo_cliente
    
    # TO_STRING
    def __str__(self):
        return (f"ID: {self.__id_venta}, "
                f"Fecha: {self.__fecha_venta}, "
                f"Cantidad: {self.__cantidad}, "
                f"Subtotal: {self.__subtotal}, "
                f"Total: {self.__total}, "
                f"Direccion a enviar: {self.__direccion_envio}, "
                f"ID del Videojuego: {self.__codigo_videojuego}, "
                f"ID del Cliente: {self.__codigo_cliente}")
    
    # METODOS GET
    def getIdVenta(self):
        return self.__id_venta
    
    def getFechaVenta(self):
        return self.__fecha_venta
    
    def getCantidad(self):
        return self.__cantidad
    
    def getSubtotal(self):
        return self.__subtotal
    
    def getTotal(self):
        return self.__total
    
    def getDireccionEnvio(self):
        return self.__direccion_envio
    
    def getCodigoVideojuego(self):
        return self.__codigo_videojuego
    
    def getCodigoCliente(self):
        return self.__codigo_cliente
    
    # METODOS SET
    def setIdVenta(self, id_venta):
        self.__id_venta = id_venta
    
    def setFechaVenta(self, fecha_venta):
        self.__fecha_venta = fecha_venta
    
    def setCantidad(self, cantidad):
        self.__cantidad = cantidad
    
    def setSubtotal(self, subtotal):
        self.__subtotal = subtotal
    
    def setTotal(self, total):
        self.__total = total
    
    def setDireccionEnvio(self, direccion_envio):
        self.__direccion_envio = direccion_envio
    
    def setCodigoVideojuego(self, codigo_videojuego):
        self.__codigo_videojuego = codigo_videojuego
    
    def setCodigoCliente(self, codigo_cliente):
        self.__codigo_cliente = codigo_cliente

if __name__ == "__main__":
    venta1 = Venta(1, "14/11/2020", 5, 100.00, 500.00, "Libertad #45", 1, 1)
    logger.debug(venta1)
    venta2 = Venta(fecha_venta="6/12/2019", total=1000.00)
    logger.debug(venta2)
    