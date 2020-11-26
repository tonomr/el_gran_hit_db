from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from views.menubar import Menubar

from models.empleado import Empleado
from controllers.empleado_dao import EmpleadoDao

class EditEmployee(ttk.Frame):
    def __init__(self, parent, header_image, search_controller, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent                              # Set parent
        self.header = PhotoImage(file=header_image)     # Imagen del header
        self.search_controller = search_controller      # Función que clientes
        self.init_gui()                                 # Iniciar la interfaz gráfica

    # Update Customer
    def update_employee(self):
        # Get input from fields using get method
        id_employee =  self.select_byid.get()
        name = self.employee_name.get()
        address = self.employee_address.get()
        tel = self.employee_tel.get()
        # Create customer instance
        employee = Empleado(id_empleado=id_employee, nombre_empleado=name, direccion_empleado=address,
                          telefono_empleado=tel)
        EmpleadoDao.actualizar(employee)
        confirm = messagebox.askyesno(parent=self.root, message='Empleado actualizado correctamente, ¿Desea modificar otro?', 
                            icon='question', title='Empleado actualizado')

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
        # Recupera un sólo item
        id = (self.select_byid.get(),)
        employee = EmpleadoDao.recuperar(id)
        # Insertamos en los inputs un valor por default
        self.employee_name.insert(END, employee.getNombreEmpleado())
        self.employee_address.insert(END, employee.getDireccionEmpleado())
        self.employee_tel.insert(END, employee.getTelefonoEmpleado())
        
    # Reset form
    # delete(index, END) elimina desde índice indicado hasta END, final del arreglo.
    def reset_form(self):
        self.employee_name.delete(0, END)
        self.employee_address.delete(0, END)
        self.employee_tel.delete(0, END)

    # Go back to main menu
    def cancel_to_main(self):
        self.root.destroy()

    # Clear Listbox
    def clear_listbox(self):
        self.listbox.delete(0, END)

    # Init the Graphic User Interface
    def init_gui(self):
        self.root.title("Editar un empleado")       # Nombre de la ventana
        self.root.geometry("790x540")               # Tamaño de la ventana
        
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
        self.label_name = ttk.Label(self.inputs_frame, text="Nombre del empleado")
        self.employee_name = ttk.Entry(self.inputs_frame, width=60)
        
        self.label_address = ttk.Label(self.inputs_frame, text="Dirección")
        self.employee_address = ttk.Entry(self.inputs_frame, width=50)
        
        self.label_tel = ttk.Label(self.inputs_frame, text="Teléfono")
        self.employee_tel = ttk.Entry(self.inputs_frame, width=50)

        # GRID inputs
        self.label_name.grid(row=0, column=0, sticky=("w"), columnspan=2)
        self.employee_name.grid(row=0, column=2, sticky=("we"), columnspan=3)

        self.label_address.grid(row=1, column=0, sticky=("w"), columnspan=2)
        self.employee_address.grid(row=1, column=2, sticky=("we"), columnspan=3)
        
        self.label_tel.grid(row=2, column=0, sticky=("w"), columnspan=2)
        self.employee_tel.grid(row=2, column=2, sticky=("we"), columnspan=3)

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
            self.btns_frame, text='Actualizar', width=20, command=self.update_employee)
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
        self.listbox_frame.grid(row=1, column=0)
        self.search_frame.grid(row=2, column=0, pady=8)
        self.bar_label.grid(row=3, column=0, pady=15)
        self.inputs_frame.grid(row=4, column=0)
        self.btns_frame.grid(row=5, column=0, padx=10, sticky=("e"))
        
        # Padding
        for child in self.inputs_frame.winfo_children():
            child.grid_configure(padx=8, pady=3)