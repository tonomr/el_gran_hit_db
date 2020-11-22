# CLASE CLIENTES DAO (DATA ACCESS OBJECT) PARA ADMINISTRAR LOS DATOS DE LA BASE DE DATOS

from models.cliente import Cliente # IMPORTAMOS LA CLASE CLIENTE
from services.cursor import CursorDelPool # IMPORTAMOS EL CURSOR DEL POOL DE CONEXIONES
from services.logger_conf import logger # IMPORTAMOS EL LOGGER

class ClienteDao:
    # SENTENCIAS
    __SELECT = "SELECT * FROM cliente"
    __INSERT = "INSERT INTO cliente(nombre_cliente, email, direccion_cliente, telefono_cliente) VALUES(%s, %s, %s, %s)"
    __UPDATE = "UPDATE cliente SET nombre_cliente = %s, email = %s, direccion_cliente = %s, telefono_cliente = %s WHERE id_cliente = %s"
    __DELETE = "DELETE FROM cliente WHERE id_cliente = %s"
    __SEARCH = "SELECT * FROM cliente WHERE nombre_cliente LIKE %s"
    __SELECT_ONE =  "SELECT * FROM cliente WHERE id_cliente = %s"
    
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
            values = (cliente.getNombreCliente(), cliente.getEmail(), cliente.getDireccionCliente(), cliente.getTelefonoCliente())
            cursor.execute(cls.__INSERT, values) # EJECUCION DE LA SENTENCIA
            
            return cursor.rowcount # RETORNAMOS EL NUMERO DE INSERCIONES
    
    # METODO ACTUALIZAR PARA MODIFICAR REGISTROS
    @classmethod
    def actualizar(cls, cliente):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__UPDATE)) # SENTENCIA A EJECUTAR
            values = (cliente.getNombreCliente(), cliente.getEmail(), cliente.getDireccionCliente(), cliente.getTelefonoCliente(), cliente.getIdCliente())
            cursor.execute(cls.__UPDATE, values) # EJECUCION DE LA SENTENCIA
            
            return cursor.rowcount # RETORNAMOS EL NUMERO DE ACTUALIZACIONES
    
    # METODO ELIMINAR PARA BORRAR REGISTROS
    @classmethod
    def eliminar(cls, cliente):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__DELETE)) # SENTENCIA A EJECUTAR
            values = (cliente.getIdCliente(),)
            cursor.execute(cls.__DELETE, values) # EJECUCION DE LA SENTENCIA
            
            return cursor.rowcount # RETORNAMOS EL NUMERO DE ELIMINACIONES
    
    @classmethod
    def buscar(cls, key_word):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__SEARCH))
            cursor.execute(cls.__SEARCH, key_word)
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
            cursor.execute(cls.__SELECT_ONE, id)
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
    #    logger.debug(cliente.getIdCliente()) # SE PUEDE IMPRIMIR LOS CAMPOS POR SEPARADO
    
    # PRUEBA INSERT
    #cliente = Cliente(nombre_cliente="Antonio Magaña", email="maganatono@mail.com", direccion_cliente="Libertad 45", telefono_cliente="9341156600")
    #registros_insertados = ClienteDao.insertar(cliente)
    #logger.debug(f"Registros insertados: {registros_insertados}")
    
    #PRUEBA UPDATE
    #cliente = Cliente(2, "Antonio Reynoso", "tonomagana@live.com", "Libertad #45", "9341156600")
    #registros_actualizados = ClienteDao.actualizar(cliente)
    #logger.debug(f"Registros actualizados: {registros_actualizados}")
    
    #PRUEBA DELETE
    #cliente = Cliente(id_cliente=2)
    #registros_eliminados = ClienteDao.eliminar(cliente)
    #logger.debug(f"Registros eliminados: {registros_eliminados}")
