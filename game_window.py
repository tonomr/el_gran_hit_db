from tkinter import *
from tkinter import ttk
from add_game_win import *
from menubar import *


class GameWindow(ttk.Frame):

    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.init_gui()

    def add_window(self):
        # self.new_win = Toplevel(self.root) # Set parent and create a new window
        # AddGameWindow(self.new_win) #New window
        self.clear_frames()
        AddGameWindow(self.root)

    def init_gui(self):
        self.root.title("Administra Videojuego")
        self.root.geometry("600x400")
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(2, weight=1)

        self.btn_games = ttk.Button(
        self, text='Agregar juego', width=100, command=self.add_window)

        self.btn_games.grid(row=0, column=0, sticky=("we"))


        self.pack()
        # self.btn_employees = ttk.Button(self, text='Ver todos los juegos', width=30, command=self.employees_window)
        # self.btn_customers = ttk.Button(self, text='Modificar juego', width=30, command=self.customer_window)
        # self.btn_shippings = ttk.Button(self, text='eliminarjuego', width=30, command=self.shippings_window)

    def clear_frames(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == '__main__':
    root = tkinter.Tk()
    AddGameWindow(root)
    root.mainloop()