from models.venta import Venta
from models.cliente import Cliente
from services.cursor import CursorDelPool
from services.logger_conf import logger

class VentaDao:
    # SENTENCIAS SQL
    __SELECT = "SELECT * FROM venta"
    __INSERT = "INSERT INTO venta(fecha_venta, cantidad, subtotal, total, direccion_envio, codigo_videojuego, codigo_cliente) VALUES(%s, %s, %s, %s, %s, %s, %s)"
    __UPDATE = "UPDATE venta SET fecha_venta = %s, cantidad = %s, subtotal = %s, total = %s, direccion_envio = %s, codigo_videojuego = %s, codigo_cliente = %s WHERE id_venta = %s"
    __DELETE = "DELETE FROM venta WHERE id_venta = %s"
    __SEARCH_CLIENTE = "SELECT * FROM cliente WHERE nombre_cliente LIKE %s"
    __SEARCH = "SELECT * FROM venta WHERE CAST(codigo_cliente AS VARCHAR) LIKE CAST(%s AS VARCHAR)"
    __SELECT_ONE =  "SELECT * FROM venta WHERE id_venta = %s"
        
    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__SELECT))
            cursor.execute(cls.__SELECT)
            registros = cursor.fetchall()
            
            ventas = []
            for registro in registros:
                venta = Venta(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5], registro[6], registro[7])
                ventas.append(venta)
            
            return ventas
    
    @classmethod
    def insertar(cls, venta):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__INSERT))
            #logger.debug(f"Venta a insertar: {venta}")
            values = (venta.getFechaVenta(), venta.getCantidad(), venta.getSubtotal(), venta.getTotal(), venta.getDireccionEnvio(), venta.getCodigoVideojuego(), venta.getCodigoCliente())
            cursor.execute(cls.__INSERT, values)
            
            return cursor.rowcount
    
    @classmethod
    def actualizar(cls, venta):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__UPDATE))
            #logger.debug(f"Venta a actualizar: {venta}")
            values = (venta.getFechaVenta(), venta.getCantidad(), venta.getSubtotal(), venta.getTotal(), venta.getDireccionEnvio(), venta.getCodigoVideojuego(), venta.getCodigoCliente(), venta.getIdVenta())
            cursor.execute(cls.__UPDATE, values)
            
            return cursor.rowcount
    
    @classmethod
    def eliminar(cls, venta):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__DELETE))
            #logger.debug(f"Venta a eliminar: {venta}")
            values = (venta.getIdVenta(),)
            cursor.execute(cls.__DELETE, values)
            
            return cursor.rowcount
    
     # EL USUARIO MANDA EL NOMBRE DEL CLIENTE PARA DEVOLVER EL OBJETO CLIENTE
    @classmethod
    def buscar_cliente(cls, nombre_cliente):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__SEARCH_CLIENTE))
            values = (nombre_cliente,)
            cursor.execute(cls.__SEARCH_CLIENTE, values)
            registro = cursor.fetchone()

            cliente = Cliente(registro[0], registro[1], registro[2], registro[3], registro[4])
            
            return cliente
        
    # SE BUSCAN LAS VENTAS CON EL ID DEL CLIENTE A PARTIR DEL OBJETO DEVUELTO POR buscar_cliente
    @classmethod
    def buscar(cls, id_cliente):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__SEARCH))
            values = (id_cliente,)
            cursor.execute(cls.__SEARCH, values)
            registros = cursor.fetchall()

            ventas = []
            for registro in registros:
                venta = Venta(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5], registro[6], registro[7])
                ventas.append(venta)
            
            return ventas

    # Método que recupera la compra con el ID que recibe
    @classmethod
    def recuperar(cls, id_venta):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__SELECT_ONE))
            values = (id_venta,)
            cursor.execute(cls.__SELECT_ONE, values)
            registro = cursor.fetchone()
        
            venta = Venta(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5], registro[6], registro[7])
            
            return venta

# SIMULACIONES
if __name__ == "__main__":
    # SIMULANDO SELECT
    #ventas = VentaDao.seleccionar()
    #for venta in ventas:
    #    logger.debug(venta)
    
    # SIMULANDO INSERT
    #venta = Venta(fecha_venta="14/11/2020", cantidad=2, subtotal=100.00, total=200.00, direccion_envio="Libertad 45", codigo_videojuego=2, codigo_cliente=1)
    #registros_insertados = VentaDao.insertar(venta)
    #logger.debug(f"Registros insertados: {registros_insertados}")
    
    # SIMULANDO UPDATE
    #venta = Venta(2, "10/12/2021", 3, 100.00, 300.00, "5 de Mayo S/N", 2, 1)
    #registros_actualizados = VentaDao.actualizar(venta)
    #logger.debug(f"Registros actualizados: {registros_actualizados}")
    
    # SIMULANDO DELETE
    #venta = Venta(id_venta=2)
    #registros_eliminados = VentaDao.eliminar(venta)
    #logger.debug(f"Registros eliminados: {registros_eliminados}")
    
    # SIMULANDO BUSQUEDA
    #nombre_cliente = "Don Lizardi"
    nombre_cliente = input("Ingrese nombre del cliente para ver sus ventas: ")
    cliente = VentaDao.buscar_cliente(nombre_cliente)
    
    ventas = VentaDao.buscar(cliente.getIdCliente())
    for venta in ventas:
        print(venta)
    
    id_venta = input("\n\nSeleccione el id de la venta para modificar: ")
    venta = VentaDao.recuperar(id_venta)
    print(F"VENTA SELECCIONADA PARA MODIFICACION/ELIMINACION: {venta}")
