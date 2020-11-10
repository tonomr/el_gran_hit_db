# CONFIGURACION PARA LA CONEXION A LA BASE DE DATOS

from logger_conf import logger # DE NUESTRA CONFIGURACION DE LOGGER IMPORTAMOS LA DEFINICION
from psycopg2 import pool  # MODULO PARA LA CONEXION PYTHON CON POSTGRESQL
import sys  # MODULO PARA TERMINAR LA EJECUCION DEL PROGRAMA SI HAY ERROR
import dotenv
import os
# CLASE CONEXION, DATOS DE LA CONEXION Y OBJETO POOL DE CONEXIONES

dotenv.load_dotenv()

class Conexion:
    __DATABASE = os.getenv("DB_NAME")
    __USERNAME = os.getenv("DB_USERNAME")
    __PASSWORD = os.getenv("DB_USER_PASSWORD")
    __PORT = os.getenv("DB_PORT")
    __HOST = os.getenv("DB_HOST")
    __MIN_CON = 1
    __MAX_CON = 5
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
        logger.debug(f"Conexiones del pool cerradas: {cls.__pool}")

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
    
