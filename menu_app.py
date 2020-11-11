# MENU PARA EL USUARIO PARA LA TABLA ARTICULO

from models.videojuego import Videojuego
from controllers.videojuego_dao import VideojuegoDao
from services.logger_conf import logger
#from views.mainmenu import GUI

opcion = None

while opcion != "5":
    print("Opciones:\n"
          "1. Listar videojuegos\n"
          "2. Insertar videojuego\n"
          "3. Actualizar videojuego\n"
          "4. Eliminar videojuego\n"
          "5. Salir")
    
    opcion = input("Escribe tu opcion (1-5): ")
    
    if opcion == "1":
        videojuegos = VideojuegoDao.seleccionar()
        
        for videojuego in videojuegos:
            print(videojuego)
    
    elif opcion == "2":
        nombre_juego = input("Escribe el NOMBRE: ")
        estado = input("Escribe el ESTADO: ")
        cantidad = int(input("Escribe la CANTIDAD: "))
        clasificacion = input("Escribe la CLASIFICACION: ")
        descripcion = input("Escribe la DESCRIPCION: ")
        precio = float(input("Escribe el PRECIO: "))        
        fecha_publicacion = input("Escribe la FECHA de PUBLICACION: ")
        codigo_desarrolladora = input("Escribe el CODIGO de la DESARROLLADORA: ")
        
        videojuego = Videojuego(nombre_juego=nombre_juego, estado=estado, cantidad=cantidad, clasificacion=clasificacion, descripcion=descripcion, precio=precio, fecha_publicacion=fecha_publicacion, codigo_desarrolladora=codigo_desarrolladora)
        registros_insertados = VideojuegoDao.insertar(videojuego)
        
        print(f"Registros insertados: {registros_insertados}")
    
    elif opcion == "3":
        id_juego = input("Escribe el ID del videojuego: ")
        nombre_juego = input("Escribe el nuevo NOMBRE: ")
        estado = input("Escribe el nuevo ESTADO: ")
        cantidad = int(input("Escribe la nueva CANTIDAD: "))
        clasificacion = input("Escribe la nueva CLASIFICACION: ")
        descripcion = input("Escribe la nueva DESCRIPCION: ")
        precio = float(input("Escribe el nuevo PRECIO: "))        
        fecha_publicacion = input("Escribe la nueva FECHA de PUBLICACION: ")
        codigo_desarrolladora = input("Escribe el nuevo CODIGO de la DESARROLLADORA: ")
        
        videojuego = Videojuego(id_juego, nombre_juego, estado, cantidad, clasificacion, descripcion, precio, fecha_publicacion, codigo_desarrolladora)
        registros_actualizados = VideojuegoDao.actualizar(videojuego)
        
        print(f"Registros actualizados: {registros_actualizados}")
        
    elif opcion == "4":
        id_juego = input("Escribe el ID del videojuego: ")
        
        videojuego = Videojuego(id_juego=id_juego)
        registros_eliminados = VideojuegoDao.eliminar(videojuego)
        
        print(f"Registros eliminados: {registros_eliminados}")
    
else:
    print("Saliendo del programa...")
    input()

