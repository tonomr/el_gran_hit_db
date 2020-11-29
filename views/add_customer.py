from tkinter import *
from tkinter import ttk
from views.menubar import Menubar
from tkinter import messagebox

from models.cliente import Cliente
from controllers.clientes_dao import ClienteDao

# Clase recibe una ventana como parametro, la ventana padre
class AddCustomer(ttk.Frame):
    # El constructor toma la ventana que se le mando y en esta nueva ventana usamos
    # la ventana original (padre) para seguir tranbajando 
    # sobre la misma ventana y agregar nuevo contenido
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent # Set parent
        self.init_gui() # Iniciar la interfaz gráfica

    # Add video game, function called from game
    def add_customer(self):
        # Get input fields .get
        name = self.customer_name.get()
        email = self.customer_email.get()
        address = self.customer_address.get()
        telephone = self.customer_tel.get()
        # Create Employee instance
        customer = Cliente(nombre_cliente=name, email_cliente=email, telefono_cliente=telephone, direccion_cliente=address)
        ClienteDao.insertar(customer)

        confirm = messagebox.askyesno(parent=self.root, message='Cliente agregado correctamente, ¿Desea agregar otro?', 
                            icon='question', title='Cliente agregado')

        if (confirm == True):
            self.reset_form()
        else:
            self.cancel_to_main()

    # Reset form
    # delete(index, END) elimina desde índice indicado hasta END, final del arreglo.
    def reset_form(self):
        self.customer_name.delete(0, END)
        self.customer_email.delete(0, END)
        self.customer_address.delete(0, END)
        self.customer_tel.delete(0, END)

    # Go back to main menu
    def cancel_to_main(self):
        self.root.destroy()

    # Init the Graphic User Interface
    def init_gui(self):
        # WINDOW TITLE
        self.root.title("Agregar Cliente")

        # WINDOW SIZE
        self.root.geometry("600x400")
        
        ############################## FRAMES ###############################
        # -------------------------- HEADER FRAME ---------------------------
        # Widgets
        self.header = PhotoImage(file='add-customer.png') 
        self.header_frame = ttk.Frame(self.root)          # Crea un frame
        self.header_label = ttk.Label(self.header_frame)  # Crea una etiqueta para la img
        self.header_label['image'] = self.header          # Setea el label al tipo imagen
        # Grid
        self.header_label.grid(row=0, column=0)
        
        # ------------------------- INPUTS FRAME --------------------------------
        self.inputs_frame = ttk.Frame(self.root)
        # Widgets
        self.label_name = ttk.Label(self.inputs_frame, text="Nombre del cliente")
        self.customer_name = ttk.Entry(self.inputs_frame, width=60)
        
        self.label_email = ttk.Label(self.inputs_frame, text="Email")
        self.customer_email = ttk.Entry(self.inputs_frame, width=50)
        
        self.label_address = ttk.Label(self.inputs_frame, text="Dirección")
        self.customer_address = ttk.Entry(self.inputs_frame, width=50)
        
        self.label_tel = ttk.Label(self.inputs_frame, text="Teléfono")
        self.customer_tel = ttk.Entry(self.inputs_frame, width=50)

        # GRID inputs
        self.label_name.grid(row=0, column=0, sticky=("w"), columnspan=2)
        self.customer_name.grid(row=0, column=2, sticky=("we"), columnspan=3)

        self.label_email.grid(row=1, column=0, sticky=("w"), columnspan=2)
        self.customer_email.grid(row=1, column=2, sticky=("we"), columnspan=3)

        self.label_address.grid(row=2, column=0, sticky=("w"), columnspan=2)
        self.customer_address.grid(row=2, column=2, sticky=("we"), columnspan=3)
        
        self.label_tel.grid(row=3, column=0, sticky=("w"), columnspan=2)
        self.customer_tel.grid(row=3, column=2, sticky=("we"), columnspan=3)

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
            self.btns_frame, text='Agregar', width=20, command=self.add_customer)
        # Reset
        self.btn_reset = ttk.Button(
            self.btns_frame, text='Reset', width=20, command=self.reset_form)
        # Cancel
        self.btn_cancel = ttk.Button(
            self.btns_frame, text='Cancelar', width=20, command=self.cancel_to_main)

        # Buttons
        self.btn_update.grid(row=1, column=1, pady=15)
        self.btn_reset.grid(row=1, column=2, pady=15)
        self.btn_cancel.grid(row=1, column=3, pady=15)

        # -------------------------- GRID ROOT -------------------------------
        self.header_frame.grid(row=0, column=0)
        self.inputs_frame.grid(row=4, column=0)
        self.btns_frame.grid(row=5, column=0, padx=10, sticky=("e"))
        
        # Padding
        for child in self.inputs_frame.winfo_children():
            child.grid_configure(padx=8, pady=3)