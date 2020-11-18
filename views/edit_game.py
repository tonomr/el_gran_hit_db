from tkinter import *
from tkinter import ttk
from views.menubar import Menubar

from models.videojuego import Videojuego
from controllers.videojuego_dao import VideojuegoDao

class EditGame(ttk.Frame):
    # El constructor toma la ventana que se le mando y en esta nueva ventana usamos
    # la ventana padre para seguir tranbajando la misma ventana y agregar nuevo contenido
    # recibe, la imagen del header, y la función de búsqueda desde guy.py
    def __init__(self, parent, header_image, search_controller, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent # Set parent
        self.header = PhotoImage(file=header_image)
        self.search_controller = search_controller
        self.init_gui() # Iniciar la interfaz gráfica

    # Limpia la ventana, recorre todos los widgets eliminandolos uno por uno
    # Nota: No elimina la configuración de columnas.
    def clear_frames(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    # Add video game, function called from game
    def update_game(self):
        # Get input fields .get
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

    def search_item(self):
      like_pattern = ('%{}%'.format(self.search_term.get()),)
      self.list_items = self.search_controller(like_pattern)
      for item in self.list_items:
        self.listbox.insert(END, item)

    def select_item(self):
      #videojuego = VideojuegoDao.SELECCIONA_UNO(id_de_juego)
      #self.game_name.insert(END, videojuego.getName(

      #e.insert(END, 'default text')
      pass
    # Go back to previous window
    def reset_form(self):
        #self.clear_frames()
        #GameWindow(self.root)
        pass

    # Go back to main menu
    def cancel_to_main(self):
        #self.clear_frames()
        pass


    # Init the Graphic User Interface
    def init_gui(self):
        self.root.title("Editar un videojuego")     # Nombre de la ventana
        self.root.geometry("790x600")               # Tamaño de la ventana
        
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
        self.edit_byid = ttk.Entry(self.search_frame, width=50)
        self.btn_edit= ttk.Button(
            self.search_frame, text='Seleccionar', width=15, command=self.select_item)
        # GRID
        self.label_search.grid(row=0, column=0)
        self.search_term.grid(row=0, column=1)
        self.btn_search.grid(row=0, column=2)
        
        self.label_edit.grid(row=1, column=0)
        self.edit_byid.grid(row=1, column=1)
        self.btn_edit.grid(row=1, column=2)

        # --------------------- ROOT LEVEL ---------------------------
        # Horizontal bar
        self.horizontal_bar = PhotoImage(file="horizontal-bar.png")
        self.bar_label = ttk.Label(self.root)
        self.bar_label['image'] = self.horizontal_bar
        
        # ----------------------- INPUTS FRAME --------------------------------
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
        self.game_condition['values'] = ('Nuevo', 'Seminuevo', 'Usado')
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

        #--------------------------------------------------------------------------
        # BUTTONS
        # Add button
        # Al presionar este parametro, mandamos llamar la función que específicamos
        # en 'command'
        #--------------------------------------------------------------------------
        # Add
        self.btn_update = ttk.Button(
            self.inputs_frame, text='Actualizar', width=30, command=self.update_game)
        # Reset
        self.btn_reset = ttk.Button(
            self.inputs_frame, text='Reset', width=30, command=self.reset_form)
        # Cancel
        self.btn_cancel = ttk.Button(
            self.inputs_frame, text='Cancelar', width=30, command=self.cancel_to_main)

        # -------------------------------------------------------------------------
        # GRID 
        # Especificamos las columnas, las filas. El ancho de las columnas NO es estático
        # Su ancho depende del widget que haya dentro de ella, es decir, si no
        # existe nada en una columna dada, el espacio no se verá reflejado en el grid de
        # de nuestra ventana.
        # Sticky puede llevar cualquier combinacion de caracteres
        # Para alinear o estierar el widget en alguna de las direcciones cardinales
        # 'w' west (izquierda) 'e' east (derecha) 'n' north 's' south
        #---------------------------------------------------------------------------
        # Inputs
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

        # Buttons
        self.btn_update.grid(row=9, column=3, sticky=("we"))
        self.btn_reset.grid(row=10, column=3, sticky=("we"))
        self.btn_cancel.grid(row=11, column=3, sticky=("we"))

        # -------------------------- GRID ROOT -------------------------------
        self.header_frame.grid(row=0, column=0)
        self.listbox_frame.grid(row=1, column=0)
        self.search_frame.grid(row=2, column=0)
        self.bar_label.grid(row=3, column=0)
        self.inputs_frame.grid(row=4, column=0)
        
        # Padding
        for child in self.inputs_frame.winfo_children():
            child.grid_configure(padx=8, pady=2)