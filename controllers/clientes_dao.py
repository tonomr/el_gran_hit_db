# CLASE CLIENTES DAO (DATA ACCESS OBJECT) PARA ADMINISTRAR LOS DATOS DE LA BASE DE DATOS

from models.cliente import Cliente # IMPORTAMOS LA CLASE CLIENTE
from services.cursor import CursorDelPool # IMPORTAMOS EL CURSOR DEL POOL DE CONEXIONES
from services.logger_conf import logger # IMPORTAMOS EL LOGGER

class ClienteDao:
    # SENTENCIAS
    __SELECT = "SELECT * FROM clientes ORDER BY id_cliente"
    __INSERT = "INSERT INTO clientes(nombre_cliente, email_cliente, telefono_cliente, direccion_cliente) VALUES(%s, %s, %s, %s)"
    __UPDATE = "UPDATE clientes SET nombre_cliente = %s, email_cliente = %s, telefono_cliente = %s, direccion_cliente = %s WHERE id_cliente = %s"
    __DELETE = "DELETE FROM clientes WHERE id_cliente = %s"
    __SEARCH = "SELECT * FROM clientes WHERE nombre_cliente LIKE %s"
    __SELECT_ONE =  "SELECT * FROM clientes WHERE id_cliente = %s"
    
    # METODO SELECT PARA MOSTRAR LOS REGISTROS DE LA TABLA EMPLEADO
    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__SELECT)) # SENTENCIA A EJECUTAR
            cursor.execute(cls.__SELECT) # EJECUCION DE LA SENTENCIA
            registros = cursor.fetchall() # GUARDAMOS LOS REGISTROS
        
            clientes = [] # DEFINICION DE UNA LISTA PARA IMPRIMIR LOS RESULTADOS
            # POR CADA REGISTRO GUARDADO EN REGISTROS, AGREGARLO A LA LISTA clientes COMO OBJETOS
            for registro in registros:
                cliente = Cliente(registro[0], registro[1], registro[2], registro[3], registro[4])
                clientes.append(cliente)

            return clientes # RETORNAMOS LA LISTA
    
    # METODO INSERTAR PARA AGREGAR REGISTROS
    @classmethod
    def insertar(cls, cliente):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__INSERT)) # SENTENCIA A EJECUTAR
            values = (cliente.get_nombre_cliente(), cliente.get_email_cliente(), cliente.get_telefono_cliente(), cliente.get_direccion_cliente())
            cursor.execute(cls.__INSERT, values) # EJECUCION DE LA SENTENCIA
            
            return cursor.rowcount # RETORNAMOS EL NUMERO DE INSERCIONES
    
    # METODO ACTUALIZAR PARA MODIFICAR REGISTROS
    @classmethod
    def actualizar(cls, cliente):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__UPDATE)) # SENTENCIA A EJECUTAR
            values = (cliente.get_nombre_cliente(), cliente.get_email_cliente(), cliente.get_telefono_cliente(), cliente.get_direccion_cliente(), cliente.get_id_cliente())
            cursor.execute(cls.__UPDATE, values) # EJECUCION DE LA SENTENCIA
            
            return cursor.rowcount # RETORNAMOS EL NUMERO DE ACTUALIZACIONES
    
    # METODO ELIMINAR PARA BORRAR REGISTROS
    @classmethod
    def eliminar(cls, cliente):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__DELETE)) # SENTENCIA A EJECUTAR
            values = (cliente.get_id_cliente(),)
            cursor.execute(cls.__DELETE, values) # EJECUCION DE LA SENTENCIA

            return cursor.rowcount # RETORNAMOS EL NUMERO DE ELIMINACIONES
    
    @classmethod
    def buscar(cls, key_word):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__SEARCH))
            values = (key_word,)
            cursor.execute(cls.__SEARCH, values)
            registros = cursor.fetchall()

            clientes = []
            for registro in registros:
                cliente = Cliente(registro[0], registro[1], registro[2], registro[3], registro[4])
                clientes.append(cliente)
            
            return clientes

    # Método que recupera el item con el ID que recibe
    @classmethod
    def recuperar(cls, id):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__SELECT_ONE))
            values = (id,)
            cursor.execute(cls.__SELECT_ONE, values)
            registro = cursor.fetchone()
        
            cliente = Cliente(registro[0], registro[1], registro[2], registro[3], registro[4])
            return cliente

# SIMULACIONES (SOLO SE EJECUTARA CUANDO SE EJECUTE ESTE MODULO)
if __name__ == "__main__":
    # PRUEBA SELECT
    clientes = ClienteDao.seleccionar()
    # POR CADA REGISTRO EN LA LISTA clientes IMPRIMIR CON SU METODO STR
    for cliente in clientes:
        logger.debug(cliente)
    #    logger.debug(cliente.get_id_cliente()) # SE PUEDE IMPRIMIR LOS CAMPOS POR SEPARADO
    
    # PRUEBA INSERT
    #cliente = Cliente(nombre_cliente="Antonio Magaña", email_cliente="maganatono@mail.com", telefono_cliente="9341156600", direccion_cliente="Libertad 45")
    #registros_insertados = ClienteDao.insertar(cliente)
    #logger.debug(f"Registros insertados: {registros_insertados}")
    
    #PRUEBA UPDATE
    #cliente = Cliente(3, "Antonio Reynoso", "tonomagana@live.com", "9341156600", "Libertad #45")
    #registros_actualizados = ClienteDao.actualizar(cliente)
    #logger.debug(f"Registros actualizados: {registros_actualizados}")
    
    #PRUEBA DELETE
    #cliente = Cliente(id_cliente=3)
    #registros_eliminados = ClienteDao.eliminar(cliente)
    #logger.debug(f"Registros eliminados: {registros_eliminados}")
