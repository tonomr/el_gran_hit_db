from tkinter import *
from tkinter import ttk
from views.menubar import Menubar

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

    # Limpia la ventana, recorre todos los widgets eliminandolos uno por uno
    # Nota: No elimina la configuración de columnas.
    def clear_frames(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    # Add video game, function called from game
    def add_customer(self):
        # Get input fields .get
        name = self.customer_name.get()
        email = self.customer_email.get()
        address = self.customer_address.get()
        telephone = self.customer_telephone.get()
        # Create Employee instance
        customer = Cliente(nombre_cliente=name, email=email,direccion_cliente=address, telefono_cliente=telephone)
        ClienteDao.insertar(customer)

    # Go back to previous window
    def back_to_prev(self):
        #self.clear_frames()
        #GameWindow(self.root)
        pass

    # Go back to main menu
    def cancel_to_main(self):
        #self.clear_frames()
        pass

    # Init the Graphic User Interface
    def init_gui(self):
        self.clear_frames()
        # WINDOW TITLE
        self.root.title("Agregar Cliente")

        # WINDOW SIZE
        self.root.geometry("600x400")
        # Configuración de columnas
        #self.grid_columnconfigure(0, weight=1)
        #self.grid_columnconfigure(2, weight=1)

        #--------------------------------------------------------------------------
        # LABEL AND INPUT FIELDS    
        # Label es una etiqueta, que describe lo que deberías escribir en el campo
        # Entry es un widget del tipo input
        #--------------------------------------------------------------------------
        # Name
        self.label_name = ttk.Label(self.root, text="Nombre del cliente")
        self.customer_name = ttk.Entry(self.root, width=50)
        # Email
        self.label_email = ttk.Label(self.root, text="Email")
        self.customer_email = ttk.Entry(self.root, width=50)
        # Address    
        self.label_address = ttk.Label(self.root, text="Dirección")
        self.customer_address = ttk.Entry(self.root, width=15)
        # Telephone
        self.label_telephone = ttk.Label(self.root, text="Teléfono")
        self.customer_telephone = ttk.Entry(self.root, width=50)

        #--------------------------------------------------------------------------
        # BUTTONS
        # Add button
        # Al presionar este parametro, mandamos llamar la función que específicamos
        # en 'command'
        #--------------------------------------------------------------------------
        # Add
        self.btn_add = ttk.Button(
            self.root, text='Agregar', width=30, command=self.add_customer)
        # Back
        self.btn_back = ttk.Button(
            self.root, text='Atrás', width=30, command=self.back_to_prev)
        # Cancel
        self.btn_cancel = ttk.Button(
            self.root, text='Cancelar', width=30, command=self.cancel_to_main)

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
        self.label_name.grid(row=0, column=0)
        self.customer_name.grid(row=0, column=2, sticky=("we"))
        self.label_email.grid(row=1, column=0)
        self.customer_email.grid(row=1, column=2, sticky=("we"))
        self.label_address.grid(row=2, column=0)
        self.customer_address.grid(row=2, column=2, sticky=("we"))
        self.label_telephone.grid(row=3, column=0)
        self.customer_telephone.grid(row=3, column=2, sticky=("we"))

        # Buttons
        self.btn_add.grid(row=19, column=2, sticky=("we"))
        #self.btn_back.grid(row=19, column=3, sticky=("we"))
        #self.btn_cancel.grid(row=19, column=4, sticky=("we"))