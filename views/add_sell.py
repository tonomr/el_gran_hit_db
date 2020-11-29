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

    # Limpia la ventana, recorre todos los widgets eliminandolos uno por uno
    # Nota: No elimina la configuración de columnas.
    def clear_frames(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    # Add video game, function called from game
    def add_sell(self):
        # Get input fields .get
        date = self.sell_date.get()
        quantity = self.sell_quantity.get()
        #subtotal = self.sell_subtotal.get()
        #total = self.sell_total.get()
        #delivery = self.sell_delivery.get()
        id_game = self.sell_idgame.get()
        id_customer = self.sell_idcustomer.get()
        # Create Purchase instance
        #sell = Venta(fecha_venta=date, cantidad_venta=quantity, subtotal_venta=subtotal, total_venta=total, direccion_envio=delivery, codigo_videojuego=id_game, codigo_cliente=id_customer)
        sell = Venta(fecha_venta=date, cantidad_venta=quantity, codigo_videojuego=id_game, codigo_cliente=id_customer)
        VentaDao.insertar(sell)

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
        self.root.title("Agregar Venta")

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

        # Fecha de venta
        self.label_date = ttk.Label(self.root, text="Fecha de venta")
        self.sell_date = ttk.Entry(self.root, width=50)
        # Cantidad
        self.label_quantity = ttk.Label(self.root, text="Cantidad")
        self.sell_quantity = ttk.Entry(self.root, width=50)
        '''
        # Subtotal
        self.label_subtotal = ttk.Label(self.root, text="Subtotal")
        self.sell_subtotal = ttk.Entry(self.root, width=50)
        # Total  
        self.label_total = ttk.Label(self.root, text="Total")
        self.sell_total = ttk.Entry(self.root, width=15)
        # Dirección de envío  
        self.label_delivery = ttk.Label(self.root, text="Envío a")
        self.sell_delivery = ttk.Entry(self.root, width=15)
        '''
        # Id del videjuego
        self.label_idgame = ttk.Label(self.root, text="ID videojuego")
        self.sell_idgame = ttk.Entry(self.root, width=50)
        # Id del empleado
        self.label_idcustomer = ttk.Label(self.root, text="ID cliente")
        self.sell_idcustomer = ttk.Entry(self.root, width=50)

        #--------------------------------------------------------------------------
        # BUTTONS
        # Add button
        # Al presionar este parametro, mandamos llamar la función que específicamos
        # en 'command'
        #--------------------------------------------------------------------------
        # Add
        self.btn_add = ttk.Button(
            self.root, text='Agregar', width=30, command=self.add_sell)
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
        self.label_date.grid(row=1, column=0)
        self.sell_date.grid(row=1, column=2, sticky=("we"))
        self.label_quantity.grid(row=2, column=0)
        self.sell_quantity.grid(row=2, column=2, sticky=("we"))
        '''
        self.label_subtotal.grid(row=3, column=0)
        self.sell_subtotal.grid(row=3, column=2, sticky=("we"))
        self.label_total.grid(row=4, column=0)
        self.sell_total.grid(row=4, column=2, sticky=("we"))
        self.label_delivery.grid(row=5, column=0)
        self.sell_delivery.grid(row=5, column=2, sticky=("we"))
        '''
        self.label_idgame.grid(row=6, column=0)
        self.sell_idgame.grid(row=6, column=2, sticky=("we"))
        self.label_idcustomer.grid(row=7, column=0)
        self.sell_idcustomer.grid(row=7, column=2, sticky=("we"))

        # Buttons
        self.btn_add.grid(row=19, column=2, sticky=("we"))
        #self.btn_back.grid(row=19, column=3, sticky=("we"))
        #self.btn_cancel.grid(row=19, column=4, sticky=("we"))
