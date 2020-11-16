from tkinter import *
from tkinter import ttk
from services.logger_conf import logger
from models.videojuego import Videojuego
from controllers.videojuego_dao import VideojuegoDao
from controllers.desarrolladora_dao import DesarrolladoraDao
from views.crud_window import CrudWindow
from views.add_game import AddGame
from views.add_employee import AddEmployee
from views.add_customer import AddCustomer
from views.add_purchase import AddPurchase
from views.add_sell import AddSell
from views.add_dev import AddDev
from views.delete_window import DeleteWindow
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
    
    #------------- UTILITIES ---------------

    
            
    
    #------------- VIDEOGAMES --------------
    def show_all(self):
            game_list = VideojuegoDao.seleccionar()
            self.games_listbox = []
            for game in game_list:
                logger.debug(game) 
                self.games_listbox.append(game)
            self.new_win = Toplevel(self.root)
            IndexWindow(self.new_win, "Lista de Videojuegos", "770x500", "listbox-games.png", self.games_listbox)

    def add_game(self):
        self.new_win = Toplevel(self.root)
        AddGame(self.new_win)

    def search_game(self, search_term):
        game_list = VideojuegoDao.buscar(search_term)
        return game_list

    def delete_window(self):
        self.new_win = Toplevel(self.root)
        self.search_pattern = self.search_game
        self.delete_controller = self.del_game_by_id
        DeleteWindow(self.new_win, "Elimina Videojuego", "780x500", "delete-game.png", self.search_pattern, self.delete_controller)
    
    def del_game_by_id(self, id_game):
        videogame = Videojuego(id_juego=id_game)
        VideojuegoDao.eliminar(videogame)

    def games_window(self):
        self.index_game = self.show_all
        self.create_game = self.add_game
        self.delete_game = self.delete_window
        self.clear_frames()
        CrudWindow(self.root, "Administra Videojuego", "title-game-menu.png", "sidebar.png", "Videojuegos", self.index_game, self.create_game, self.delete_game)
    # -------------- CUSTOMERS -------------
    def add_customer(self):
        self.new_win = Toplevel(self.root)
        AddCustomer(self.new_win)

    def customer_window(self):
        self.index_customer = self.show_all
        self.create_customer = self.add_customer
        self.clear_frames()
        #CrudWindow(self.root, "Administra Clientes", "title-customer-menu.png", "sidebar.png", "Clientes", self.index_customer, self.create_customer)

    #---------------- SELLS ----------------
    def add_sell(self):
        self.new_win = Toplevel(self.root)
        AddSell(self.new_win)

    def sells_window(self):
        self.index_sell = self.show_all
        self.create_sell = self.add_sell
        self.clear_frames()
        #CrudWindow(self.root, "Administra Ventas", "title-sell-menu.png", "sidebar.png", "Ventas" , self.index_sell, self.create_sell)
    
    #------------- EMPLOYEES --------------
    def add_employee(self):
        self.new_win = Toplevel(self.root)
        AddEmployee(self.new_win)

    def employees_window(self):
        self.index_games = self.show_all
        self.create_employee = self.add_employee
        self.clear_frames()
        #CrudWindow(self.root, "Administra Empleados", "title-employee-menu.png", "sidebar.png", "Empleados", self.index_games, self.create_employee)
    
    #------------- DESARROLLADORAS --------------
    def add_dev(self):
        self.new_win = Toplevel(self.root)
        AddDev(self.new_win)

    def devs_window(self):
        self.index_games = self.show_all
        self.create_dev = self.add_dev
        self.clear_frames()
        #CrudWindow(self.root, "Administra Desarrolladoras", "title-dev-menu.png", "sidebar.png", "Desarrolladoras", self.index_games, self.create_dev)
        
    #------------- COMPRAS ----------------
    def add_purchase(self):
        self.new_win = Toplevel(self.root)
        AddPurchase(self.new_win)

    def purchases_window(self):
        self.index_purchase = self.show_all
        self.create_purchase = self.add_purchase
        self.clear_frames()
        #CrudWindow(self.root, "Administra Compras", "title-purchase-menu.png", "sidebar.png", "Compras", self.index_purchase, self.create_purchase)
        pass
    
    #--------------- INTERFAZ ------------------
    def init_gui(self):
        self.root.title('El Gran Hit Videogames')
        #self.root.geometry("600x400")
      
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


