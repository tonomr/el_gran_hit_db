from tkinter import *
from tkinter import ttk
from views.menubar import Menubar

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

    # Limpia la ventana, recorre todos los widgets eliminandolos uno por uno
    # Nota: No elimina la configuración de columnas.
    def clear_frames(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    # Add video game, function called from game
    def add_purchase(self):
        # Get input fields .get
        condition = self.game_condition.get()
        date = self.purchase_date.get()
        total = self.purchase_total.get()
        id_game = self.purchase_idgame.get()
        id_employee = self.purchase_idemployee.get()
        # Create Purchase instance
        purchase = Compra(estado_compra=condition, fecha_compra=date,precio_compra=total, codigo_videojuego=id_game, codigo_empleado=id_employee)
        CompraDao.insertar(purchase)

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
        # Estado
        self.label_condition = ttk.Label(self.root, text="Estado del videojuego")
        self.game_condition = ttk.Entry(self.root, width=50)
        # Fecha de Compra
        self.label_date = ttk.Label(self.root, text="Fecha de compra")
        self.purchase_date = ttk.Entry(self.root, width=50)
        # Precio final  
        self.label_total = ttk.Label(self.root, text="Precio final")
        self.purchase_total = ttk.Entry(self.root, width=15)
        # Id del videjuego
        self.label_idgame = ttk.Label(self.root, text="ID videojuego")
        self.purchase_idgame = ttk.Entry(self.root, width=50)
        # Id del empleado
        self.label_idemployee = ttk.Label(self.root, text="ID empleado")
        self.purchase_idemployee = ttk.Entry(self.root, width=50)

        #--------------------------------------------------------------------------
        # BUTTONS
        # Add button
        # Al presionar este parametro, mandamos llamar la función que específicamos
        # en 'command'
        #--------------------------------------------------------------------------
        # Add
        self.btn_add = ttk.Button(
            self.root, text='Agregar', width=30, command=self.add_purchase)
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
        self.label_condition.grid(row=0, column=0)
        self.game_condition.grid(row=0, column=2, sticky=("we"))
        self.label_date.grid(row=1, column=0)
        self.purchase_date.grid(row=1, column=2, sticky=("we"))
        self.label_total.grid(row=2, column=0)
        self.purchase_total.grid(row=2, column=2, sticky=("we"))
        self.label_idgame.grid(row=3, column=0)
        self.purchase_idgame.grid(row=3, column=2, sticky=("we"))
        self.label_idemployee.grid(row=4, column=0)
        self.purchase_idemployee.grid(row=4, column=2, sticky=("we"))

        # Buttons
        self.btn_add.grid(row=19, column=2, sticky=("we"))
        #self.btn_back.grid(row=19, column=3, sticky=("we"))
        #self.btn_cancel.grid(row=19, column=4, sticky=("we"))
