from tkinter import *
from tkinter import ttk
from views.add_game_win import AddGameWindow
from views.menubar import *
from views.index_window import IndexWindow

class GameWindow(ttk.Frame):

    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.init_gui()
    # Create a new Videogame
    def create_window(self):
        # self.new_win = Toplevel(self.root) # Set parent and create a new window
        # AddGameWindow(self.new_win) #New window
        self.clear_frames()         #Limpia los widgets en la ventana
        AddGameWindow(self.root)    # Instancia una nueva ventana de AddGameWindow

    # Show all VideoGames
    def index_window(self):
        self.clear_frames()
        IndexWindow(self.root, "Lista de Videojuegos", "500x600", "sidebar.png", "titles-header.png")
        pass
    
    # Edit a videogame
    def edit_window(self):
        pass
    
    # Delete a videogame
    def destroy_window(self):
        pass
    

    def init_gui(self):
        self.grid_forget()
        self.root.title("Administra Videojuego")
        self.root.geometry("600x400")
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=0)

        # Image/Sidebar widget
        self.sidebar = ttk.Label(self.root)
        self.imgobj = PhotoImage(file='sidebar.png')
        self.sidebar['image'] = self.imgobj

        # Header image widget
        self.header_label = ttk.Label(self.root)
        self.header = PhotoImage(file='title-game-menu.png')
        self.header_label['image'] = self.header

        self.btn_create = ttk.Button(
        self.root, text='Agregar juego', width=30, command=self.create_window)
        self.btn_index = ttk.Button(
        self.root, text='Listar Videojuegos', width=30, command=self.index_window)
        self.btn_edit = ttk.Button(
        self.root, text='Modificar Videojuego', width=30, command=self.edit_window)
        self.btn_destroy = ttk.Button(
        self.root, text='Eliminar Videojuego', width=30, command=self.destroy_window)

        # Grid Images
        self.sidebar.grid(row=0, column=0, rowspan=21, sticky=("ws"))
        self.header_label.grid(row=0, column=1, rowspan=10, columnspan=2, sticky=("we"))

        # Grid Buttons
        self.btn_create.grid(row=14, column=1, sticky=("nwes"), columnspan=2)
        self.btn_index.grid(row=16, column=1, sticky=("nwes"), columnspan=2)
        self.btn_edit.grid(row=18, column=1, sticky=("nwes"), columnspan=2)
        self.btn_destroy.grid(row=20, column=1, sticky=("nwes"), columnspan=2)

        # Padding
        
        # self.btn_employees = ttk.Button(self, text='Ver todos los juegos', width=30, command=self.employees_window)
        # self.btn_customers = ttk.Button(self, text='Modificar juego', width=30, command=self.customer_window)
        # self.btn_shippings = ttk.Button(self, text='eliminarjuego', width=30, command=self.shippings_window)
        #self.pack()
    def clear_frames(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        

if __name__ == '__main__':
    root = tkinter.Tk()
    AddGameWindow(root)
    root.mainloop()