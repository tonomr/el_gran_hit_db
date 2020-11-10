# CONFIGURACION DE LOS CURSORES DE LA CONEXION

from conexion import Conexion
from logger_conf import logger

# CLASE CursorDelPool CON ATRIBUTOS OBJETO DE CONEXION Y CURSOR
class CursorDelPool:
    # CONSTRUCTOR DE LA CLASE
    def __init__(self):
        self.__conn = None
        self.__cursor = None
    
    # CUANDO SE LLAME ESTA CLASE CON with SE EJECUTARA ESTE METODO
    def __enter__(self):
        self.__conn = Conexion.obtenerConexion()
        self.__cursor = self.__conn.cursor()
        logger.debug(f"Cursor exitoso: {self.__cursor}")
        
        return self.__cursor
    
    # CUANDO TERMINE DE EJECUTARSE __enter__ SE EJECUTARA ESTE METODO, SI HUBO ERRORES NO SE HACE COMMIT
    def __exit__(self, exception_type, exception_value, exception_traceback):
        if exception_value:
            self.__conn.rollback()
            logger.debug(f"Ocurrio una excepcion: {exception_value}")
        
        else:
            self.__conn.commit()
            logger.debug(f"Commit de la transaccion")
            
        self.__cursor.close()
        Conexion.liberarConexion(self.__conn)

# PRUEBA DE CONFIGURACION (SOLO SE EJECUTARA CUANDO SE EJECUTE ESTE MODULO)        
if __name__ == "__main__":
    with CursorDelPool() as cursor:
        cursor.execute("SELECT * FROM articulo")
        logger.debug(cursor.fetchall())
