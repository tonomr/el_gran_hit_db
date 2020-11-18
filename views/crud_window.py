from tkinter import *
from tkinter import ttk
from services.logger_conf import logger 
from views.menubar import *

#------------- CRUD MENU ---------------------------------------------------------------
# This window will be created from within the GUI class
# its constructor receives
# parent                A window object, which is always the root
# win_title             A string with the title for the window
# header_title          A string with the path to the header image
# sidebar               A string with the path to the sidebar image
# model_name            A string with the name of the model we are working with
#                       This string is used to replace the name of the model in buttons
# index_controller      A function from Class GUI that links to the INDEX windows
# create_controller     A function from Class GUI that links to the CREATE windows
# edit_controller       [PENDING] function
# destroy_controller    [PENDING] function
# *args and **kwargs    [NOT BEING USED]
#----------------------------------------------------------------------------------------
class CrudWindow(ttk.Frame): 
    def __init__(self, parent, win_title,
                header_title, sidebar, model_name,
                index_controller, create_controller,
                edit_controller, delete_controller, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent                              # Ventana padre
        self.root.title(win_title)                      # Título de ventana
        self.header = PhotoImage(file=header_title)     # Objeto del tipo imagen
        self.sidebar = PhotoImage(file=sidebar)         # Objeto del tipo imagen
        self.model_name = model_name                    # El string nombre de la entidad
        self.index_controller = index_controller        # Funcion
        self.create_controller = create_controller      # Funcion
        self.edit_controller = edit_controller          # Funcion
        self.delete_controller = delete_controller      # Funcion
        self.init_gui()                                 # Inicia el grid y los widgets

    # -------------------- UTILITIES ------------------------
    # Function that cleans out the widgets on the window, 
    # it bassically removes all the images, text, etc.
    def clear_frames(self):
        for widget in self.root.winfo_children():
            widget.destroy()
    
    # Function that is called when the "Regresar" button is 
    # pressed. it just clears the window and create another
    # instance of the GUI window, but receiving as a parameter
    # the root widnow, the window we have worked with since 
    # the main file
    def back_home(self):
      from views.gui import GUI
      self.clear_frames()
      GUI(self.root)  

    # ---------------------- CREATE -------------------------
    # Call to GUI function where user is
    # redirected to the ADD window of the specidied entity
    def create_window(self):
      self.create_controller()

    # ----------------------- SHOW ALL -----------------------
    # Call to GUI function where user is 
    # redirected to the INDEX window of the specidified entity
    def index_window(self):
        self.index_controller()
        
    # ------------------------- EDIT -------------------------
    # Call to GUI function where user is 
    # redirected to a EDIT window of the specidified entity
    def edit_window(self):
        self.edit_controller()
    
     # ---------------------- DELETE -------------------------
    # Call to GUI function where user is
    # redirected to the DELETE window of the specidied entity
    def destroy_window(self):
        self.delete_controller()
    
    # -------- INIT WIDGETS ON THE WINDOW --------------------
    def init_gui(self):
        # Image/Sidebar widget
        self.sidebar_label = ttk.Label(self.root)
        self.sidebar_label['image'] = self.sidebar

        # Header image widget
        self.header_label = ttk.Label(self.root)
        self.header_label['image'] = self.header
        # CRUD Buttons
        self.btn_create = ttk.Button(
        self.root, text=f'Agregar {self.model_name}', width=30, command=self.create_window)
        self.btn_index = ttk.Button(
        self.root, text=f'Listar {self.model_name}', width=30, command=self.index_window)
        self.btn_edit = ttk.Button(
        self.root, text=f'Modificar {self.model_name}', width=30, command=self.edit_window)
        self.btn_destroy = ttk.Button(
        self.root, text=f'Eliminar {self.model_name}', width=30, command=self.destroy_window)
        # Go back home btn
        self.btn_back_home = ttk.Button(
        self.root, text='Regresar', width=20, command=self.back_home)
        
        # Grid Images
        self.sidebar_label.grid(row=0, column=0, rowspan=21, sticky=("ws"))
        self.header_label.grid(row=0, column=1, rowspan=10, columnspan=2, sticky=("we"))

        # Grid Buttons
        self.btn_create.grid(row=12, column=1, sticky=("nwes"), columnspan=2)
        self.btn_index.grid(row=14, column=1, sticky=("nwes"), columnspan=2)
        self.btn_edit.grid(row=16, column=1, sticky=("nwes"), columnspan=2)
        self.btn_destroy.grid(row=18, column=1, sticky=("nwes"), columnspan=2)

        self.btn_back_home.grid(row=20, column=1, sticky=("news"))

        # Padding
        for child in self.winfo_children():
            child.grid_configure(padx=8, pady=2)