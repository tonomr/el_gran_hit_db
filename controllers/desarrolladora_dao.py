# CLASE DESARROLLADORA DAO (DATA ACCESS OBJECT) PARA ADMINISTRAR LOS DATOS DE LA BASE DE DATOS

from models.desarrolladora import Desarrolladora # IMPORTAMOS LA CLASE DESARROLLADORA
from services.cursor import CursorDelPool # IMPORTAMOS EL CURSOR DEL POOL DE CONEXIONES
from services.logger_conf import logger # IMPORTAMOS EL LOGGER

class DesarrolladoraDao:
    # SENTENCIAS
    __SELECT = "SELECT * FROM desarrolladora"
    __INSERT = "INSERT INTO desarrolladora(nombre_desarrolladora, telefono_desarrolladora, direccion_desarrolladora) VALUES(%s, %s, %s)"
    __UPDATE = "UPDATE desarrolladora SET nombre_desarrolladora = %s, telefono_desarrolladora = %s, direccion_desarrolladora = %s WHERE id_desarrolladora = %s"
    __DELETE = "DELETE FROM desarrolladora WHERE id_desarrolladora = %s"
    __SEARCH = "SELECT * FROM desarrolladora WHERE nombre_desarrolladora LIKE %s"
    __SELECT_ONE =  "SELECT * FROM desarrolladora WHERE id_desarrolladora = %s"

    listadoDesarrolladoras = None
    
    # METODO SELECT PARA MOSTRAR LOS REGISTROS DE LA TABLA DESARROLLADORA
    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__SELECT)) # SENTENCIA A EJECUTAR
            cursor.execute(cls.__SELECT) # EJECUCION DE LA SENTENCIA
            registros = cursor.fetchall() # GUARDAMOS LOS REGISTROS
        
            desarrolladoras = [] # DEFINICION DE UNA LISTA PARA IMPRIMIR LOS RESULTADOS
            # POR CADA REGISTRO GUARDADO EN REGISTROS, AGREGARLO A LA LISTA desarrolladoras COMO OBJETOS
            for registro in registros:
                desarrolladora = Desarrolladora(registro[0], registro[1], registro[2], registro[3])
                desarrolladoras.append(desarrolladora)

            return desarrolladoras # RETORNAMOS LA LISTA
    
    # METODO INSERTAR PARA AGREGAR REGISTROS
    @classmethod
    def insertar(cls, desarrolladora):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__INSERT)) # SENTENCIA A EJECUTAR
            logger.debug(f"Desarrolladora a insertar: {desarrolladora}") # OBJETO desarrolladora A INSERTAR
            values = (desarrolladora.getNombreDesarrolladora(), desarrolladora.getTelefonoDesarrolladora(), desarrolladora.getDireccionDesarrolladora())
            cursor.execute(cls.__INSERT, values) # EJECUCION DE LA SENTENCIA
            
            return cursor.rowcount # RETORNAMOS EL NUMERO DE INSERCIONES
    
    # METODO ACTUALIZAR PARA MODIFICAR REGISTROS
    @classmethod
    def actualizar(cls, desarrolladora):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__UPDATE)) # SENTENCIA A EJECUTAR
            logger.debug(f"Desarrolladora a actualizar: {desarrolladora}") # SE IMPRIME EL OBJETO desarrolladora A ACTUALIZAR
            values = (desarrolladora.getNombreDesarrolladora(), desarrolladora.getTelefonoDesarrolladora(), desarrolladora.getDireccionDesarrolladora(), desarrolladora.getIdDesarrolladora())
            cursor.execute(cls.__UPDATE, values) # EJECUCION DE LA SENTENCIA
            
            return cursor.rowcount # RETORNAMOS EL NUMERO DE ACTUALIZACIONES
    
    # METODO ELIMINAR PARA BORRAR REGISTROS
    @classmethod
    def eliminar(cls, desarrolladora):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__DELETE)) # SENTENCIA A EJECUTAR
            logger.debug(f"Desarrolladora a eliminar: {desarrolladora}") # SE IMPRIME EL OBJETO desarrolladora A ELIMINAR
            values = (desarrolladora.getIdDesarrolladora(),)
            cursor.execute(cls.__DELETE, values) # EJECUCION DE LA SENTENCIA
            
            return cursor.rowcount # RETORNAMOS EL NUMERO DE ELIMINACIONES
        
    # ESTE METODO RECIBE UN ID DE DESARROLLADORA PARA DEVOLVER MEDIANTE UNA BUSQUEDA EL NOMBRE DE TAL
    @classmethod
    def buscarNombre(cls, id_busqueda):
        nombre_encontrado = None
        if cls.listadoDesarrolladoras == None:
            cls.listadoDesarrolladoras = DesarrolladoraDao.seleccionar()
        for desarrolladora in cls.listadoDesarrolladoras:
            if desarrolladora.getIdDesarrolladora() == id_busqueda:
                nombre_encontrado = desarrolladora.getNombreDesarrolladora()
                break
        return nombre_encontrado
    
    @classmethod
    def buscar(cls, key_word):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__SEARCH))
            cursor.execute(cls.__SEARCH, key_word)
            registros = cursor.fetchall()

            desarrolladoras = []
            for registro in registros:
                desarrolladora = Desarrolladora(registro[0], registro[1], registro[2], registro[3])
                desarrolladoras.append(desarrolladora)
            
            return desarrolladoras

    # Método que recupera el videjuego con el ID que recibe
    @classmethod
    def recuperar(cls, id):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__SELECT_ONE))
            cursor.execute(cls.__SELECT_ONE, id)
            registro = cursor.fetchone()
        
            desarrolladora = Desarrolladora(registro[0], registro[1], registro[2], registro[3])

            return desarrolladora

# SIMULACIONES (SOLO SE EJECUTARA CUANDO SE EJECUTE ESTE MODULO)
if __name__ == "__main__":
    # PRUEBA SELECT
    desarrolladoras = DesarrolladoraDao.seleccionar()
    # POR CADA REGISTRO EN LA LISTA desarrolladoras IMPRIMIR CON SU METODO STR
    for desarrolladora in desarrolladoras:
        logger.debug(desarrolladora)
    #    logger.debug(desarrolladora.getIdDesarrolladora()) # SE PUEDE IMPRIMIR LOS CAMPOS POR SEPARADO
    
    # PRUEBA INSERT
    #desarrolladora = Desarrolladora(nombre_desarrolladora="Nintendo", telefono_desarrolladora="1234567890", direccion_desarrolladora="Puntasvergas 123")
    #registros_insertados = DesarrolladoraDao.insertar(desarrolladora)
    #logger.debug(f"Registros insertados: {registros_insertados}")
    
    #PRUEBA UPDATE
    #desarrolladora = Desarrolladora(2, "Nintendo Ultimate", "0987654321", "Lomas de los Alots")
    #registros_actualizados = DesarrolladoraDao.actualizar(desarrolladora)
    #logger.debug(f"Registros actualizados: {registros_actualizados}")
    
    #PRUEBA DELETE
    #desarrolladora = Desarrolladora(id_desarrolladora=2)
    #registros_eliminados = DesarrolladoraDao.eliminar(desarrolladora)
    #logger.debug(f"Registros eliminados: {registros_eliminados}")
