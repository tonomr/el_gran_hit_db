from tkinter import *
from tkinter import ttk
from views.menubar import Menubar

from models.venta import Venta
from controllers.venta_dao import VentaDao

# Clase recibe una ventana como parametro, la ventana padre
class AddSell(ttk.Frame):
    # El constructor toma la ventana que se le mando y en esta nueva ventana usamos
    # la ventana original (padre) para seguir tranbajando 
    # sobre la misma ventana y agregar nuevo contenido
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent # Set parent
        self.init_gui() # Iniciar la interfaz gráfica

    # Reset form
    def reset_form(self):
        self.game_id.delete(0, END)
        self.sell_date.delete(0, END)
        self.sell_quantity.delete(0, END)
        #self.sell_address.delete(0, END)
        self.customer_id.delete(0, END)

    # Go back to main menu
    def cancel_to_main(self):
        self.root.destroy()

    # Add video game, function called from game
    def add_sell(self):
        # Get input fields .get
        date = self.sell_date.get()
        quantity = self.sell_quantity.get()
        #subtotal = self.sell_subtotal.get()
        #total = self.sell_total.get()
        #delivery = self.sell_delivery.get()
        id_game = self.game_id.get()
        id_customer = self.customer_id.get()
        # Create Purchase instance
        #sell = Venta(fecha_venta=date, cantidad_venta=quantity, subtotal_venta=subtotal, total_venta=total, direccion_envio=delivery, codigo_videojuego=id_game, codigo_cliente=id_customer)
        sell = Venta(fecha_venta=date, cantidad_venta=quantity, codigo_videojuego=id_game, codigo_cliente=id_customer)
        VentaDao.insertar(sell)

        confirm = messagebox.askyesno(parent=self.root, message='Agregado correctamente, ¿Desea agregar otro?', 
                            icon='question', title='Agregado extiosamente')

        if (confirm == True):
            self.reset_form()
        else:
            self.cancel_to_main()


    # Init the Graphic User Interface
    def init_gui(self):
        # WINDOW TITLE
        self.root.title("Agregar Venta")

        # WINDOW SIZE
        self.root.geometry("600x400")
        
        ############################## FRAMES ###############################
        # -------------------------- HEADER FRAME ---------------------------
        # Widgets
        self.header = PhotoImage(file='add-sell.png')
        self.header_frame = ttk.Frame(self.root)          # Crea un frame
        self.header_label = ttk.Label(self.header_frame)  # Crea una etiqueta para la img
        self.header_label['image'] = self.header          # Setea el label al tipo imagen
        # Grid
        self.header_label.grid(row=0, column=0)
        
        
        # ------------------------- INPUTS FRAME --------------------------------
        self.inputs_frame = ttk.Frame(self.root)
        # Widgets
        self.label_gameid = ttk.Label(self.inputs_frame, text="ID de videojuego")
        self.game_id = ttk.Entry(self.inputs_frame, width=60)
        
        self.label_date = ttk.Label(self.inputs_frame, text="Fecha de venta")
        self.sell_date = ttk.Entry(self.inputs_frame, width=15)

        self.label_quantity = ttk.Label(self.inputs_frame, text="Cantidad")
        self.sell_quantity = ttk.Entry(self.inputs_frame, width=15)

        #self.label_address = ttk.Label(self.inputs_frame, text="Dirección envío")
        #self.sell_address = ttk.Entry(self.inputs_frame, width=15)

        self.label_customer = ttk.Label(self.inputs_frame, text="ID de cliente")
        self.customer_id = ttk.Entry(self.inputs_frame, width=50)

        # GRID inputs
        self.label_gameid.grid(row=0, column=0, sticky=("w"), columnspan=2)
        self.game_id.grid(row=0, column=2, sticky=("we"), columnspan=3)
        self.label_date.grid(row=2, column=0, sticky=("w"))
        self.sell_date.grid(row=2, column=2, sticky=("we"))
        self.label_quantity.grid(row=3, column=0, sticky=("w"))
        self.sell_quantity.grid(row=3, column=2, sticky=("we"))

        #self.label_address.grid(row=4, column=0, sticky=("w"))
        #self.sell_address.grid(row=4, column=2, sticky=("we"))

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
            self.btns_frame, text='Agregar', width=20, command=self.add_sell)
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