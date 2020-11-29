from tkinter import *
from tkinter import ttk
from views.menubar import Menubar
from tkinter import messagebox

from models.videojuego import Videojuego
from controllers.videojuego_dao import VideojuegoDao

# Clase recibe una ventana como parametro, la ventana padre
class AddGame(ttk.Frame):
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
    def add_game(self):
        # Get input fields .get
        name = self.game_name.get()
        condition = self.game_condition.get()
        quantity = self.game_quantity.get()
        classification = self.game_classification.get()
        description = self.game_description.get()
        price = self.game_price.get()
        released = self.game_released.get()
        devs = self.game_devs.get()
        # Create videogame instance
        videogame = Videojuego(nombre_videojuego=name, estado_videojuego=condition, cantidad_videojuego=quantity, clasificacion_videojuego=classification,
                               descripcion_videojuego=description, precio_videojuego=price, publicacion_videojuego=released, codigo_desarrolladora=devs)
        VideojuegoDao.insertar(videogame)

        confirm = messagebox.askyesno(parent=self.root, message='Videojuego agregado correctamente, ¿Desea modificar otro?', 
                            icon='question', title='Videojuego agregado')

        if (confirm == True):
            self.reset_form()
        else:
            self.cancel_to_main()

    # Reset form
    # delete(index, END) elimina desde índice indicado hasta END, final del arreglo.
    def reset_form(self):
        print("Llega")
        self.game_name.delete(0, END)
        self.game_condition.current(0)
        self.game_quantity.delete(0, END)
        self.game_classification.delete(0, END)
        self.game_description.delete(0, END)
        self.game_price.delete(0, END)
        self.game_released.delete(0, END)
        self.game_devs.delete(0, END)

    # Go back to main menu
    def cancel_to_main(self):
        self.root.destroy()


    # Init the Graphic User Interface
    def init_gui(self):
        # WINDOW TITLE
        self.root.title("Agregar un videojuego")

        # WINDOW SIZE
        self.root.geometry("600x400")

        ############################## FRAMES ###############################
        # -------------------------- HEADER FRAME ---------------------------
        # Widgets
        self.header = PhotoImage(file='add-game.png')            
        self.header_frame = ttk.Frame(self.root)          # Crea un frame
        self.header_label = ttk.Label(self.header_frame)  # Crea una etiqueta para la img
        self.header_label['image'] = self.header          # Setea el label al tipo imagen
        # Grid
        self.header_label.grid(row=0, column=0)
        self.header_frame.grid(row=0, column=0)
        
        # ------------------------- INPUTS FRAME --------------------------------
        self.inputs_frame = ttk.Frame(self.root)
        # Widgets
        self.label_name = ttk.Label(self.inputs_frame, text="Nombre del videojuego")
        self.game_name = ttk.Entry(self.inputs_frame, width=60)
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
        self.label_quantity = ttk.Label(self.inputs_frame, text="Cantidad")
        self.game_quantity = ttk.Entry(self.inputs_frame, width=15)
        self.label_classification = ttk.Label(self.inputs_frame, text="Clasificación")
        self.game_classification = ttk.Entry(self.inputs_frame, width=15)
        self.label_description = ttk.Label(self.inputs_frame, text="Descripción")
        self.game_description = ttk.Entry(self.inputs_frame, width=50)
        self.label_price = ttk.Label(self.inputs_frame, text="Precio")
        self.game_price = ttk.Entry(self.inputs_frame, width=15)
        self.label_released = ttk.Label(self.inputs_frame, text="Fecha de publicaión")
        self.game_released = ttk.Entry(self.inputs_frame, width=15)
        self.label_devs = ttk.Label(self.inputs_frame, text="Desarrolladora")
        self.game_devs = ttk.Entry(self.inputs_frame, width=50)

        # GRID inputs
        self.label_name.grid(row=0, column=0, sticky=("w"), columnspan=2)
        self.game_name.grid(row=0, column=2, sticky=("we"), columnspan=3)

        self.label_condition.grid(row=1, column=0, sticky=("w"), columnspan=2)
        self.game_condition.grid(row=1, column=2, sticky=("we"), columnspan=3)

        self.label_quantity.grid(row=2, column=0, sticky=("w"))
        self.game_quantity.grid(row=2, column=2, sticky=("we"))
        self.label_classification.grid(row=2, column=3, sticky=("w"), columnspan=2)
        self.game_classification.grid(row=2, column=4, sticky=("we"), columnspan=3)

        self.label_description.grid(row=4, column=0, sticky=("w"), columnspan=2)
        self.game_description.grid(row=4, column=2, sticky=("we"), columnspan=3)

        self.label_price.grid(row=5, column=0, sticky=("w"))
        self.game_price.grid(row=5, column=2, sticky=("we"))
        self.label_released.grid(row=5, column=3, sticky=("w"))
        self.game_released.grid(row=5, column=4, sticky=("we"))

        self.label_devs.grid(row=7, column=0, sticky=("w"), columnspan=2)
        self.game_devs.grid(row=7, column=2, sticky=("we"), columnspan=3)

        # Padding
        for child in self.inputs_frame.winfo_children():
            child.grid_configure(padx=8, pady=3)
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
            self.btns_frame, text='Agregar', width=20, command=self.add_game)
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
        """ self.label_name.grid(row=0, column=0)
        self.game_name.grid(row=0, column=2, sticky=("we"))
        self.label_condition.grid(row=1, column=0)
        self.game_condition.grid(row=1, column=2, sticky=("we"))
        self.label_quantity.grid(row=2, column=0)
        self.game_quantity.grid(row=2, column=2, sticky=("we"))
        self.label_classification.grid(row=3, column=0)
        self.game_classification.grid(row=3, column=2, sticky=("we"))
        self.label_description.grid(row=4, column=0)
        self.game_description.grid(row=4, column=2, sticky=("we"))
        self.label_price.grid(row=5, column=0)
        self.game_price.grid(row=5, column=2, sticky=("we"))
        self.label_released.grid(row=6, column=0)
        self.game_released.grid(row=6, column=2, sticky=("we"))
        self.label_devs.grid(row=7, column=0)
        self.game_devs.grid(row=7, column=2, sticky=("we")) """

        # Buttons
        #self.btn_add.grid(row=19, column=2, sticky=("we"))
        #self.btn_back.grid(row=19, column=3, sticky=("we"))
        #self.btn_cancel.grid(row=19, column=4, sticky=("we"))

        self.header_label.grid(row=0, column=0)
        self.header_frame.grid(row=0, column=0)
        self.inputs_frame.grid(row=1, column=0)
        self.btns_frame.grid(row=5, column=0, padx=10, sticky=("e"))
if __name__ == '__main__':
    root = tkinter.Tk()
    AddGameWindow(root)
    root.mainloop()
