from tkinter import *
from tkinter import ttk
from services.logger_conf import logger
from views.crud_window import CrudWindow
from views.game_window import GameWindow
from controllers.videojuego_dao import VideojuegoDao
from views.menubar import Menubar
from views.index_window import IndexWindow
class GUI(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.init_gui()

    def clear_frames(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
    def show_all(self):
            game_list = VideojuegoDao.seleccionar()
            self.games_listbox = []
            for game in game_list:
                logger.debug(game)
                self.games_listbox.append(game)
            self.new_win = Toplevel(self.root)
            IndexWindow(self.new_win, "Lista de Videojuegos", "530x600", "listbox-games.png", self.games_listbox)

    def games_window(self):
        self.index_games = self.show_all
        self.clear_frames()
        #GameWindow(self.root)
        CrudWindow(self.root, "Administra Videojuego", "title-game-menu.png", "sidebar.png", "Videojuegos", self.index_games)

    def customer_window(self):
        self.index_games = self.show_all
        self.clear_frames()
        #GameWindow(self.root)
        CrudWindow(self.root, "Administra Clientes", "title-game-menu.png", "sidebar.png", "Clientes", self.index_games)
        pass

    def sells_window(self):
        self.index_games = self.show_all
        self.clear_frames()
        #GameWindow(self.root)
        CrudWindow(self.root, "Administra Ventas", "title-game-menu.png", "sidebar.png", "Ventas" , self.index_games)
        pass

    def employees_window(self):
        self.index_games = self.show_all
        self.clear_frames()
        #GameWindow(self.root)
        CrudWindow(self.root, "Administra Empleados", "title-game-menu.png", "sidebar.png", "Empleados", self.index_games)
        pass

    def devs_window(self):
        self.index_games = self.show_all
        self.clear_frames()
        #GameWindow(self.root)
        CrudWindow(self.root, "Administra Desarrolladoras", "title-game-menu.png", "sidebar.png", "Desarrolladoras", self.index_games)
        pass

    def purchases_window(self):
        self.index_games = self.show_all
        self.clear_frames()
        #GameWindow(self.root)
        CrudWindow(self.root, "Administra Compras", "title-game-menu.png", "sidebar.png", "Compras", self.index_games)
        pass
 
    def init_gui(self):
        self.root.title('El Gran Hit Videogames')
        self.root.geometry("600x400")
      
        self.grid(column=0, row=0, sticky=("nswe"))
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(2, weight=1)
      
        # GRID
        #self.root.grid_columnconfigure(0, weight=1)
        #self.root.grid_rowconfigure(0, weight=1)
        # Disables ability to tear menu bar into own window
        self.root.option_add('*tearOff', 'FALSE')

        self.menubar = Menubar(self.root)

        # WIDGETS
        # Image/Logo widget
        self.label = ttk.Label(self)
        self.imgobj = PhotoImage(file='logo.png')
        self.label['image'] = self.imgobj

        # Header image widget
        self.header_label = ttk.Label(self)
        self.header = PhotoImage(file='titles-header.png')
        self.header_label['image'] = self.header

        # Buttons
        self.btn_games = ttk.Button(self, text='Videojuegos', width=30, command=self.games_window)
        self.btn_employees = ttk.Button(self, text='Empleados', width=30, command=self.employees_window)
        self.btn_customers = ttk.Button(self, text='Clientes', width=30, command=self.customer_window)
        self.btn_sells = ttk.Button(self, text='Ventas', width=30, command=self.sells_window)
        self.btn_devs = ttk.Button(self, text='Desarrolladoras', width=30, command=self.devs_window)
        self.btn_purchases = ttk.Button(self, text='Compras', width=30, command=self.purchases_window)

        # Widgets LAYOUT
        self.label.grid(row=0, column=0, rowspan=26, sticky=("we"))
        self.header_label.grid(row=1, column=1, rowspan=19, columnspan=2, sticky=("e"))

        self.btn_games.grid(row=20, column=2, sticky=("we"))
        self.btn_employees.grid(row=21, column=2, sticky=("we")) 
        self.btn_customers.grid(row=22, column=2, sticky=("we"))
        self.btn_sells.grid(row=23, column=2, sticky=("we"))
        self.btn_devs.grid(row=24, column=2, sticky=("we"))
        self.btn_purchases.grid(row=25, column=2, sticky=("we"))
        
        # Padding
        for child in self.winfo_children():
            child.grid_configure(padx=8, pady=2)

    

if __name__ == '__main__':
    root = tkinter.Tk()
    GUI(root)
    root.mainloop()


""" 
  try:
    value = float(feet.get())
    meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
  except ValueError:
    pass

feet = StringVar()
meters = StringVar()

feet_entry = ttk.Entry(mainframe, width = 10, textvariable = feet)
feet_entry.grid(column = 2, row = 1, sticky = (W,E))

ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children():
  child.grid_configure(padx=5, pady=5)

feet_entry.focus() """

