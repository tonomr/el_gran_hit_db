from models.compra import Compra
from models.empleado import Empleado
from services.cursor import CursorDelPool
from services.logger_conf import logger

class CompraDao:
    # SENTENCIAS SQL
    __SELECT = "SELECT compras.id_compra, compras.fecha_compra, compras.estado_compra, precio_compra, videojuegos.nombre_videojuego, empleados.nombre_empleado FROM compras INNER JOIN videojuegos ON compras.codigo_videojuego=videojuegos.id_videojuego INNER JOIN empleados ON compras.codigo_empleado=empleados.id_empleado ORDER BY id_compra"
    __INSERT = "INSERT INTO compras(fecha_compra, estado_compra, precio_compra, codigo_videojuego, codigo_empleado) VALUES(%s, %s, %s, %s, %s)"
    __UPDATE = "UPDATE compras SET fecha_compra = %s, estado_compra = %s, precio_compra = %s, codigo_videojuego = %s, codigo_empleado = %s WHERE id_compra = %s"
    __DELETE = "DELETE FROM compras WHERE id_compra = %s"
    __SEARCH_EMPLEADO = "SELECT * FROM empleados WHERE nombre_empleado LIKE %s"
    __SEARCH = "SELECT * FROM compras WHERE codigo_empleado = %s" 
    __SELECT_ONE =  "SELECT * FROM compras WHERE id_compra = %s"
    
    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            #logger.debug(cursor.mogrify(cls.__SELECT))
            logger.debug("Llega aqui")
            cursor.execute(cls.__SELECT)
            registros = cursor.fetchall()
            logger.debug("TAMBIEN AQUI")
            compras = []
            for registro in registros:
                compra = Compra(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5])
                compras.append(compra)
            return compras
    
    @classmethod
    def insertar(cls, compra):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__INSERT))
            #logger.debug(f"Compra a insertar: {compra}")
            values = (compra.get_fecha_compra(), compra.get_estado_compra(), compra.get_precio_compra(), compra.get_codigo_videojuego(), compra.get_codigo_empleado())
            cursor.execute(cls.__INSERT, values)
            
            return cursor.rowcount
    
    @classmethod
    def actualizar(cls, compra):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__UPDATE))
            #logger.debug(f"Compra a actualizar: {compra}")
            values = (compra.get_fecha_compra(), compra.get_estado_compra(), compra.get_precio_compra(), compra.get_codigo_videojuego(), compra.get_codigo_empleado(), compra.get_id_compra())
            cursor.execute(cls.__UPDATE, values)
            
            return cursor.rowcount
    
    @classmethod
    def eliminar(cls, compra):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__DELETE))
            #logger.debug(f"Compra a eliminar: {compra}")
            logger.debug("Lllega aqui")
            values = (compra.get_id_compra(),)
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
    #compra = Compra(fecha_compra="14/11/2020", estado_compra="Semi-nuevo", precio_compra=433.33, codigo_videojuego=2, codigo_empleado=1)
    #registros_insertados = CompraDao.insertar(compra)
    #logger.debug(f"Registros insertados: {registros_insertados}")
    
    # SIMULANDO UPDATE
    #compra = Compra(3, "10/12/2021", "Usado", 100.00, 2, 1)
    #registros_actualizados = CompraDao.actualizar(compra)
    #logger.debug(f"Registros actualizados: {registros_actualizados}")
    
    # SIMULANDO DELETE
    #compra = Compra(id_compra=3)
    #registros_eliminados = CompraDao.eliminar(compra)
    #logger.debug(f"Registros eliminados: {registros_eliminados}")
    
    # SIMULANDO BUSQUEDA
    nombre_empleado = input("Ingrese nombre del empleado para ver sus compras: ")
    empleado = CompraDao.buscar_empleado(nombre_empleado)
    
    compras = CompraDao.buscar(empleado.get_id_empleado())
    for compra in compras:
        print(compra)
    
    id_compra = input("\n\nSeleccione el id de la compra para modificar: ")
    compra = CompraDao.recuperar(id_compra)
    print(F"COMPRA SELECCIONADA PARA MODIFICACION/ELIMINACION: {compra}")  
