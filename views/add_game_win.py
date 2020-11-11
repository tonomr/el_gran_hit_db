from tkinter import *
from tkinter import ttk
from views.menubar import Menubar

from models.videojuego import Videojuego
from controllers.videojuego_dao import VideojuegoDao

class AddGameWindow(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.init_gui()

    def add_game(self):
        nombre = self.game_name.get()
        categoria = self.game_category.get()
        desarrolladora = self.game_developer.get()
        precio = self.game_price.get()
        nombre = self.game_name.get()
        videojuego = Videojuego(nombre, categoria, desarrolladora, precio)
        registros_insertados = VideojuegoDao.insertar(videojuego)
        
        
    def init_gui(self):
        self.root.title("Agregar un videojuego")
        self.root.geometry("600x600")
        #self.grid_columnconfigure(0, weight=1)
        #self.grid_columnconfigure(2, weight=1)

        self.name_label = ttk.Label(self.root, text="Nombre del videojuego")
        self.game_name = ttk.Entry(self.root, width=50)
        self.category_label = ttk.Label(self.root, text="Categoría")
        self.game_category = ttk.Entry(self.root, width=50)
        self.developer_label = ttk.Label(self.root, text="Desarrolladora")
        self.game_developer = ttk.Entry(self.root, width=50)
        self.price_label = ttk.Label(self.root, text="Precio")
        self.game_price = ttk.Entry(self.root, width=10)

        self.btn_games = ttk.Button(self.root, text='Agregar', width=30, command=self.add_game)

        self.name_label.grid(row=0, column=0)
        self.game_name.grid(row=0, column=2, sticky=("we"))
        self.category_label.grid(row=1, column=0)
        self.game_category.grid(row=1, column=2, sticky=("we"))
        self.developer_label.grid(row=2, column=0)
        self.game_developer.grid(row=2, column=2, sticky=("we"))
        self.price_label.grid(row=3, column=0)
        self.game_price.grid(row=3, column=2, sticky=("we"))

        self.btn_games.grid(row=19, column=2, sticky=("we"))
       
        #self.btn_employees = ttk.Button(self, text='Ver todos los juegos', width=30, command=self.employees_window)
        #self.btn_customers = ttk.Button(self, text='Modificar juego', width=30, command=self.customer_window)
        #self.btn_shippings = ttk.Button(self, text='eliminarjuego', width=30, command=self.shippings_window)

if __name__ == '__main__':
    root = tkinter.Tk()
    AddGameWindow(root)
    root.mainloop()
