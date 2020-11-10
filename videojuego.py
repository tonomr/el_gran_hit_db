# CLASE VIDEOJUEGO PARA LA ENTIDAD DE LA BASE DE DATOS

from logger_conf import logger # DE NUESTRA CONFIGURACION DE LOGGER IMPORTAMOS LA DEFINICION

# VIDEOJUEGO CONTIENE SU CONSTRUCTOR CON LOS ATRIBUTOS DE LA ENTIDAD, SU METODO STR Y SUS GET Y SET
class Videojuego:
    # CONSTRUCTOR DE LA CLASE
    def __init__(self, codigo=None, nombre=None, categoria=None, precio=None, descripcion=None, clasificacion=None, copias=None, publicacion=None, estado=None, desarrolladora=None):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__categoria = categoria
        self.__precio = precio
        self.__descripcion = descripcion
        self.__clasificacion = clasificacion
        self.__copias = copias
        self.__publicacion = publicacion
        self.__estado = estado
        self.__desarrolladora = desarrolladora
        
    # METODO STR DE LA CLASE
    def __str__(self):
        return (f"Codigo: {self.__codigo}, "
                f"Nombre: {self.__nombre}, "
                f"Categoria: {self.__categoria}, "
                f"Precio: {self.__precio}, "
                f"Descripcion: {self.__descripcion}, "
                f"Clasificacion: {self.__clasificacion}, "
                f"Copias: {self.__copias}, "
                f"Publicacion: {self.__publicacion}, "
                f"Estado: {self.__estado}, "
                f"Desarrolladora: {self.__desarrolladora}")
    
    # METODOS GET DE LA CLASE
    def getCodigo(self):
        return self.__codigo
    def getNombre(self):
        return self.__nombre
    def getCategoria(self):
        return self.__categoria
    def getPrecio(self):
        return self.__precio
    def getDescripcion(self):
        return self.__descripcion
    def getClasificacion(self):
        return self.__clasificacion
    def getCopias(self):
        return self.__copias
    def getPublicacion(self):
        return self.__publicacion
    def getEstado(self):
        return self.__estado
    def getDesarrolladora(self):
        return self.__desarrolladora
    
    # METODOS SET DE LA CLASE
    def setCodigo(self, codigo):
        self.__codigo = codigo
    def setNombre(self, nombre):
        self.__nombre = nombre
    def setCategoria(self, categoria):
        self.__categoria = categoria
    def setPrecio(self, precio):
        self.__precio = precio
    def setDescripcion(self, descripcion):
        self.__descripcion = descripcion
    def setClasificacion(self, clasificacion):
        self.__clasificacion = clasificacion
    def setCopias(self, copias):
        self.__copias = copias
    def setPublicacion(self, publicacion):
        self.__publicacion = publicacion
    def setEstado(self, estado):
        self.__estado = estado
    def setDesarrolladora(self, desarrolladora):
        self.__desarrolladora = desarrolladora

# PRUEBA DE CONFIGURACION (SOLO SE EJECUTARA CUANDO SE EJECUTE ESTE MODULO)
if __name__ == "__main__":
    videojuego1 = Videojuego("ASD123F4", "Bioshock", "Shooter", 500.00, "Disparos en primera persona submarino.", "M", 100, "9/4/2008", "Nuevo", "2K Games")
    logger.debug(videojuego1)
    videojuego2 = Videojuego(nombre="Age of Empires", desarrolladora="Microsoft Games")
    logger.debug(videojuego2)
