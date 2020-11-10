# PRUEBA DE CONEXION A UNA BASE DE DATOS DE POSTGRES

# SE IMPORTA LA LIBRERIA psycopg2 (INSTALAR ANTES CON LA HERRAMIENTA pip)
import psycopg2

# OBJETO CONEXION PARA LA BASE DE DATOS
conexion = psycopg2.connect(user='postgres',
                            password='admin',
                            host='127.0.0.1',
                            port='5433',
                            database='el_gran_hit_db')

# OBJETO CURSOR PARA EJECUTAR SENTENCIAS USANDO EL OBJETO CONEXION
cursor = conexion.cursor()

# SENTECIA A EJECUTAR
sql = "SELECT codigo, nombre, categoria, precio, descripcion, clasificacion, copias, to_char(publicacion, 'DD-MM-YYYY'), estado, desarrolladora FROM articulo"
cursor.execute(sql)

# SE GUARDAN LOS REGISTROS EN ESTA VARIABLE CON UN fetchall
registros = cursor.fetchall()

# SE IMPRIMEN LOS REGISTROS
print(registros)

# CERRAMOS CONEXIONES
cursor.close()
conexion.close()
