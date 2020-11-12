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
        # Get input fields
        name = self.game_name.get()
        condition = self.game_condition.get()
        quantity = self.game_quantity.get()
        classification = self.game_classification.get()
        description = self.game_description.get()
        price = self.game_price.get()
        released = self.game_released.get()
        devs = self.game_devs.get()
        # Create videogame instance
        videogame = Videojuego(nombre_juego=name, estado=condition, cantidad=quantity, clasificacion=classification,
                               descripcion=description, precio=price, fecha_publicacion=released, codigo_desarrolladora=devs)
        VideojuegoDao.insertar(videogame)

    def init_gui(self):
        self.root.title("Agregar un videojuego")
        self.root.geometry("600x400")
        #self.grid_columnconfigure(0, weight=1)
        #self.grid_columnconfigure(2, weight=1)

        # Label/Input fields
        self.label_name = ttk.Label(self.root, text="Nombre del videojuego")
        self.game_name = ttk.Entry(self.root, width=50)
        # combox
        self.label_condition = ttk.Label(self.root, text="Condición")
        self.game_condition = ttk.Combobox(self.root, width=30)
        self.game_condition['values'] = ('Nuevo', 'Seminuevo', 'Usado')
        self.game_condition.state(['readonly'])

        self.label_quantity = ttk.Label(self.root, text="Cantidad")
        self.game_quantity = ttk.Entry(self.root, width=15)
        self.label_classification = ttk.Label(self.root, text="Clasificación")
        self.game_classification = ttk.Entry(self.root, width=50)
        self.label_description = ttk.Label(self.root, text="Descripción")
        self.game_description = ttk.Entry(self.root, width=50)
        self.label_price = ttk.Label(self.root, text="Precio")
        self.game_price = ttk.Entry(self.root, width=10)
        self.label_released = ttk.Label(self.root, text="Fecha de publicaión")
        self.game_released = ttk.Entry(self.root, width=10)
        self.label_devs = ttk.Label(self.root, text="Desarrolladora")
        self.game_devs = ttk.Entry(self.root, width=50)

        self.btn_games = ttk.Button(
            self.root, text='Agregar', width=30, command=self.add_game)

        self.label_name.grid(row=0, column=0)
        self.game_name.grid(row=0, column=2, sticky=("we"))
        self.label_condition.grid(row=1, column=0)
        self.game_condition.grid(row=1, column=2, sticky=("we"))
        self.label_quantity.grid(row=2, column=0)
        self.game_quantity.grid(row=2, column=2, sticky=("we"))
        self.label_classification.grid(row=3, column=0)
        self.game_classification.grid(row=3, column=2, sticky=("we"))
        self.label_description.grid(row=4, column=0)
        self.game_description.grid(row=4, column=2, sticky=("we"))
        self.label_price.grid(row=5, column=0)
        self.game_price.grid(row=5, column=2, sticky=("we"))
        self.label_released.grid(row=6, column=0)
        self.game_released.grid(row=6, column=2, sticky=("we"))
        self.label_devs.grid(row=7, column=0)
        self.game_devs.grid(row=7, column=2, sticky=("we"))

        self.btn_games.grid(row=19, column=2, sticky=("we"))

        #self.btn_employees = ttk.Button(self, text='Ver todos los juegos', width=30, command=self.employees_window)
        #self.btn_customers = ttk.Button(self, text='Modificar juego', width=30, command=self.customer_window)
        #self.btn_shippings = ttk.Button(self, text='eliminarjuego', width=30, command=self.shippings_window)


if __name__ == '__main__':
    root = tkinter.Tk()
    AddGameWindow(root)
    root.mainloop()
