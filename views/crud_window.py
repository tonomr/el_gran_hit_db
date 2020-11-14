from tkinter import *
from tkinter import ttk
from services.logger_conf import logger 
from views.add_game_win import AddGameWindow
from views.menubar import *
from controllers.videojuego_dao import VideojuegoDao 
from views.index_window import IndexWindow
from models.videojuego import Videojuego

class CrudWindow(ttk.Frame):

    def __init__(self, parent, win_title, header_title, sidebar, entity_name, index_controller, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent                              # Ventana padre
        self.root.title(win_title)                      # Título de ventana
        self.header = PhotoImage(file=header_title)     # Objeto del tipo imagen
        self.sidebar = PhotoImage(file=sidebar)         # Objeto del tipo imagen
        self.entity_name = entity_name                  # El string nombre de la entidad
        self.index_controller = index_controller
        self.init_gui()                                 # Inicia el grid y los widgets

    # Create a new Videogame
    def create_window(self):
      pass
    # Show all VideoGames
    def index_window(self):
        self.index_controller()
        pass
    
    # Edit a videogame
    def edit_window(self):
        pass
    
    # Delete a videogame
    def destroy_window(self):
        pass

    
    

    def init_gui(self):
        self.grid_forget()
        self.root.geometry("600x400")
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=0)

        # Image/Sidebar widget
        self.sidebar_label = ttk.Label(self.root)
        self.sidebar_label['image'] = self.sidebar

        # Header image widget
        self.header_label = ttk.Label(self.root)
        self.header_label['image'] = self.header

        self.btn_create = ttk.Button(
        self.root, text=f'Agregar {self.entity_name}', width=30, command=self.create_window)
        self.btn_index = ttk.Button(
        self.root, text=f'Listar {self.entity_name}', width=30, command=self.index_window)
        self.btn_edit = ttk.Button(
        self.root, text=f'Modificar {self.entity_name}', width=30, command=self.edit_window)
        self.btn_destroy = ttk.Button(
        self.root, text=f'Eliminar {self.entity_name}', width=30, command=self.destroy_window)

        # Grid Images
        self.sidebar_label.grid(row=0, column=0, rowspan=21, sticky=("ws"))
        self.header_label.grid(row=0, column=1, rowspan=10, columnspan=2, sticky=("we"))

        # Grid Buttons
        self.btn_create.grid(row=14, column=1, sticky=("nwes"), columnspan=2)
        self.btn_index.grid(row=16, column=1, sticky=("nwes"), columnspan=2)
        self.btn_edit.grid(row=18, column=1, sticky=("nwes"), columnspan=2)
        self.btn_destroy.grid(row=20, column=1, sticky=("nwes"), columnspan=2)

        # Padding
        
        # self.btn_employees = ttk.Button(self, text='Ver todos los juegos', width=30, command=self.employees_window)
        # self.btn_customers = ttk.Button(self, text='Modificar juego', width=30, command=self.customer_window)
        # self.btn_shippings = ttk.Button(self, text='eliminarjuego', width=30, command=self.shippings_window)
        #self.pack()
    def clear_frames(self):
        for widget in self.root.winfo_children():
            widget.destroy()
