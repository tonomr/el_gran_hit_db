from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from views.menubar import Menubar

from models.venta import Venta
from controllers.venta_dao import VentaDao

class EditSell(ttk.Frame):
    def __init__(self, parent, header_image, search_controller, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent                              # Set parent
        self.header = PhotoImage(file=header_image)     # Imagen del header
        self.search_controller = search_controller      # Función que busca juegos
        self.init_gui()                                 # Iniciar la interfaz gráfica

    # Update purchase
    def update_sell(self):
        # Get input from fields using get method
        self.id_sell =  self.select_byid.get()
        self.date = self.sell_date.get()
        self.quantity = self.sell_quantity.get()
        self.address = self.sell_address.get()
        self.gameid = self.game_id.get()
        self.customerid = self.customer_id.get()

        # Default inputs
        

        # Create sell instance
        sell = Venta(id_venta=self.id_sell, fecha_venta=self.date, cantidad=self.quantity, subtotal=self.subtotal, total=self.total, direccion_envio=self.address, codigo_videojuego=self.gameid, codigo_cliente=self.customerid)
        VentaDao.actualizar(sell)
        confirm = messagebox.askyesno(parent=self.root, message='Venta actualizada correctamente, ¿Desea modificar otra?', 
                            icon='question', title='Venta actualizada')

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
        sell = VentaDao.recuperar(id)
        # Insertamos en los inputs un valor por default
        self.game_id.insert(END, sell.getCodigoVideojuego())
        self.sell_date.insert(END, sell.getFechaVenta())
        self.sell_quantity.insert(END, sell.getCantidad())
        self.customer_id.insert(END, sell.getCodigoCliente())
        self.sell_address.insert(END, sell.getDireccionEnvio())
        # Defaults
        self.subtotal = sell.getSubtotal()
        self.total = sell.getTotal()
        
    # Reset form
    # delete(index, END) elimina desde índice indicado hasta END, final del arreglo.
    def reset_form(self):
        self.game_id.delete(0, END)
        self.sell_date.delete(0, END)
        self.sell_quantity.delete(0, END)
        self.sell_address.delete(0, END)
        self.customer_id.delete(0, END)

    # Go back to main menu
    def cancel_to_main(self):
        self.root.destroy()

    # Clear Listbox
    def clear_listbox(self):
        self.listbox.delete(0, END)

    # Init the Graphic User Interface
    def init_gui(self):
        self.root.title("Editar una venta")         # Nombre de la ventana
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
        self.label_gameid = ttk.Label(self.inputs_frame, text="ID de videojuego")
        self.game_id = ttk.Entry(self.inputs_frame, width=60)
        
        self.label_date = ttk.Label(self.inputs_frame, text="Fecha de venta")
        self.sell_date = ttk.Entry(self.inputs_frame, width=15)

        self.label_quantity = ttk.Label(self.inputs_frame, text="Cantidad")
        self.sell_quantity = ttk.Entry(self.inputs_frame, width=15)

        self.label_address = ttk.Label(self.inputs_frame, text="Dirección envío")
        self.sell_address = ttk.Entry(self.inputs_frame, width=15)

        self.label_customer = ttk.Label(self.inputs_frame, text="ID de cliente")
        self.customer_id = ttk.Entry(self.inputs_frame, width=50)

        # GRID inputs
        self.label_gameid.grid(row=0, column=0, sticky=("w"), columnspan=2)
        self.game_id.grid(row=0, column=2, sticky=("we"), columnspan=3)
        self.label_date.grid(row=2, column=0, sticky=("w"))
        self.sell_date.grid(row=2, column=2, sticky=("we"))
        self.label_quantity.grid(row=3, column=0, sticky=("w"))
        self.sell_quantity.grid(row=3, column=2, sticky=("we"))

        self.label_address.grid(row=4, column=0, sticky=("w"))
        self.sell_address.grid(row=4, column=2, sticky=("we"))

        self.label_customer.grid(row=5, column=0, sticky=("w"), columnspan=2)
        self.customer_id.grid(row=5, column=2, sticky=("we"), columnspan=3)

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
            self.btns_frame, text='Actualizar', width=20, command=self.update_sell)
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