from tkinter import *
from tkinter import ttk
from views.menubar import Menubar

from models.videojuego import Videojuego
from controllers.videojuego_dao import VideojuegoDao

# Clase recibe una ventana como parametro, la ventana padre
class AddGameWindow(ttk.Frame):
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
        videogame = Videojuego(nombre_juego=name, estado=condition, cantidad=quantity, clasificacion=classification,
                               descripcion=description, precio=price, fecha_publicacion=released, codigo_desarrolladora=devs)
        VideojuegoDao.insertar(videogame)

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
        # WINDOW TITLE
        self.root.title("Agregar un videojuego")

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
        self.label_name = ttk.Label(self.root, text="Nombre del videojuego")
        self.game_name = ttk.Entry(self.root, width=50)
        # Multiple Option input
        # Crea la etiqueta "Condición"
        self.label_condition = ttk.Label(self.root, text="Condición")
        # Crea el objeto de input múltiple, recibe ventana padre y ocpional el ancho
        self.game_condition = ttk.Combobox(self.root, width=30)
        # Agrega una tupla a la configuración 'values' del input
        # Aquí agregamos los valores que se usan
        self.game_condition['values'] = ('Nuevo', 'Seminuevo', 'Usado')
        # Configuramos el estado del input para que sea únicamente de lectura
        # y el usario no pueda modificar su valor
        self.game_condition.state(['readonly'])
        # More labels and input fields...
        self.label_quantity = ttk.Label(self.root, text="Cantidad")
        self.game_quantity = ttk.Entry(self.root, width=15)
        self.label_classification = ttk.Label(self.root, text="Clasificación")
        self.game_classification = ttk.Entry(self.root, width=50)
        self.label_description = ttk.Label(self.root, text="Descripción")
        self.game_description = ttk.Entry(self.root, width=50)
        self.label_price = ttk.Label(self.root, text="Precio")
        self.game_price = ttk.Entry(self.root, width=10)
        self.label_released = ttk.Label(self.root, text="Fecha de publicaión")
        self.game_released = ttk.Entry(self.root, width=10)
        self.label_devs = ttk.Label(self.root, text="Desarrolladora")
        self.game_devs = ttk.Entry(self.root, width=50)

        #--------------------------------------------------------------------------
        # BUTTONS
        # Add button
        # Al presionar este parametro, mandamos llamar la función que específicamos
        # en 'command'
        #--------------------------------------------------------------------------
        # Add
        self.btn_add = ttk.Button(
            self.root, text='Agregar', width=30, command=self.add_game)
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
        self.game_devs.grid(row=7, column=2, sticky=("we"))

        # Buttons
        self.btn_add.grid(row=19, column=2, sticky=("we"))
        #self.btn_back.grid(row=19, column=3, sticky=("we"))
        #self.btn_cancel.grid(row=19, column=4, sticky=("we"))


if __name__ == '__main__':
    root = tkinter.Tk()
    AddGameWindow(root)
    root.mainloop()
