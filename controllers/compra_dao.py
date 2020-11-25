from models.compra import Compra
from models.empleado import Empleado
from services.cursor import CursorDelPool
from services.logger_conf import logger

class CompraDao:
    # SENTENCIAS SQL
    __SELECT = "SELECT compra.id_compra, compra.estado_compra, compra.fecha_compra, precio_compra, videojuego.nombre_juego, empleado.nombre_empleado FROM compra INNER JOIN videojuego ON compra.codigo_videojuego=videojuego.id_juego INNER JOIN empleado ON compra.codigo_empleado=empleado.id_empleado"
    __INSERT = "INSERT INTO compra(estado_compra, fecha_compra, precio_compra, codigo_videojuego, codigo_empleado) VALUES(%s, %s, %s, %s, %s)"
    __UPDATE = "UPDATE compra SET estado_compra = %s, fecha_compra = %s, precio_compra = %s, codigo_videojuego = %s, codigo_empleado = %s WHERE id_compra = %s"
    __DELETE = "DELETE FROM compra WHERE id_compra = %s"
    __SEARCH_EMPLEADO = "SELECT * FROM empleado WHERE nombre_empleado LIKE %s"
    __SEARCH = "SELECT * FROM compra WHERE CAST(codigo_empleado AS VARCHAR) LIKE CAST(%s AS VARCHAR)"
    __SELECT_ONE =  "SELECT * FROM compra WHERE id_compra = %s"
    
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
    
    # EL USUARIO MANDA EL NOMBRE DEL EMPLEADO PARA DEVOLVER EL OBJETO EMPLEADO
    @classmethod
    def buscar_empleado(cls, nombre_empleado):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__SEARCH_EMPLEADO))
            values = (nombre_empleado,)
            cursor.execute(cls.__SEARCH_EMPLEADO, values)
            registro = cursor.fetchone()

            empleado = Empleado(registro[0], registro[1], registro[2], registro[3])
            
            return empleado
        
    # SE BUSCAN LAS COMPRAS CON EL ID DEL EMPLEADO A PARTIR DEL OBJETO DEVUELTO POR buscar_empleado
    @classmethod
    def buscar(cls, id_empleado):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__SEARCH))
            values = (id_empleado,)
            cursor.execute(cls.__SEARCH, values)
            registros = cursor.fetchall()

            compras = []
            for registro in registros:
                compra = Compra(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5])
                compras.append(compra)
            
            return compras

    # Método que recupera la compra con el ID que recibe
    @classmethod
    def recuperar(cls, id_compra):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__SELECT_ONE))
            values = (id_compra,)
            cursor.execute(cls.__SELECT_ONE, values)
            registro = cursor.fetchone()
        
            compra = Compra(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5])
            
            return compra

# SIMULACIONES
if __name__ == "__main__":
    # SIMULANDO SELECT
    #compras = CompraDao.seleccionar()
    #for compra in compras:
    #    logger.debug(compra)
    
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
    
    # SIMULANDO BUSQUEDA
    #nombre_empleado = "Antonio"
    nombre_empleado = input("Ingrese nombre del empleado para ver sus compras: ")
    empleado = CompraDao.buscar_empleado(nombre_empleado)
    
    compras = CompraDao.buscar(empleado.getIdEmpleado())
    for compra in compras:
        print(compra)
    
    id_compra = input("\n\nSeleccione el id de la compra para modificar: ")
    compra = CompraDao.recuperar(id_compra)
    print(F"COMPRA SELECCIONADA PARA MODIFICACION/ELIMINACION: {compra}")  
