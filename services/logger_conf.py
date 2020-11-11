# CONFIGURACION PARA NUESTRO ARCHIVO LOG

# SE IMPORTA LA LIBRERIA logging
import logging

# DEFINICION DE logger PARA EL PROYECTO
logger = logging

# CONFIGURACION DEL LOGGER
logger.basicConfig(level=logging.DEBUG,
                   format="%(asctime)s: %(levelname)s [%(filename)s: %(lineno)s] %(message)s",
                   datefmt="%I:%M:%S %p",
                   handlers=[
                       logging.FileHandler("reports.log"),
                       logging.StreamHandler()
                   ])

# PRUEBA DE CONFIGURACION (SOLO SE EJECUTARA CUANDO SE EJECUTE ESTE MODULO)
if __name__ == "__main__":
    logging.debug("Mensaje a nivel DEBUG")
    logging.info("Mensaje a nivel INFO")
    logging.warning("Mensaje a nivel WARNING")
    logging.error("Mensaje a nivel ERROR")
