# CLASE VIDEOJUEGO DAO (DATA ACCESS OBJECT) PARA ADMINISTRAR LOS DATOS DE LA BASE DE DATOS

from models.videojuego import Videojuego # IMPORTAMOS LA CLASE VIDEOJUEGO
from services.cursor import CursorDelPool # IMPORTAMOS EL CURSOR DEL POOL DE CONEXIONES
from services.logger_conf import logger # IMPORTAMOS EL LOGGER

# LA CLASE VIDEOJUEGODAO CONTIENE LAS CONSTANTES PARA HACER LAS CONSULTAS A LA BASE DE DATOS Y SUS RESPECTIVOS METODOS PARA MOSTRARLAS AL USUARIO
class VideojuegoDao:
    # SENTENCIAS
    __SELECT = "SELECT * FROM videojuegos ORDER BY id_videojuego"
    __INSERT = "INSERT INTO videojuegos(nombre_videojuego, estado_videojuego, cantidad_videojuego, clasificacion_videojuego, descripcion_videojuego, precio_videojuego, publicacion_videojuego, codigo_desarrolladora) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
    __UPDATE = "UPDATE videojuegos SET nombre_videojuego = %s, estado_videojuego = %s, cantidad_videojuego = %s, clasificacion_videojuego = %s, descripcion_videojuego = %s, precio_videojuego = %s, publicacion_videojuego = %s, codigo_desarrolladora = %s WHERE id_videojuego = %s"
    __DELETE = "DELETE FROM videojuegos WHERE id_videojuego = %s"
    __SEARCH = "SELECT * FROM videojuegos WHERE nombre_videojuego LIKE %s"
    __SELECT_ONE =  "SELECT * FROM videojuegos WHERE id_videojuego = %s"
    __SELECT_NOMBRE = "SELECT nombre_videojuego FROM videojuegos WHERE id_videojuego = %s"

    listadoVideojuegos = None
    
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
            #logger.debug(f"Videojuego a insertar: {videojuego}") # OBJETO videojuego A INSERTAR
            values = (videojuego.get_nombre_videojuego(), videojuego.get_estado_videojuego(), videojuego.get_cantidad_videojuego(), videojuego.get_clasificacion_videojuego(), videojuego.get_descripcion_videojuego(), videojuego.get_precio_videojuego(), videojuego.get_publicacion_videojuego(), videojuego.get_codigo_desarrolladora())
            cursor.execute(cls.__INSERT, values) # EJECUCION DE LA SENTENCIA
            
            return cursor.rowcount # RETORNAMOS EL NUMERO DE INSERCIONES
        
    # METODO ACTUALIZAR PARA MODIFICAR REGISTROS
    @classmethod
    def actualizar(cls, videojuego):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__UPDATE)) # SENTENCIA A EJECUTAR
            
            values = (videojuego.get_nombre_videojuego(), videojuego.get_estado_videojuego(), videojuego.get_cantidad_videojuego(), videojuego.get_clasificacion_videojuego(), videojuego.get_descripcion_videojuego(), videojuego.get_precio_videojuego(), videojuego.get_publicacion_videojuego(), videojuego.get_codigo_desarrolladora(), videojuego.get_id_videojuego())
            cursor.execute(cls.__UPDATE, values) # EJECUCION DE LA SENTENCIA
            
            return cursor.rowcount # RETORNAMOS EL NUMERO DE ACTUALIZACIONES
        
    # METODO ELIMINAR PARA BORRAR REGISTROS
    @classmethod
    def eliminar(cls, videojuego):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__DELETE)) # SENTENCIA A EJECUTAR
            values = (videojuego.get_id_videojuego(),)
            cursor.execute(cls.__DELETE, values) # EJECUCION DE LA SENTENCIA
            
            return cursor.rowcount # RETORNAMOS EL NUMERO DE ELIMINACIONES

    @classmethod
    def buscar(cls, key_word):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__SEARCH))
            values = (key_word,)
            cursor.execute(cls.__SEARCH, values)
            registros = cursor.fetchall()

            videojuegos = []
            for registro in registros:
                videojuego = Videojuego(registro[0], registro[1], registro[2], registro[3],
                                        registro[4], registro[5], registro[6], registro[7], registro[8])
                videojuegos.append(videojuego)
            
            return videojuegos

    # Método que recupera el videjuego con el ID que recibe
    @classmethod
    def recuperar(cls, id):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__SELECT_ONE))
            values = (id,)
            cursor.execute(cls.__SELECT_ONE, values)
            registro = cursor.fetchone()
        
            videojuego = Videojuego(registro[0], registro[1], registro[2], registro[3],
                                        registro[4], registro[5], registro[6], registro[7], registro[8])
            return videojuego

    # ESTE METODO RECIBE UN ID DE DESARROLLADORA PARA DEVOLVER MEDIANTE UNA BUSQUEDA EL NOMBRE DE TAL
    """     
    @classmethod
    def buscarNombre(cls, id_busqueda):
        nombre_encontrado = None
        if cls.listadoVideojuegos == None:
            cls.listadoVideojuegos = VideojuegoDao.seleccionar()
        for videojuego in cls.listadoVideojuegos:
            if videojuego.get_id_videojuego() == id_busqueda:
                nombre_encontrado = videojuego.get_nombre_videojuego()
                break
        return nombre_encontrado
    """

    # Método que recupera el nombre del videjuego con el ID que recibe
    @classmethod
    def buscar_nombre(cls, id):
        with CursorDelPool() as cursor:
            #logger.debug(cursor.mogrify(cls.__SELECT_NOMBRE))
            values = (id,)
            cursor.execute(cls.__SELECT_NOMBRE, values)
            registro = cursor.fetchone()
            return registro

# SIMULACIONES (SOLO SE EJECUTARA CUANDO SE EJECUTE ESTE MODULO)
if __name__ == "__main__":
    # PRUEBA SELECT
    videojuegos = VideojuegoDao.seleccionar()
    # POR CADA REGISTRO EN LA LISTA videojuegos IMPRIMIR CON SU METODO STR
    for videojuego in videojuegos:
        logger.debug(videojuego)
    #    logger.debug(videojuego.get_id_videojuego()) # SE PUEDE IMPRIMIR LOS CAMPOS POR SEPARADO
    
    # PRUEBA INSERT
    #videojuego = Videojuego(nombre_videojuego="Mario Bros 2", estado_videojuego="Nuevo", cantidad_videojuego=33, clasificacion_videojuego="E", descripcion_videojuego="Juego clasico de plataformas de los 80s", precio_videojuego=150.50, publicacion_videojuego="2/5/1985", codigo_desarrolladora=1)
    #registros_insertados = VideojuegoDao.insertar(videojuego)
    #logger.debug(f"Registros insertados: {registros_insertados}")
    
    #PRUEBA UPDATE
    #videojuego = Videojuego(3, "Mario Bros 3", "Usado", 45, "EE", "Juego clasico de plataformas de los 90s", 200.50, "2/5/1995", 1)
    #registros_actualizados = VideojuegoDao.actualizar(videojuego)
    #logger.debug(f"Registros actualizados: {registros_actualizados}")
    
    #PRUEBA DELETE
    #videojuego = Videojuego(id_videojuego=3)
    #registros_eliminados = VideojuegoDao.eliminar(videojuego)
    #logger.debug(f"Registros eliminados: {registros_eliminados}")
