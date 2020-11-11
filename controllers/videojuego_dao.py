# CLASE VIDEOJUEGO DAO (DATA ACCESS OBJECT) PARA ADMINISTRAR LOS DATOS DE LA BASE DE DATOS

from models.videojuego import Videojuego # IMPORTAMOS LA CLASE VIDEOJUEGO
from services.cursor import CursorDelPool # IMPORTAMOS EL CURSOR DEL POOL DE CONEXIONES
from services.logger_conf import logger # IMPORTAMOS EL LOGGER

# LA CLASE VIDEOJUEGODAO CONTIENE LAS CONSTANTES PARA HACER LAS CONSULTAS A LA BASE DE DATOS Y SUS RESPECTIVOS METODOS PARA MOSTRARLAS AL USUARIO
class VideojuegoDao:
    # SENTENCIAS
    __SELECT = "SELECT * FROM videojuego"
    __INSERT = "INSERT INTO videojuego(nombre_juego, estado, cantidad, clasificacion, descripcion, precio, fecha_publicacion, codigo_desarrolladora) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
    __UPDATE = "UPDATE videojuego SET nombre_juego = %s, estado = %s, cantidad = %s, clasificacion = %s, descripcion = %s, precio = %s, fecha_publicacion = %s, codigo_desarrolladora = %s WHERE id_juego = %s"
    __DELETE = "DELETE FROM videojuego WHERE id_juego = %s"
    
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
                videojuego = Videojuego(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5], registro[6], registro[7], registro[8])
                videojuegos.append(videojuego)

            return videojuegos # RETORNAMOS LA LISTA
    
    # METODO INSERTAR PARA AGREGAR REGISTROS
    @classmethod
    def insertar(cls, videojuego):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__INSERT)) # SENTENCIA A EJECUTAR
            logger.debug(f"Videojuego a insertar: {videojuego}") # OBJETO videojuego A INSERTAR
            values = (videojuego.getNombreJuego(), videojuego.getEstado(), videojuego.getCantidad(), videojuego.getClasificacion(), videojuego.getDescripcion(), videojuego.getPrecio(), videojuego.getFechaPublicacion(), videojuego.getCodigoDesarrolladora())
            cursor.execute(cls.__INSERT, values) # EJECUCION DE LA SENTENCIA
            
            return cursor.rowcount # RETORNAMOS EL NUMERO DE INSERCIONES
        
    # METODO ACTUALIZAR PARA MODIFICAR REGISTROS
    @classmethod
    def actualizar(cls, videojuego):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__UPDATE)) # SENTENCIA A EJECUTAR
            logger.debug(f"Videojuego a actualizar: {videojuego}") # SE IMPRIME EL OBJETO videojuego A ACTUALIZAR
            values = (videojuego.getNombreJuego(), videojuego.getEstado(), videojuego.getCantidad(), videojuego.getClasificacion(), videojuego.getDescripcion(), videojuego.getPrecio(), videojuego.getFechaPublicacion(), videojuego.getCodigoDesarrolladora(), videojuego.getIdJuego())
            cursor.execute(cls.__UPDATE, values) # EJECUCION DE LA SENTENCIA
            
            return cursor.rowcount # RETORNAMOS EL NUMERO DE ACTUALIZACIONES
        
    # METODO ELIMINAR PARA BORRAR REGISTROS
    @classmethod
    def eliminar(cls, videojuego):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__DELETE)) # SENTENCIA A EJECUTAR
            logger.debug(f"Videojuego a eliminar: {videojuego}") # SE IMPRIME EL OBJETO videojuego A ELIMINAR
            values = (videojuego.getIdJuego(),)
            cursor.execute(cls.__DELETE, values) # EJECUCION DE LA SENTENCIA
            
            return cursor.rowcount # RETORNAMOS EL NUMERO DE ELIMINACIONES

# SIMULACIONES (SOLO SE EJECUTARA CUANDO SE EJECUTE ESTE MODULO)
if __name__ == "__main__":
    # PRUEBA SELECT
    videojuegos = VideojuegoDao.seleccionar()
    # POR CADA REGISTRO EN LA LISTA videojuegos IMPRIMIR CON SU METODO STR
    for videojuego in videojuegos:
        logger.debug(videojuego)
    #    logger.debug(videojuego.getIdJuego()) # SE PUEDE IMPRIMIR LOS CAMPOS POR SEPARADO
    
    # PRUEBA INSERT
    #videojuego = Videojuego(nombre_juego="Mario Bros 2", estado="Nuevo", cantidad=33, clasificacion="E", descripcion="Juego clasico de plataformas de los 80s", precio=150.50, fecha_publicacion="2/5/1985", codigo_desarrolladora=1)
    #registros_insertados = VideojuegoDao.insertar(videojuego)
    #logger.debug(f"Registros insertados: {registros_insertados}")
    
    #PRUEBA UPDATE
    #videojuego = Videojuego(2, "Mario Bros 3", "Usado", 45, "EE", "Juego clasico de plataformas de los 90s", 200.50, "2/5/1995", 1)
    #registros_actualizados = VideojuegoDao.actualizar(videojuego)
    #logger.debug(f"Registros actualizados: {registros_actualizados}")
    
    #PRUEBA DELETE
    #videojuego = Videojuego(id_juego=2)
    #registros_eliminados = VideojuegoDao.eliminar(videojuego)
    #logger.debug(f"Registros eliminados: {registros_eliminados}")
