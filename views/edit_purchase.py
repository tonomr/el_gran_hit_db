from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from views.menubar import Menubar

from models.compra import Compra
from controllers.compra_dao import CompraDao

class EditPurchase(ttk.Frame):
    def __init__(self, parent, header_image, search_controller, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent                              # Set parent
        self.header = PhotoImage(file=header_image)     # Imagen del header
        self.search_controller = search_controller      # Función que busca juegos
        self.init_gui()                                 # Iniciar la interfaz gráfica

    # Update purchase
    def update_purchase(self):
        # Get input from fields using get method
        id_purchase =  self.select_byid.get()
        condition = self.game_condition.get()
        price = self.game_price.get()
        purchase_date = self.purchase_date.get()
        employee = self.employee_id.get()
        game_id = self.game_id.get()
        # Create videogame instance
        purchase = Compra(id_compra=id_purchase, fecha_compra=purchase_date, estado_compra=condition, precio_compra=price, codigo_videojuego=game_id, codigo_empleado=employee)
        CompraDao.actualizar(purchase)
        confirm = messagebox.askyesno(parent=self.root, message='Compra actualizada correctamente, ¿Desea modificar otra?', 
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
        purchase = CompraDao.recuperar(id)
        # Insertamos en los inputs un valor por default
        self.game_id.insert(END, purchase.get_codigo_videojuego())
        self.game_price.insert(END, purchase.get_precio_compra())
        self.purchase_date.insert(END, purchase.get_fecha_compra())
        self.employee_id.insert(END, purchase.get_codigo_empleado())
        # Al final seteamos el estado del videjuego comparando las opciones existentes
        # Con la que contiene el videojuego que estamos buscando
        for condition in self.game_condition['values']:
            if condition == purchase.get_estado_compra():
                self.game_condition.set(condition)
        
    # Reset form
    # delete(index, END) elimina desde índice indicado hasta END, final del arreglo.
    def reset_form(self):
        self.game_id.delete(0, END)
        self.game_condition.current(0)
        self.game_price.delete(0, END)
        self.purchase_date.delete(0, END)
        self.employee_id.delete(0, END)

    # Go back to main menu
    def cancel_to_main(self):
        self.root.destroy()

    # Clear Listbox
    def clear_listbox(self):
        self.listbox.delete(0, END)

    # Init the Graphic User Interface
    def init_gui(self):
        self.root.title("Editar una compra")         # Nombre de la ventana
        self.root.geometry("790x585")                # Tamaño de la ventana
        
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
        self.label_name = ttk.Label(self.inputs_frame, text="ID del videojuego")
        self.game_id = ttk.Entry(self.inputs_frame, width=60)
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
        self.label_price = ttk.Label(self.inputs_frame, text="Precio")
        self.game_price = ttk.Entry(self.inputs_frame, width=15)
        self.label_purchase_date = ttk.Label(self.inputs_frame, text="Fecha de compra")
        self.purchase_date = ttk.Entry(self.inputs_frame, width=15)
        self.label_employee = ttk.Label(self.inputs_frame, text="ID de empleado")
        self.employee_id = ttk.Entry(self.inputs_frame, width=50)

        # GRID inputs
        self.label_name.grid(row=0, column=0, sticky=("w"), columnspan=2)
        self.game_id.grid(row=0, column=2, sticky=("we"), columnspan=3)

        self.label_condition.grid(row=1, column=0, sticky=("w"), columnspan=2)
        self.game_condition.grid(row=1, column=2, sticky=("we"), columnspan=3)

        self.label_price.grid(row=5, column=0, sticky=("w"))
        self.game_price.grid(row=5, column=2, sticky=("we"))
        self.label_purchase_date.grid(row=5, column=3, sticky=("w"))
        self.purchase_date.grid(row=5, column=4, sticky=("we"))

        self.label_employee.grid(row=7, column=0, sticky=("w"), columnspan=2)
        self.employee_id.grid(row=7, column=2, sticky=("we"), columnspan=3)

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
            self.btns_frame, text='Actualizar', width=20, command=self.update_purchase)
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