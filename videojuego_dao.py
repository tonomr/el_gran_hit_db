# CLASE VIDEOJUEGO DAO (DATA ACCESS OBJECT) PARA ADMINISTRAR LOS DATOS DE LA BASE DE DATOS

from videojuego import Videojuego # IMPORTAMOS LA CLASE VIDEOJUEGO
from conexion import Conexion # IMPORTAMOS LA CONEXION
from logger_conf import logger # IMPORTAMOS EL LOGGER

# LA CLASE VIDEOJUEGODAO CONTIENE LAS CONSTANTES PARA HACER LAS CONSULTAS A LA BASE DE DATOS Y SUS RESPECTIVOS METODOS PARA MOSTRARLAS AL USUARIO
class VideojuegoDao:
    # SENTENCIAS
    __SELECT = "SELECT * FROM articulo"
    __INSERTAR = "INSERT INTO articulo(codigo, nombre, categoria, precio, descripcion, clasificacion, copias, publicacion, estado, desarrolladora) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    
    # METODO SELECT PARA MOSTRAR LOS REGISTROS DE LA TABLA VIDEOJUEGOS
    @classmethod
    def seleccionar(cls):
        cursor = Conexion.obtenerCursor()
        logger.debug(cursor.mogrify(cls.__SELECT)) # SENTENCIA A EJECUTAR
        cursor.execute(cls.__SELECT) # EJECUCION DE LA SENTENCIA
        registros = cursor.fetchall() # GUARDAMOS LOS REGISTROS
        
        videojuegos = [] # DEFINICION DE UNA LISTA PARA IMPRIMIR LOS RESULTADOS
        # POR CADA REGISTRO GUARDADO EN REGISTROS, AGREGARLO A LA LISTA videojuegos COMO OBJETOS
        for registro in registros:
            videojuego = Videojuego(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5], registro[6], registro[7], registro[8], registro[9])
            videojuegos.append(videojuego)

        Conexion.cerrarConexiones() # CERRAMOS LA CONEXIONES
        return videojuegos # RETORNAMOS LA LISTA
    
    # METODO INSERTAR PARA AGREGAR REGISTROS
    @classmethod
    def insertar(cls, videojuego):
        try:
            conexion = Conexion.obtenerConexion() # OBTENEMOS EL OBJETO CONEXION PARA PODER HACER UN commit O rollback
            cursor = Conexion.obtenerCursor() # OBTENEMOS EL OBJETO CURSOR PARA EJECUTAR SENTENCIAS
            logger.debug(cursor.mogrify(cls.__INSERTAR)) # SENTENCIA A EJECUTAR
            logger.debug(f"Videojuego a insertar: {videojuego}") # SE IMPRIME EL OBJETO videojuego A INSERTAR
            valores = (videojuego.getCodigo(), videojuego.getNombre(), videojuego.getCategoria(), videojuego.getPrecio(), videojuego.getDescripcion(), videojuego.getClasificacion(), videojuego.getCopias(), videojuego.getPublicacion(), videojuego.getEstado(), videojuego.getDesarrolladora())
            cursor.execute(cls.__INSERTAR, valores) # EJECUCION DE LA SENTENCIA
            conexion.commit() # SI NO HUBO ERRORES, GUARDA LOS CAMBIOS
            return cursor.rowcount # RETORNAMOS EL NUMERO DE INSERCIONES
        
        except Exception as excepcion:
            conexion.rollback() # SI HUBO ERRORES, NO GUARDAR LOS CAMBIOS
            logger.error(f"ERROR, Insertando videojuego: {excepcion}")
            
        finally:
            Conexion.cerrarConexiones() # CERRAMOS LAS CONEXIONES SI FALLA O NO FALLA

# PRUEBA DE CONFIGURACION (SOLO SE EJECUTARA CUANDO SE EJECUTE ESTE MODULO)
if __name__ == "__main__":
    # PRUEBA SELECT
    videojuegos = VideojuegoDao.seleccionar()
    # POR CADA REGISTRO EN LA LISTA videojuegos IMPRIMIR CON SU METODO STR
    for videojuego in videojuegos:
        logger.debug(videojuego)
    #    logger.debug(videojuego.getCodigo()) # SE PUEDE IMPRIMIR LOS CAMPOS POR SEPARADO
    
    # PRUEBA INSERT
    #videojuego = Videojuego("QWE567R8", "Mario Bros 2", "Plataforma", 150.33, "Juego clasico de plataformas de los 80s", "E", 4, "2/5/1985", "Usado", "Nintendo")
    #registros_insertados = VideojuegoDao.insertar(videojuego)
    #logger.debug(f"Registros insertados: {registros_insertados}")
    