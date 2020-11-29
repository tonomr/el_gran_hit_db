# CLASE EMPLEADO DAO (DATA ACCESS OBJECT) PARA ADMINISTRAR LOS DATOS DE LA BASE DE DATOS

from models.empleado import Empleado # IMPORTAMOS LA CLASE EMPLEADO
from services.cursor import CursorDelPool # IMPORTAMOS EL CURSOR DEL POOL DE CONEXIONES
from services.logger_conf import logger # IMPORTAMOS EL LOGGER

class EmpleadoDao:
    # SENTENCIAS
    __SELECT = "SELECT * FROM empleados ORDER BY id_empleado"
    __INSERT = "INSERT INTO empleados(nombre_empleado, telefono_empleado, direccion_empleado) VALUES(%s, %s, %s)"
    __UPDATE = "UPDATE empleados SET nombre_empleado = %s, telefono_empleado = %s, direccion_empleado = %s WHERE id_empleado = %s"
    __DELETE = "DELETE FROM empleados WHERE id_empleado = %s"
    __SEARCH = "SELECT * FROM empleados WHERE nombre_empleado LIKE %s"
    __SELECT_ONE =  "SELECT * FROM empleados WHERE id_empleado = %s"
    __SELECT_NOMBRE = "SELECT nombre_empleado FROM empleados WHERE id_empleado = %s"
    
    # METODO SELECT PARA MOSTRAR LOS REGISTROS DE LA TABLA EMPLEADO
    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__SELECT)) # SENTENCIA A EJECUTAR
            cursor.execute(cls.__SELECT) # EJECUCION DE LA SENTENCIA
            registros = cursor.fetchall() # GUARDAMOS LOS REGISTROS
        
            empleados = [] # DEFINICION DE UNA LISTA PARA IMPRIMIR LOS RESULTADOS
            # POR CADA REGISTRO GUARDADO EN REGISTROS, AGREGARLO A LA LISTA empleados COMO OBJETOS
            for registro in registros:
                empleado = Empleado(registro[0], registro[1], registro[2], registro[3])
                empleados.append(empleado)

            return empleados # RETORNAMOS LA LISTA
    
    # METODO INSERTAR PARA AGREGAR REGISTROS
    @classmethod
    def insertar(cls, empleado):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__INSERT)) # SENTENCIA A EJECUTAR
            #logger.debug(f"Empleado a insertar: {empleado}") # OBJETO empleado A INSERTAR
            values = (empleado.get_nombre_empleado(), empleado.get_telefono_empleado(), empleado.get_direccion_empleado())
            cursor.execute(cls.__INSERT, values) # EJECUCION DE LA SENTENCIA
            
            return cursor.rowcount # RETORNAMOS EL NUMERO DE INSERCIONES
    
    # METODO ACTUALIZAR PARA MODIFICAR REGISTROS
    @classmethod
    def actualizar(cls, empleado):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__UPDATE)) # SENTENCIA A EJECUTAR
            #logger.debug(f"Empleado a actualizar: {empleado}") # SE IMPRIME EL OBJETO empleado A ACTUALIZAR
            values = (empleado.get_nombre_empleado(), empleado.get_telefono_empleado(), empleado.get_direccion_empleado(), empleado.get_id_empleado())
            cursor.execute(cls.__UPDATE, values) # EJECUCION DE LA SENTENCIA
            
            return cursor.rowcount # RETORNAMOS EL NUMERO DE ACTUALIZACIONES
    
    # METODO ELIMINAR PARA BORRAR REGISTROS
    @classmethod
    def eliminar(cls, empleado):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__DELETE)) # SENTENCIA A EJECUTAR
            #logger.debug(f"Empleado a eliminar: {empleado}") # SE IMPRIME EL OBJETO empleado A ELIMINAR
            values = (empleado.get_id_empleado(),)
            cursor.execute(cls.__DELETE, values) # EJECUCION DE LA SENTENCIA
            
            return cursor.rowcount # RETORNAMOS EL NUMERO DE ELIMINACIONES
    
    @classmethod
    def buscar(cls, key_word):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__SEARCH))
            values = (key_word,)
            cursor.execute(cls.__SEARCH, values)
            registros = cursor.fetchall()

            empleados = []
            for registro in registros:
                empleado = Empleado(registro[0], registro[1], registro[2], registro[3])
                empleados.append(empleado)
            
            return empleados

    # Método que recupera el item con el ID que recibe
    @classmethod
    def recuperar(cls, id):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__SELECT_ONE))
            values = (id,)
            cursor.execute(cls.__SELECT_ONE, values)
            registro = cursor.fetchone()
            empleado = Empleado(registro[0], registro[1], registro[2], registro[3])

            return empleado

    # Método que recupera el nombre del empleado con el ID que recibe
    @classmethod
    def buscar_nombre(cls, id):
        with CursorDelPool() as cursor:
            #logger.debug(cursor.mogrify(cls.__SELECT_NOMBRE))
            values = (id,)
            cursor.execute(cls.__SELECT_NOMBRE, values)
            registro = cursor.fetchone()
            return registro

# SIMULACIONES (SOLO SE EJECUTARA CUANDO SE EJECUTE ESTE MODULO)
if __name__ == "__main__":
    # PRUEBA SELECT
    empleados = EmpleadoDao.seleccionar()
    # POR CADA REGISTRO EN LA LISTA empleados IMPRIMIR CON SU METODO STR
    for empleado in empleados:
        logger.debug(empleado)
    #    logger.debug(empleado.get_id_empleado()) # SE PUEDE IMPRIMIR LOS CAMPOS POR SEPARADO
    
    # PRUEBA INSERT
    #empleado = Empleado(nombre_empleado="Antonio Magaña", telefono_empleado="9341156600", direccion_empleado="Calle Libertad #45")
    #registros_insertados = EmpleadoDao.insertar(empleado)
    #logger.debug(f"Registros insertados: {registros_insertados}")
    
    #PRUEBA UPDATE
    #empleado = Empleado(3, "Antonio Reynoso", "9341156600", "Calle Libertad #45")
    #registros_actualizados = EmpleadoDao.actualizar(empleado)
    #logger.debug(f"Registros actualizados: {registros_actualizados}")
    
    #PRUEBA DELETE
    #empleado = Empleado(id_empleado=3)
    #registros_eliminados = EmpleadoDao.eliminar(empleado)
    #logger.debug(f"Registros eliminados: {registros_eliminados}")
