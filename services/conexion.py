# CONFIGURACION PARA LA CONEXION A LA BASE DE DATOS

from services.logger_conf import logger # DE NUESTRA CONFIGURACION DE LOGGER IMPORTAMOS LA DEFINICION
from psycopg2 import pool  # MODULO PARA LA CONEXION PYTHON CON POSTGRESQL
import sys  # MODULO PARA TERMINAR LA EJECUCION DEL PROGRAMA SI HAY ERROR

# CLASE CONEXION, DATOS DE LA CONEXION Y OBJETO POOL DE CONEXIONES
class Conexion:
    __DATABASE = "el_gran_hit_db"
    __USERNAME = "postgres"
    __PASSWORD = "admin"
    __PORT = "5433"
    __HOST = "127.0.0.1"
    __MIN_CON = 1
    __MAX_CON = 10
    __pool = None

    # EL METODO obtenerPool CREA UN POOL DE CONEXIONES SIMPLE CON LOS DATOS DE LA CONEXION,  LIMITES DE LAS CONEXIONES Y LO REGRESA A LA VARIABLE __pool
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

                logger.info(f"Creacion del pool de conexiones exitoso: {cls.__pool}")
                return cls.__pool

            except Exception as excepcion:
                logger.error(f"ERROR, al crear un pool de conexiones: {excepcion}")
                sys.exit()
        else:
            return cls.__pool

    # EL METODO obtenerConexion REGRESA UN OBJETO CONEXION DEL POOL DE CONEXIONES
    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()
        logger.debug(f"Conexion exitosa: {conexion}")
        return conexion
        
    # EL METODO liberarConexion LIBERAMOS UNA CONEXION AL POOL DE CONEXIONES
    @classmethod
    def liberarConexion(cls, conexion):
        cls.obtenerPool().putconn(conexion)
        logger.debug(f"Se libera la conexion al pool: {conexion}")
        logger.debug(f"Estado del pool: {cls.__pool}")

    # EL METODO cerrarConexiones CIERRA TODAS LAS CONEXIONES DEL POOL
    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall()
        logger.info(f"Conexiones del pool cerradas: {cls.__pool}")

# PRUEBA DE CONFIGURACION (SOLO SE EJECUTARA CUANDO SE EJECUTE ESTE MODULO)
if __name__ == "__main__":
    # OBTENIENDO CONEXIONES DE UN POOL
    conexion1 = Conexion.obtenerConexion()
    conexion2 = Conexion.obtenerConexion()
    # LIBERANDO ESAS CONEXIONES AL POOL
    Conexion.liberarConexion(conexion1)
    Conexion.liberarConexion(conexion2)
    
    conexion3 = Conexion.obtenerConexion()
    Conexion.cerrarConexiones()
    #conexion3 = Conexion.obtenerConexion() # ERROR, POOL DE CONEXIONES CERRADA
