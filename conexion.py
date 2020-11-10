# CONFIGURACION PARA LA CONEXION A LA BASE DE DATOS

from logger_conf import logger # DE NUESTRA CONFIGURACION DE LOGGER IMPORTAMOS LA DEFINICION
import psycopg2 as db # MODULO PARA LA CONEXION PYTHON CON POSTGRESQL
import sys # MODULO PARA TERMINAR LA EJECUCION DEL PROGRAMA SI HAY ERROR

# CLASE CONEXION, DATOS DE LA CONEXION Y LOS OBJETOS CONEXION Y CURSOR
class Conexion:
    __DATABASE = "el_gran_hit_db"
    __USERNAME = "postgres"
    __PASSWORD = "admin"
    __PORT = "5433"
    __HOST = "127.0.0.1"
    __conexion = None
    __cursor = None
    
    # EL METODO obtenerConexion REGRESA UN OBJETO CONEXION SI ES POSIBLE CONECTAR A LA BASE DE DATOS, SINO, TERMINA EL PROGRAMA
    @classmethod
    def obtenerConexion(cls):
        if cls.__conexion is None:
            try:
                cls.__conexion = db.connect(user = cls.__USERNAME,
                                            password = cls.__PASSWORD,
                                            host = cls.__HOST,
                                            port = cls.__PORT,
                                            database = cls.__DATABASE)
                logger.debug(f"Conexion Exitosa: {cls.__conexion}")
                return cls.__conexion
                
            except Exception as excepcion:
                logger.error(f"ERROR, Conexion a la base de datos fallo: {excepcion}")
                sys.exit()
        
        else:
            return cls.__conexion
    
    # EL METODO obtenerCursosr REGRESA UN CURSOR A PARTIR DE UNA CONEXION, SINO SE CREA EL CURSOR, TERMINA EL PROGRAMA
    @classmethod
    def obtenerCursor(cls):
        if cls.__cursor is None:
            try:
                cls.__cursor = cls.obtenerConexion().cursor()
                logger.debug(f"Cursor Exitoso: {cls.__cursor}")
                return cls.__cursor
            
            except Exception as excepcion:
                logger.error(f"ERROR, Cursor de la conexion fallo: {excepcion}")
                sys.exit()

        else:
            return cls.__cursor
    
    # EL METODO cerrarConexiones CIERRA LA CONEXION Y EL CURSOR SI ES QUE EXISTEN, SINO, IMPRIME ERROR
    @classmethod
    def cerrarConexiones(cls):
        if cls.__cursor is not None:
            try:
                cls.__cursor.close()
                
            except Exception as excepcion:
                logger.error(f"ERROR, Cerrar cursor fallo: {excepcion}")
        
        if cls.__conexion is not None:
            try:
                cls.__conexion.close()
                
            except Exception as excepcion:
                logger.error(f"ERROR, Cerrar conexion fallo: {excepcion}")
        
        logger.debug(f"Conexiones cerradas con exito")
            

# PRUEBA DE CONFIGURACION (SOLO SE EJECUTARA CUANDO SE EJECUTE ESTE MODULO)
if __name__ == "__main__":
    logger.info(Conexion.obtenerCursor())
    Conexion.cerrarConexiones()
