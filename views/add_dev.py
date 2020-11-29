from tkinter import *
from tkinter import ttk
from views.menubar import Menubar
from tkinter import messagebox

from models.desarrolladora import Desarrolladora 
from controllers.desarrolladora_dao import DesarrolladoraDao

# Clase recibe una ventana como parametro, la ventana padre
class AddDev(ttk.Frame):
    # El constructor toma la ventana que se le mando y en esta nueva ventana usamos
    # la ventana padre para seguir tranbajando la misma ventana y agregar nuevo contenido
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
    def add_dev(self):
        # Get input fields .get
        name = self.dev_name.get()
        address = self.dev_address.get()
        telephone = self.dev_tel.get()
        # Create Employee instance
        dev = Desarrolladora(nombre_desarrolladora=name, telefono_desarrolladora=telephone, direccion_desarrolladora=address)
        DesarrolladoraDao.insertar(dev)

        confirm = messagebox.askyesno(parent=self.root, message='Desarrolladora agregada correctamente, ¿Desea agregar otro?', 
                            icon='question', title='Desarrolladora agregada')

        if (confirm == True):
            self.reset_form()
        else:
            self.cancel_to_main()

    # Reset form
    # delete(index, END) elimina desde índice indicado hasta END, final del arreglo.
    def reset_form(self):
        self.dev_name.delete(0, END)
        self.dev_address.delete(0, END)
        self.dev_tel.delete(0, END)

    # Go back to main menu
    def cancel_to_main(self):
        self.root.destroy()


    # Init the Graphic User Interface
    def init_gui(self):
        # WINDOW TITLE
        self.root.title("Agregar Desarrolladora")

        # WINDOW SIZE
        self.root.geometry("600x400")
        
        ############################## FRAMES ###############################
        # -------------------------- HEADER FRAME ---------------------------
        # Widgets
        self.header = PhotoImage(file='add-dev.png') 
        self.header_frame = ttk.Frame(self.root)          # Crea un frame
        self.header_label = ttk.Label(self.header_frame)  # Crea una etiqueta para la img
        self.header_label['image'] = self.header          # Setea el label al tipo imagen
        # Grid
        self.header_label.grid(row=0, column=0)
    
        # ------------------------- INPUTS FRAME --------------------------------
        self.inputs_frame = ttk.Frame(self.root)
        # Widgets
        self.label_name = ttk.Label(self.inputs_frame, text="Nombre de Desarrolladora")
        self.dev_name = ttk.Entry(self.inputs_frame, width=60)
        
        self.label_address = ttk.Label(self.inputs_frame, text="Dirección")
        self.dev_address = ttk.Entry(self.inputs_frame, width=50)
        
        self.label_tel = ttk.Label(self.inputs_frame, text="Teléfono")
        self.dev_tel = ttk.Entry(self.inputs_frame, width=50)

        # GRID inputs
        self.label_name.grid(row=0, column=0, sticky=("w"), columnspan=2)
        self.dev_name.grid(row=0, column=2, sticky=("we"), columnspan=3)

        self.label_address.grid(row=1, column=0, sticky=("w"), columnspan=2)
        self.dev_address.grid(row=1, column=2, sticky=("we"), columnspan=3)
        
        self.label_tel.grid(row=2, column=0, sticky=("w"), columnspan=2)
        self.dev_tel.grid(row=2, column=2, sticky=("we"), columnspan=3)

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
            self.btns_frame, text='Agregar', width=20, command=self.add_dev)
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