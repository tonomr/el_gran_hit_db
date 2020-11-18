from services.logger_conf import logger
from services.conexion import Conexion
from views.gui import GUI

import tkinter

if __name__ == '__main__':

    # Tkinter
    root = tkinter.Tk()
    root.geometry("600x400")
    # Menu principal de Tkinter
    GUI(root)
    # Ventana Menu de videojuegos
    # GameWindow(root)
    # Ventana Agrega Juego
    # AddGameWindow(root)
    root.mainloop()
