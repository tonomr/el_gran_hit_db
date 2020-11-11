from models.videojuego import Videojuego
from controllers.videojuego_dao import VideojuegoDao
from services.logger_conf import logger
from services.conexion import Conexion
from views.gui import GUI
from views.menubar import Menubar
from views.add_game_win import AddGameWindow
from views.game_window import GameWindow
import tkinter

if __name__ == '__main__':

    # Tkinter
    root = tkinter.Tk()
    # Menu principal de Tkinter
    GUI(root)
    # Ventana Menu de videojuegos
    # GameWindow(root)
    # Ventana Agrega Juego
    # AddGameWindow(root)
    root.mainloop()