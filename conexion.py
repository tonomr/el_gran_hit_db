# CONFIGURACION PARA LA CONEXION A LA BASE DE DATOS

# DE NUESTRA CONFIGURACION DE LOGGER IMPORTAMOS LA DEFINICION
from logger_conf import logger
from psycopg2 import pool  # MODULO PARA LA CONEXION PYTHON CON POSTGRESQL
import sys  # MODULO PARA TERMINAR LA EJECUCION DEL PROGRAMA SI HAY ERROR

# CLASE CONEXION, DATOS DE LA CONEXION Y LOS OBJETOS CONEXION Y CURSOR


class Conexion:
    __DATABASE = "el_gran_hit_db"
    __USERNAME = "postgres"
    __PASSWORD = "admin"
    __PORT = "5433"
    __HOST = "127.0.0.1"
    __MIN_CON = 1
    __MAX_CON = 5
    __pool = None

    @classmethod
    def obtenerPool(cls):
        if cls.__pool is None:
            try:
                cls.__pool = pool.SimpleConnectionPool(cls.__MIN_CON,
                                                       cls.__MAX_CON,
                                                       user=cls.__USERNAME,
                                                       password=cls.__PASSWORD,
                                                       host=cls.__HOST,
                                                       port=cls.__PORT,
                                                       database=cls.__DATABASE)

                logger.info(f"Pool exitoso {cls.__pool}")
                return cls.__pool

            except Exception as excepcion:
                logger.error(f"Error {excepcion}")
                sys.exit()
        else:
            return cls.__pool

    # EL METODO obtenerConexion REGRESA UN OBJETO CONEXION SI ES POSIBLE CONECTAR A LA BASE DE DATOS, SINO, TERMINA EL PROGRAMA
    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()
        logger.debug(f"Pool exitoso {conexion}")
        return conexion
        
    @classmethod
    def liberarConexion(cls, conexion):
        #Regresar una conexion al pool
        cls.obtenerPool().putconn(conexion)
        logger.debug(f"Regresamos la conexion al pool: {conexion}")
        logger.debug(f"Estado del pool: {cls.__pool}")

    # EL METODO cerrarConexiones CIERRA LA CONEXION Y EL CURSOR SI ES QUE EXISTEN, SINO, IMPRIME ERROR
    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall()
        logger.debug(f"Cerramos todas las conexiones del pool: {cls.__pool}")

# PRUEBA DE CONFIGURACION (SOLO SE EJECUTARA CUANDO SE EJECUTE ESTE MODULO)
if __name__ == "__main__":
    #Obtener conexion a partir del pool
    conexion1 = Conexion.obtenerConexion()
    conexion2 = Conexion.obtenerConexion()
    #Regresar conexiones al pool
    Conexion.liberarConexion(conexion1)
    Conexion.liberarConexion(conexion2)
    conexion3 = Conexion.obtenerConexion()
    
    #Cerrar pool
    Conexion.cerrarConexiones()
    #Si intentamos pedir una conexion al pool cerrado
    #conexion3 = Conexion.obtenerConexion() #Error: Pool cerrado
