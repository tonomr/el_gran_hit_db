from tkinter import *
from tkinter import ttk
from views.menubar import Menubar
from tkinter import messagebox

from models.compra import Compra
from controllers.compra_dao import CompraDao

# Clase recibe una ventana como parametro, la ventana padre
class AddPurchase(ttk.Frame):
    # El constructor toma la ventana que se le mando y en esta nueva ventana usamos
    # la ventana original (padre) para seguir tranbajando 
    # sobre la misma ventana y agregar nuevo contenido
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent # Set parent
        self.init_gui() # Iniciar la interfaz gráfica


    # Add video game, function called from game
    def add_purchase(self):
        # Get input fields .get
        condition = self.game_condition.get()
        date = self.purchase_date.get()
        total = self.game_price.get()
        id_game = self.game_id.get()
        id_employee = self.employee_id.get()
        # Create Purchase instance
        purchase = Compra(fecha_compra=date, estado_compra=condition,precio_compra=total, codigo_videojuego=id_game, codigo_empleado=id_employee)
        CompraDao.insertar(purchase)

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

    # Init the Graphic User Interface
    def init_gui(self):
        # WINDOW TITLE
        self.root.title("Agregar Compra")

        # WINDOW SIZE
        self.root.geometry("600x400")
        
        ############################## FRAMES ###############################
        # -------------------------- HEADER FRAME ---------------------------
        # Widgets
        self.header = PhotoImage(file='add-purchase.png')   
        self.header_frame = ttk.Frame(self.root)          # Crea un frame
        self.header_label = ttk.Label(self.header_frame)  # Crea una etiqueta para la img
        self.header_label['image'] = self.header          # Setea el label al tipo imagen
        # Grid
        self.header_label.grid(row=0, column=0)
        
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
            self.btns_frame, text='Agregar', width=20, command=self.add_purchase)
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
    
        self.inputs_frame.grid(row=4, column=0)
        self.btns_frame.grid(row=5, column=0, padx=10, sticky=("e"))
        
        # Padding
        for child in self.inputs_frame.winfo_children():
            child.grid_configure(padx=8, pady=3)
