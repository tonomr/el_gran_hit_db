# PROYECTO PARA SEMINARIO DE BASE DE DATOS "EL GRAN HIT"

## Instalación
- SE CREO UNA BASE DE DATOS EN POSTGRES LLAMADA el_gran_hit_db CON UNA TABLA articulos AGREGANDO DOS REGISTROS DESDE AHI.

## Servicios
- EL ARCHIVO logger_conf.py ES UN ARCHIVO DE CONFIGURACION QUE ESCRIBE EN LA TERMINAL Y EN UN ARCHIVO LOS EVENTOS QUE OCURREN EN NUESTRO PROYECTO, YA SEAN ERRORES O INFORMACION DE COMO SE EJECUTA EL PROGRAMA. SE PUEDE CONFIGURAR EL FORMATO DE ESTOS EVENTOS Y EL NIVEL QUE SE DESEA VISUALIZAR. EL MODO DEBUG ESTA PUESTO PORQUE EL PROYECTO ESTA EN DESARROLLO, CUANDO SE FINALIZE SE PUEDE CAMBIAR A WARNING O INCLUSO A ERROR PARA QUE SOLO MUESTRE EVENTOS DE ESA MAGNITUD.

- EL ARCHIVO conexion.py ES EL ARCHIVO QUE GUARDAR LOS DATOS PARA LA CONEXION A LA BASE DE DATOS Y CREAR UN POOL DE CONEXIONES PARA QUE NO ESTE LIMITADA A UNA CONEXION PARA TODOS LOS USUARIOS, ESTA CONFIGURADA PARA UNA BASE DE DATOS LLAMADA el_gran_hit_db CON USUARIO postgres, CONTRASEÑA admin, HOST 5433 Y UN PUERTO localhost.

- EL ARCHIVO cursor.py SE USA PARA CREAR OBJETOS DE CONEXION Y CURSOR PARA PODER EJECUTAR SENTENCIAS, HACER CONSULTAS Y DEPENDIENDO DEL RESULTADO, HACER COMMIT DE LAS TRANSACCIONES O ROLLBACK DE LAS MISMAS.

## Controladores
- EL ARCHIVO videojuego.py ES LA CLASE VIDEOJUEGO PARA LA ENTIDAD articulo DE LA BASE DE DATOS. AQUI SE ENCUENTRAN LOS ATRIBUTOS DE LA CLASE O ENTIDAD, SUS METODOS CONSTRUCTORES, STR, GETTERS Y SETTERS.

- EL ARCHIVO videojuego_dao.py ES PARA MANIPULAR LOS DATOS DE LA BASE DE DATOS EN BASE A LA CLASE VIDEOJUEGOS. AQUI SE ENCUENTRAN LOS METODOS PARA HACER SELECT, INSERT, UPDATE Y DELETE DE LA TABLA articulo.

- EL ARCHIVO menu_app.py ES EL MENU PARA EL USUARIO, LE DA LAS OPCIONES PARA LAS CONSULTAS DE LA BASE DE DATOS Y LAS IMPRIME EN TERMINAL.
