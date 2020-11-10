# MENU PARA EL USUARIO PARA LA TABLA ARTICULO

from videojuego import Videojuego
from videojuego_dao import VideojuegoDao
from logger_conf import logger

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
        codigo = input("Escribe el CODIGO: ")
        nombre = input("Escribe el NOMBRE: ")
        precio = float(input("Escribe el PRECIO: "))
        categoria = input("Escribe la CATEGORIA: ")
        descripcion = input("Escribe la DESCRIPCION: ")
        clasificacion = input("Escribe la CLASIFICACION: ")
        copias = int(input("Escribe la cantidad de COPIAS: "))
        publicacion = input("Escribe la fecha de PUBLICACION: ")
        estado = input("Escribe el ESTADO: ")
        desarrolladora = input("Escribe la DESARROLLADORA: ")
        
        videojuego = Videojuego(codigo, nombre, categoria, precio, descripcion, clasificacion, copias, publicacion, estado, desarrolladora)
        registros_insertados = VideojuegoDao.insertar(videojuego)
        
        print(f"Registros insertados: {registros_insertados}")
    
    elif opcion == "3":
        codigo = input("Escribe el CODIGO del videojuego: ")
        nombre = input("Escribe el nuevo NOMBRE: ")
        precio = float(input("Escribe el nuevo PRECIO: "))
        categoria = input("Escribe la nueva CATEGORIA: ")
        descripcion = input("Escribe la nueva DESCRIPCION: ")
        clasificacion = input("Escribe la nueva CLASIFICACION: ")
        copias = int(input("Escribe la nueva cantidad de COPIAS: "))
        publicacion = input("Escribe la nueva fecha de PUBLICACION: ")
        estado = input("Escribe el nuevo ESTADO: ")
        desarrolladora = input("Escribe la nueva DESARROLLADORA: ")
        
        videojuego = Videojuego(codigo, nombre, categoria, precio, descripcion, clasificacion, copias, publicacion, estado, desarrolladora)
        registros_actualizados = VideojuegoDao.actualizar(videojuego)
        
        print(f"Registros actualizados: {registros_actualizados}")
        
    elif opcion == "4":
        codigo = input("Escribe el CODIGO del videojuego: ")
        
        videojuego = Videojuego(codigo=codigo)
        registros_eliminados = VideojuegoDao.eliminar(videojuego)
        
        print(f"Registros eliminados: {registros_eliminados}")
    
else:
    print("Saliendo del programa...")
    input()

