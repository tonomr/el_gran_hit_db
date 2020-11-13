# CLASE EMPLEADO DAO (DATA ACCESS OBJECT) PARA ADMINISTRAR LOS DATOS DE LA BASE DE DATOS

from models.empleado import Empleado # IMPORTAMOS LA CLASE EMPLEADO
from services.cursor import CursorDelPool # IMPORTAMOS EL CURSOR DEL POOL DE CONEXIONES
from services.logger_conf import logger # IMPORTAMOS EL LOGGER

class EmpleadoDao:
    # SENTENCIAS
    __SELECT = "SELECT * FROM empleado"
    __INSERT = "INSERT INTO empleado(nombre_empleado, direccion_empleado, telefono_empleado) VALUES(%s, %s, %s)"
    __UPDATE = "UPDATE empleado SET nombre_empleado = %s, direccion_empleado = %s, telefono_empleado = %s WHERE id_empleado = %s"
    __DELETE = "DELETE FROM empleado WHERE id_empleado = %s"
    
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
            logger.debug(f"Empleado a insertar: {empleado}") # OBJETO empleado A INSERTAR
            values = (empleado.getNombreEmpleado(), empleado.getDireccionEmpleado(), empleado.getTelefonoEmpleado())
            cursor.execute(cls.__INSERT, values) # EJECUCION DE LA SENTENCIA
            
            return cursor.rowcount # RETORNAMOS EL NUMERO DE INSERCIONES
    
    # METODO ACTUALIZAR PARA MODIFICAR REGISTROS
    @classmethod
    def actualizar(cls, empleado):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__UPDATE)) # SENTENCIA A EJECUTAR
            logger.debug(f"Empleado a actualizar: {empleado}") # SE IMPRIME EL OBJETO empleado A ACTUALIZAR
            values = (empleado.getNombreEmpleado(), empleado.getDireccionEmpleado(), empleado.getTelefonoEmpleado(), empleado.getIdEmpleado())
            cursor.execute(cls.__UPDATE, values) # EJECUCION DE LA SENTENCIA
            
            return cursor.rowcount # RETORNAMOS EL NUMERO DE ACTUALIZACIONES
    
    # METODO ELIMINAR PARA BORRAR REGISTROS
    @classmethod
    def eliminar(cls, empleado):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__DELETE)) # SENTENCIA A EJECUTAR
            logger.debug(f"Empleado a eliminar: {empleado}") # SE IMPRIME EL OBJETO empleado A ELIMINAR
            values = (empleado.getIdEmpleado(),)
            cursor.execute(cls.__DELETE, values) # EJECUCION DE LA SENTENCIA
            
            return cursor.rowcount # RETORNAMOS EL NUMERO DE ELIMINACIONES

# SIMULACIONES (SOLO SE EJECUTARA CUANDO SE EJECUTE ESTE MODULO)
if __name__ == "__main__":
    # PRUEBA SELECT
    empleados = EmpleadoDao.seleccionar()
    # POR CADA REGISTRO EN LA LISTA empleados IMPRIMIR CON SU METODO STR
    for empleado in empleados:
        logger.debug(empleado)
    #    logger.debug(empleado.getIdEmpleado()) # SE PUEDE IMPRIMIR LOS CAMPOS POR SEPARADO
    
    # PRUEBA INSERT
    #empleado = Empleado(nombre_empleado="Antonio Magaña", direccion_empleado="Libertad 45", telefono_empleado="9341156600")
    #registros_insertados = EmpleadoDao.insertar(empleado)
    #logger.debug(f"Registros insertados: {registros_insertados}")
    
    #PRUEBA UPDATE
    #empleado = Empleado(2, "Antonio Reynoso", "Libertad #45", "9341156600")
    #registros_actualizados = EmpleadoDao.actualizar(empleado)
    #logger.debug(f"Registros actualizados: {registros_actualizados}")
    
    #PRUEBA DELETE
    #empleado = Empleado(id_empleado=2)
    #registros_eliminados = EmpleadoDao.eliminar(empleado)
    #logger.debug(f"Registros eliminados: {registros_eliminados}")
