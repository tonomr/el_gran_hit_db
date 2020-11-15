from models.compra import Compra
from services.cursor import CursorDelPool
from services.logger_conf import logger

class CompraDao:
    # SENTENCIAS SQL
    __SELECT = "SELECT compra.id_compra, compra.estado_compra, compra.fecha_compra, precio_compra, videojuego.nombre_juego, empleado.nombre_empleado FROM compra INNER JOIN videojuego ON compra.codigo_videojuego=videojuego.id_juego INNER JOIN empleado ON compra.codigo_empleado=empleado.id_empleado"
    __INSERT = "INSERT INTO compra(estado_compra, fecha_compra, precio_compra, codigo_videojuego, codigo_empleado) VALUES(%s, %s, %s, %s, %s)"
    __UPDATE = "UPDATE compra SET estado_compra = %s, fecha_compra = %s, precio_compra = %s, codigo_videojuego = %s, codigo_empleado = %s WHERE id_compra = %s"
    __DELETE = "DELETE FROM compra WHERE id_compra = %s"
    
    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__SELECT))
            cursor.execute(cls.__SELECT)
            registros = cursor.fetchall()
            
            compras = []
            for registro in registros:
                compra = Compra(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5])
                compras.append(compra)
            
            return compras
    
    @classmethod
    def insertar(cls, compra):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__INSERT))
            logger.debug(f"Compra a insertar: {compra}")
            values = (compra.getEstadoCompra(), compra.getFechaCompra(), compra.getPrecioCompra(), compra.getCodigoVideojuego(), compra.getCodigoEmpleado())
            cursor.execute(cls.__INSERT, values)
            
            return cursor.rowcount
    
    @classmethod
    def actualizar(cls, compra):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__UPDATE))
            logger.debug(f"Compra a actualizar: {compra}")
            values = (compra.getEstadoCompra(), compra.getFechaCompra(), compra.getPrecioCompra(), compra.getCodigoVideojuego(), compra.getCodigoEmpleado(), compra.getIdCompra())
            cursor.execute(cls.__UPDATE, values)
            
            return cursor.rowcount
    
    @classmethod
    def eliminar(cls, compra):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__DELETE))
            logger.debug(f"Compra a eliminar: {compra}")
            values = (compra.getIdCompra(),)
            cursor.execute(cls.__DELETE, values)
            
            return cursor.rowcount

# SIMULACIONES
if __name__ == "__main__":
    # SIMULANDO SELECT
    compras = CompraDao.seleccionar()
    for compra in compras:
        logger.debug(compra)
    
    # SIMULANDO INSERT
    #compra = Compra(estado_compra="Semi-nuevo", fecha_compra="14/11/2020", precio_compra=433.33, codigo_videojuego=2, codigo_empleado=1)
    #registros_insertados = CompraDao.insertar(compra)
    #logger.debug(f"Registros insertados: {registros_insertados}")
    
    # SIMULANDO UPDATE
    #compra = Compra(2, "Usado", "10/12/2021", 100.00, 2, 1)
    #registros_actualizados = CompraDao.actualizar(compra)
    #logger.debug(f"Registros actualizados: {registros_actualizados}")
    
    # SIMULANDO DELETE
    #compra = Compra(id_compra=2)
    #registros_eliminados = CompraDao.eliminar(compra)
    #logger.debug(f"Registros eliminados: {registros_eliminados}")
