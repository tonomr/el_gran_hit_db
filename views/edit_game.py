from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from views.menubar import Menubar

from models.videojuego import Videojuego
from controllers.videojuego_dao import VideojuegoDao

class EditGame(ttk.Frame):
    def __init__(self, parent, header_image, search_controller, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent                              # Set parent
        self.header = PhotoImage(file=header_image)     # Imagen del header
        self.search_controller = search_controller      # Función que busca juegos
        self.init_gui()                                 # Iniciar la interfaz gráfica

    # Add video game, function called from game
    def update_game(self):
        # Get input from fields using get method
        id_game =  self.select_byid.get()
        name = self.game_name.get()
        condition = self.game_condition.get()
        quantity = self.game_quantity.get()
        classification = self.game_classification.get()
        description = self.game_description.get()
        price = self.game_price.get()
        released = self.game_released.get()
        devs = self.game_devs.get()
        # Create videogame instance
        videogame = Videojuego(id_videojuego=id_game, nombre_videojuego=name, estado_videojuego=condition, cantidad_videojuego=quantity, clasificacion_videojuego=classification,
                               descripcion_videojuego=description, precio_videojuego=price, publicacion_videojuego=released, codigo_desarrolladora=devs)
        VideojuegoDao.actualizar(videogame)
        confirm = messagebox.askyesno(parent=self.root, message='Videojuego actualizado correctamente, ¿Desea modificar otro?', 
                            icon='question', title='Videojuego actualizado')

        if (confirm == True):
            self.select_byid.delete(0, END)
            self.reset_form()
        else:
            self.cancel_to_main()
    
    # ------------------------------------------------------------------
    # search_items es llamada cuando el usuario da click en el botón de buscar
    # y ha ingresado o no un ID
    # like_pattern almacena en una tupla el valor insertado en el input
    # search_term, a este string tomado del input le damos el formato
    # %string% para que pueda ser ejecutado por la sentencia LIKE de PostgresSQL
    # ------------------------------------------------------------------
    def search_item(self):
        self.reset_form()
        self.clear_listbox()
        like_pattern = ('%{}%'.format(self.search_term.get()),)
        self.list_items = self.search_controller(like_pattern)      # search_controller regresa una lista de matches
        for item in self.list_items:                                # Llenamos el Listbox con los elementos
            self.listbox.insert(END, item)                          # de la lista

    # select_item llena los inputs con todos los datos de el item con el id
    # correspondiente.
    def select_item(self):
        # Llamamos la función recuperar que recibe como parametro
        # un id de videojuego, en este caso el que ha sido insertado en el
        # campo select_byid
        id = (self.select_byid.get(),)
        videojuego = VideojuegoDao.recuperar(id)
        # Insertamos en los inputs un valor por default
        self.game_name.insert(END, videojuego.get_nombre_videojuego())
        self.game_quantity.insert(END, videojuego.get_cantidad_videojuego())
        self.game_classification.insert(END, videojuego.get_clasificacion_videojuego())
        self.game_description.insert(END, videojuego.get_descripcion_videojuego())
        self.game_price.insert(END, videojuego.get_precio_videojuego())
        self.game_released.insert(END, videojuego.get_publicacion_videojuego())
        self.game_devs.insert(END, videojuego.get_codigo_desarrolladora())
        # Al final seteamos el estado del videjuego comparando las opciones existentes
        # Con la que contiene el videojuego que estamos buscando
        for condition in self.game_condition['values']:
            if condition == videojuego.getEstado():
                self.game_condition.set(condition)
        
    # Reset form
    # delete(index, END) elimina desde índice indicado hasta END, final del arreglo.
    def reset_form(self):
        self.game_name.delete(0, END)
        self.game_condition.current(0)
        self.game_quantity.delete(0, END)
        self.game_classification.delete(0, END)
        self.game_description.delete(0, END)
        self.game_price.delete(0, END)
        self.game_released.delete(0, END)
        self.game_devs.delete(0, END)

    # Go back to main menu
    def cancel_to_main(self):
        self.root.destroy()

    # Clear Listbox
    def clear_listbox(self):
        self.listbox.delete(0, END)

    # Init the Graphic User Interface
    def init_gui(self):
        self.root.title("Editar un videojuego")     # Nombre de la ventana
        self.root.geometry("790x585")               # Tamaño de la ventana
        
        ############################## FRAMES ###############################
        # -------------------------- HEADER FRAME ---------------------------
        # Widgets
        self.header_frame = ttk.Frame(self.root)          # Crea un frame
        self.header_label = ttk.Label(self.header_frame)  # Crea una etiqueta para la img
        self.header_label['image'] = self.header          # Setea el label al tipo imagen
        # Grid
        self.header_label.grid(row=0, column=0)
        # --------------------------- LISTBOX FRAME --------------------------
        # Widgets
        self.listbox_frame = ttk.Frame(self.root)         # Crea un frame
        self.listbox = Listbox(self.listbox_frame, font='consolas', width=85, height=5) # Crea listbox
        # Scrollbar
        self.scrollbar = ttk.Scrollbar(self.listbox_frame, orient=VERTICAL, command=self.listbox.yview)    
        # Grid
        self.listbox.grid(row=0, column=0, sticky=("we"))
        self.scrollbar.grid(column=1, row=0, sticky=("ns"))
        self.listbox['yscrollcommand'] = self.scrollbar.set 
        # ---------------------------- SEARCH/SELECT FRAME --------------------
        # Widgets
        self.search_frame = ttk.Frame(self.root) 
        self.label_search = ttk.Label(self.search_frame, text="Buscar por nombre")
        self.search_term = ttk.Entry(self.search_frame, width=50)
        self.btn_search = ttk.Button(
            self.search_frame, text='Buscar', width=15, command=self.search_item)
        
        self.label_edit = ttk.Label(self.search_frame, text="Introduzca el id para modificar")
        self.select_byid = ttk.Entry(self.search_frame, width=50)
        self.btn_edit= ttk.Button(
            self.search_frame, text='Seleccionar', width=15, command=self.select_item)
        # GRID
        self.label_search.grid(row=0, column=0)
        self.search_term.grid(row=0, column=1)
        self.btn_search.grid(row=0, column=2)
        
        self.label_edit.grid(row=1, column=0)
        self.select_byid.grid(row=1, column=1)
        self.btn_edit.grid(row=1, column=2)

        # --------------------------- ROOT LEVEL --------------------------------
        # Horizontal bar
        self.horizontal_bar = PhotoImage(file="horizontal-bar.png")
        self.bar_label = ttk.Label(self.root)
        self.bar_label['image'] = self.horizontal_bar
        
        # ------------------------- INPUTS FRAME --------------------------------
        self.inputs_frame = ttk.Frame(self.root)
        # Widgets
        self.label_name = ttk.Label(self.inputs_frame, text="Nombre del videojuego")
        self.game_name = ttk.Entry(self.inputs_frame, width=60)
        # Multiple Option input
        # Crea la etiqueta "Condición"
        self.label_condition = ttk.Label(self.inputs_frame, text="Estado")
        # Crea el objeto de input múltiple, recibe ventana padre y ocpional el ancho
        self.game_condition = ttk.Combobox(self.inputs_frame, width=60)
        # Agrega una tupla a la configuración 'values' del input
        # Aquí agregamos los valores que se usan
        self.game_condition['values'] = (' ','Nuevo', 'Seminuevo', 'Usado')
        # Configuramos el estado del input para que sea únicamente de lectura
        # y el usario no pueda modificar su valor
        self.game_condition.state(['readonly'])
        # More labels and input fields...
        self.label_quantity = ttk.Label(self.inputs_frame, text="Cantidad")
        self.game_quantity = ttk.Entry(self.inputs_frame, width=15)
        self.label_classification = ttk.Label(self.inputs_frame, text="Clasificación")
        self.game_classification = ttk.Entry(self.inputs_frame, width=15)
        self.label_description = ttk.Label(self.inputs_frame, text="Descripción")
        self.game_description = ttk.Entry(self.inputs_frame, width=50)
        self.label_price = ttk.Label(self.inputs_frame, text="Precio")
        self.game_price = ttk.Entry(self.inputs_frame, width=15)
        self.label_released = ttk.Label(self.inputs_frame, text="Fecha de publicaión")
        self.game_released = ttk.Entry(self.inputs_frame, width=15)
        self.label_devs = ttk.Label(self.inputs_frame, text="Desarrolladora")
        self.game_devs = ttk.Entry(self.inputs_frame, width=50)

        # GRID inputs
        self.label_name.grid(row=0, column=0, sticky=("w"), columnspan=2)
        self.game_name.grid(row=0, column=2, sticky=("we"), columnspan=3)

        self.label_condition.grid(row=1, column=0, sticky=("w"), columnspan=2)
        self.game_condition.grid(row=1, column=2, sticky=("we"), columnspan=3)

        self.label_quantity.grid(row=2, column=0, sticky=("w"))
        self.game_quantity.grid(row=2, column=2, sticky=("we"))
        self.label_classification.grid(row=2, column=3, sticky=("w"), columnspan=2)
        self.game_classification.grid(row=2, column=4, sticky=("we"), columnspan=3)

        self.label_description.grid(row=4, column=0, sticky=("w"), columnspan=2)
        self.game_description.grid(row=4, column=2, sticky=("we"), columnspan=3)

        self.label_price.grid(row=5, column=0, sticky=("w"))
        self.game_price.grid(row=5, column=2, sticky=("we"))
        self.label_released.grid(row=5, column=3, sticky=("w"))
        self.game_released.grid(row=5, column=4, sticky=("we"))

        self.label_devs.grid(row=7, column=0, sticky=("w"), columnspan=2)
        self.game_devs.grid(row=7, column=2, sticky=("we"), columnspan=3)

        #--------------------------------------------------------------------------
        # BUTTONS
        # Add button
        # Al presionar este parametro, mandamos llamar la función que específicamos
        # en 'command'
        #--------------------------------------------------------------------------
        # Buttons Frame
        self.btns_frame = ttk.Frame(self.root)
        # Add
        self.btn_update = ttk.Button(
            self.btns_frame, text='Actualizar', width=20, command=self.update_game)
        # Reset
        self.btn_reset = ttk.Button(
            self.btns_frame, text='Reset', width=20, command=self.reset_form)
        # Cancel
        self.btn_cancel = ttk.Button(
            self.btns_frame, text='Cancelar', width=20, command=self.cancel_to_main)

        # Buttons
        self.btn_update.grid(row=9, column=1, pady=15)
        self.btn_reset.grid(row=9, column=2, pady=15)
        self.btn_cancel.grid(row=9, column=3, pady=15)

        # -------------------------- GRID ROOT -------------------------------
        self.header_frame.grid(row=0, column=0)
        self.listbox_frame.grid(row=1, column=0)
        self.search_frame.grid(row=2, column=0, pady=8)
        self.bar_label.grid(row=3, column=0, pady=15)
        self.inputs_frame.grid(row=4, column=0)
        self.btns_frame.grid(row=5, column=0, padx=10, sticky=("e"))
        
        # Padding
        for child in self.inputs_frame.winfo_children():
            child.grid_configure(padx=8, pady=3)
