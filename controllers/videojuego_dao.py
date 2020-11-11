# CLASE VIDEOJUEGO DAO (DATA ACCESS OBJECT) PARA ADMINISTRAR LOS DATOS DE LA BASE DE DATOS

from models.videojuego import Videojuego # IMPORTAMOS LA CLASE VIDEOJUEGO
from services.cursor import CursorDelPool # IMPORTAMOS EL CURSOR DEL POOL DE CONEXIONES
from services.logger_conf import logger # IMPORTAMOS EL LOGGER

# LA CLASE VIDEOJUEGODAO CONTIENE LAS CONSTANTES PARA HACER LAS CONSULTAS A LA BASE DE DATOS Y SUS RESPECTIVOS METODOS PARA MOSTRARLAS AL USUARIO
class VideojuegoDao:
    # SENTENCIAS
    __SELECT = "SELECT * FROM articulo"
    __INSERTAR = "INSERT INTO articulo(codigo, nombre, categoria, precio, descripcion, clasificacion, copias, publicacion, estado, desarrolladora) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    __UPDATE = "UPDATE articulo SET nombre = %s, categoria = %s, precio = %s, descripcion = %s, clasificacion = %s, copias = %s, publicacion = %s, estado = %s, desarrolladora = %s WHERE codigo = %s"
    __DELETE = "DELETE FROM articulo WHERE codigo = %s"
    
    # METODO SELECT PARA MOSTRAR LOS REGISTROS DE LA TABLA VIDEOJUEGOS
    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__SELECT)) # SENTENCIA A EJECUTAR
            cursor.execute(cls.__SELECT) # EJECUCION DE LA SENTENCIA
            registros = cursor.fetchall() # GUARDAMOS LOS REGISTROS
        
            videojuegos = [] # DEFINICION DE UNA LISTA PARA IMPRIMIR LOS RESULTADOS
            # POR CADA REGISTRO GUARDADO EN REGISTROS, AGREGARLO A LA LISTA videojuegos COMO OBJETOS
            for registro in registros:
                videojuego = Videojuego(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5], registro[6], registro[7], registro[8], registro[9])
                videojuegos.append(videojuego)

            return videojuegos # RETORNAMOS LA LISTA
    
    # METODO INSERTAR PARA AGREGAR REGISTROS
    @classmethod
    def insertar(cls, videojuego):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__INSERTAR)) # SENTENCIA A EJECUTAR
            logger.debug(f"Videojuego a insertar: {videojuego}") # OBJETO videojuego A INSERTAR
            valores = (videojuego.getCodigo(), videojuego.getNombre(), videojuego.getCategoria(), videojuego.getPrecio(), videojuego.getDescripcion(), videojuego.getClasificacion(), videojuego.getCopias(), videojuego.getPublicacion(), videojuego.getEstado(), videojuego.getDesarrolladora())
            cursor.execute(cls.__INSERTAR, valores) # EJECUCION DE LA SENTENCIA
            
            return cursor.rowcount # RETORNAMOS EL NUMERO DE INSERCIONES
        
    # METODO ACTUALIZAR PARA MODIFICAR REGISTROS
    @classmethod
    def actualizar(cls, videojuego):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__UPDATE)) # SENTENCIA A EJECUTAR
            logger.debug(f"Videojuego a actualizar: {videojuego}") # SE IMPRIME EL OBJETO videojuego A ACTUALIZAR
            valores = (videojuego.getNombre(), videojuego.getCategoria(), videojuego.getPrecio(), videojuego.getDescripcion(), videojuego.getClasificacion(), videojuego.getCopias(), videojuego.getPublicacion(), videojuego.getEstado(), videojuego.getDesarrolladora(), videojuego.getCodigo())
            cursor.execute(cls.__UPDATE, valores) # EJECUCION DE LA SENTENCIA
            
            return cursor.rowcount # RETORNAMOS EL NUMERO DE ACTUALIZACIONES
        
    # METODO ELIMINAR PARA BORRAR REGISTROS
    @classmethod
    def eliminar(cls, videojuego):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__DELETE)) # SENTENCIA A EJECUTAR
            logger.debug(f"Videojuego a eliminar: {videojuego}") # SE IMPRIME EL OBJETO videojuego A ELIMINAR
            valores = (videojuego.getCodigo(),)
            cursor.execute(cls.__DELETE, valores) # EJECUCION DE LA SENTENCIA
            
            return cursor.rowcount # RETORNAMOS EL NUMERO DE ELIMINACIONES

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
    
    #PRUEBA UPDATE
    #videojuego = Videojuego("QWE567R8", "Mario Bros 3", "Plataforma", 200.87, "Juego clasico de plataformas de los 90s", "E", 4, "5/6/1995", "Semi-nuevo", "Nintendo")
    #registros_actualizados = VideojuegoDao.actualizar(videojuego)
    #logger.debug(f"Registros actualizados: {registros_actualizados}")
    
    #PRUEBA DELETE
    #videojuego = Videojuego(codigo="QWE567R8")
    #registros_eliminados = VideojuegoDao.eliminar(videojuego)
    #logger.debug(f"Registros eliminados: {registros_eliminados}")    
