from tkinter import *
from tkinter import ttk
from services.logger_conf import logger
# Models
from models.videojuego import Videojuego
from models.cliente import Cliente
from models.empleado import Empleado
from models.venta import Venta
from models.compra import Compra
from models.desarrolladora import Desarrolladora
# Controllers
from controllers.videojuego_dao import VideojuegoDao
from controllers.clientes_dao import ClienteDao
from controllers.empleado_dao import EmpleadoDao
from controllers.venta_dao import VentaDao
from controllers.compra_dao import CompraDao
from controllers.desarrolladora_dao import DesarrolladoraDao
# Views
from views.crud_window import CrudWindow
from views.add_game import AddGame
from views.add_employee import AddEmployee
from views.add_customer import AddCustomer
from views.add_purchase import AddPurchase
from views.add_sell import AddSell
from views.add_dev import AddDev
from views.edit_game import EditGame
from views.delete_window import DeleteWindow
from views.menubar import Menubar
from views.index_window import IndexWindow
class GUI(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.init_gui()
    
    #------------------------------------ UTILITIES --------------------------------------------
    def clear_frames(self):
        for widget in self.root.winfo_children():
            widget.destroy()
            
    
   # ------------------------------------- VIDEOGAMES ------------------------------------------
    # Index Controller
    def game_index_window(self):
            game_list = VideojuegoDao.seleccionar()
            self.games_listbox = []
            for game in game_list:
                logger.debug(game) 
                self.games_listbox.append(game)
            self.new_win = Toplevel(self.root)
            IndexWindow(self.new_win, "Lista de Videojuegos", "810x500", "listbox-games.png", self.games_listbox)

    # Create Widnow
    def game_add_window(self):
        self.new_win = Toplevel(self.root)
        AddGame(self.new_win)

    # Edit Window
    def game_update_window(self):
        self.new_win = Toplevel(self.root)
        EditGame(self.new_win, "edit-game.png", self.search_game)

    # Delete Window
    def game_delete_window(self):
        self.new_win = Toplevel(self.root)
        self.search_pattern = self.search_game
        self.delete_controller = self.del_game_by_id
        DeleteWindow(self.new_win, "Elimina Videojuego", "810x500", "delete-game.png", self.search_pattern, self.delete_controller)
    
    # Delete Controller
    def del_game_by_id(self, id_game):
        videogame = Videojuego(id_juego=id_game)
        VideojuegoDao.eliminar(videogame)

    # Search Game Controller
    def search_game(self, search_term):
        game_list = VideojuegoDao.buscar(search_term)
        return game_list

    # CRUD Window
    def games_window(self):
        self.index_game = self.game_index_window
        self.create_game = self.game_add_window
        self.edit_game = self.game_update_window
        self.delete_game = self.game_delete_window
        self.clear_frames()
        CrudWindow(self.root, "Administra Videojuego", "title-game-menu.png", "sidebar.png", "Videojuegos", self.index_game, self.create_game, self.edit_game, self.delete_game)
    
    # ------------------------------------- CUSTOMERS ------------------------------------------
    # Index Window 
    def customers_index_window(self):
            customers_list = ClienteDao.seleccionar()
            self.customers_listbox = []
            for customer in customers_list:
                logger.debug(customer) 
                self.customers_listbox.append(customer)
            self.new_win = Toplevel(self.root)
            IndexWindow(self.new_win, "Lista de Clientes", "810x500", "listbox-games.png", self.customers_listbox)

    # Create Window
    def customer_add_window(self):
        self.new_win = Toplevel(self.root)
        AddCustomer(self.new_win)

    # Edit Window
    def customer_update_window(self):
        #self.new_win = Toplevel(self.root)
        #EditGame(self.new_win, "edit-customer.png", self.search_game)
        pass

    # Delete Window
    def customer_delete_window(self):
        self.new_win = Toplevel(self.root)
        self.search_pattern = self.search_customer
        self.delete_controller = self.del_customer_by_id
        DeleteWindow(self.new_win, "Elimina Cliente", "810x500", "delete-game.png", self.search_pattern, self.delete_controller)

    # Delete Controller
    def del_customer_by_id(self, id_customer):
        customer = Cliente(id_cliente=id_customer)
        ClienteDao.eliminar(customer)

    # Search Controller
    def search_customer(self, search_term):
        customer_list = ClienteDao.buscar(search_term)
        return customer_list
        
    
    # CRUD Window
    def customer_window(self):
        self.index_customer = self.customers_index_window
        self.create_customer = self.customer_add_window
        self.update_customer = self.customer_update_window
        self.delete_customer = self.customer_delete_window
        self.clear_frames()
        CrudWindow(self.root, "Administra Clientes", "title-customer-menu.png", "sidebar.png", "Clientes", self.index_customer, self.create_customer, self.update_customer, self.delete_customer)

    # ---------------------------------------- SELLS ------------------------------------------
    def add_sell(self):
        self.new_win = Toplevel(self.root)
        AddSell(self.new_win)

    def sells_window(self):
        self.index_sell = self.show_all
        self.create_sell = self.add_sell
        self.clear_frames()
        #CrudWindow(self.root, "Administra Ventas", "title-sell-menu.png", "sidebar.png", "Ventas" , self.index_sell, self.create_sell)
    
    # ------------------------------------- EMPLOYEES ------------------------------------------
    # Index Window 
    def employee_index_window(self):
            employees_list = EmpleadoDao.seleccionar()
            self.employees_listbox = []
            for employee in employees_list:
                logger.debug(employee) 
                self.employees_listbox.append(employee)
            self.new_win = Toplevel(self.root)
            IndexWindow(self.new_win, "Lista de Empleados", "810x500", "listbox-games.png", self.employees_listbox)

    # Create Window
    def employee_add_window(self):
        self.new_win = Toplevel(self.root)
        AddEmployee(self.new_win)

    # Edit Window
    def employee_update_window(self):
        #self.new_win = Toplevel(self.root)
        #EditEmployee(self.new_win, "edit-customer.png", self.search_game)
        pass

    # Delete Window
    def employee_delete_window(self):
        self.new_win = Toplevel(self.root)
        self.search_pattern = self.search_employee
        self.delete_controller = self.del_employee_by_id
        DeleteWindow(self.new_win, "Elimina Empleado", "810x500", "delete-game.png", self.search_pattern, self.delete_controller)

    # Delete Controller
    def del_employee_by_id(self, id_employee):
        employee = Empleado(id_empleado=id_employee)
        EmpleadoDao.eliminar(employee)

    # Search Controller
    def search_employee(self, search_term):
        employee_list = EmpleadoDao.buscar(search_term)
        return employee_list
        
    # CRUD Window
    def employees_window(self):
        self.index_employee = self.employee_index_window
        self.create_employee = self.employee_add_window
        self.update_employee = self.employee_update_window
        self.delete_employee = self.employee_delete_window
        self.clear_frames()
        CrudWindow(self.root, "Administra Empleado", "title-customer-menu.png", "sidebar.png", "Empleados", self.index_employee, self.create_employee, self.update_employee, self.delete_employee)
    
    # -------------------------------------- DESARROLLADORAS ------------------------------------
    # Index Window 
    def dev_index_window(self):
            devs_list = DesarrolladoraDao.seleccionar()
            self.devs_listbox = []
            for dev in devs_list:
                logger.debug(dev) 
                self.devs_listbox.append(dev)
            self.new_win = Toplevel(self.root)
            IndexWindow(self.new_win, "Lista de Desarrolladoras", "810x500", "listbox-games.png", self.devs_listbox)

    # Create Window
    def dev_add_window(self):
        self.new_win = Toplevel(self.root)
        AddDev(self.new_win)

    # Edit Window
    def dev_update_window(self):
        #self.new_win = Toplevel(self.root)
        #EditEmployee(self.new_win, "edit-customer.png", self.search_game)
        pass

    # Delete Window
    def dev_delete_window(self):
        self.new_win = Toplevel(self.root)
        self.search_pattern = self.search_dev
        self.delete_controller = self.del_dev_by_id
        DeleteWindow(self.new_win, "Elimina Desarrolladora", "810x500", "delete-game.png", self.search_pattern, self.delete_controller)

    # Delete Controller
    def del_dev_by_id(self, id_dev):
        dev = Desarrolladora(id_desarrolladora=id_dev)
        DesarrolladoraDao.eliminar(dev)

    # Search Controller
    def search_dev(self, search_term):
        dev_list = DesarrolladoraDao.buscar(search_term)
        return dev_list
        
    # CRUD Window
    def devs_window(self):
        self.index_dev = self.dev_index_window
        self.create_dev = self.dev_add_window
        self.update_dev = self.dev_update_window
        self.delete_dev = self.dev_delete_window
        self.clear_frames()
        CrudWindow(self.root, "Administra Empleado", "title-customer-menu.png", "sidebar.png", "Empleados", self.index_dev, self.create_dev, self.update_dev, self.delete_dev)
        
    # ------------------------------------------- COMPRAS --------------------------------------
    def add_purchase(self):
        self.new_win = Toplevel(self.root)
        AddPurchase(self.new_win)

    def purchases_window(self):
        self.index_purchase = self.show_all
        self.create_purchase = self.add_purchase
        self.clear_frames()
        #CrudWindow(self.root, "Administra Compras", "title-purchase-menu.png", "sidebar.png", "Compras", self.index_purchase, self.create_purchase)
        pass
    
    # ------------------------------------- MAIN INTERFACE --------------------------------------
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


