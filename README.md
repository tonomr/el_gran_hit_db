PROYECTO PARA SEMINARIO DE BASE DE DATOS "EL GRAN HIT"

SE CREO UNA BASE DE DATOS EN POSTGRES LLAMADA el_gran_hit_db CON UNA TABLA articulos AGREGANDO DOS REGISTROS DESDE AHI.

EL ARCHIVO prueba.py HACE UNA PEQUEÑA PRUEBA DE CONEXION A LA BASE DE DATOS PARA POSTERIORMENTE IMPRIMIR UNA CONSULTA SELECT DIRECTAMENTE DE LA BASE DE DATOS.

EL ARCHIVO logger_conf.py ES UN ARCHIVO DE CONFIGURACION QUE ESCRIBE EN LA TERMINAL Y EN UN ARCHIVO LOS EVENTOS QUE OCURREN EN NUESTRO PROYECTO, YA SEAN ERRORES O INFORMACION DE COMO SE EJECUTA EL PROGRAMA. SE PUEDE CONFIGURAR EL FORMATO DE ESTOS EVENTOS Y EL NIVEL QUE SE DESEA VISUALIZAR. EL MODO DEBUG ESTA PUESTO PORQUE EL PROYECTO ESTA EN DESARROLLO, CUANDO SE FINALIZE SE PUEDE CAMBIAR A WARNING O INCLUSO A ERROR PARA QUE SOLO MUESTRE EVENTOS DE ESA MAGNITUD.

EL ARCHIVO conexion.py ES EL ARCHIVO QUE GUARDA LOS DATOS PARA LA CONEXION A LA BASE DE DATOS, ESTA CONFIGURADA PARA UNA BASE DE DATOS LLAMADA el_gran_hit_db CON USUARIO postgres, CONTRASEÑA admin, HOST 5433 Y UN PUERTO localhost.

EL ARCHIVO videojuego.py ES LA CLASE VIDEOJUEGO PARA LA ENTIDAD articulo DE LA BASE DE DATOS. AQUI SE ENCUENTRAN LOS ATRIBUTOS DE LA CLASE O ENTIDAD, SUS METODOS CONSTRUCTORES, STR, GETTERS Y SETTERS.

EL ARCHIVO videojuego_dao.py ES PARA MANIPULAR LOS DATOS DE LA BASE DE DATOS EN BASE A LA CLASE VIDEOJUEGOS. AQUI SE ENCUENTRAN LOS METODOS PARA HACER SELECT, INSERT, UPDATE Y DELETE DE LA TABLA articulo.
