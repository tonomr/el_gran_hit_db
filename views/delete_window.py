from tkinter import *
from tkinter import ttk
from views.menubar import Menubar
# This class is a pop up window that receives a function to search for an item
# in the DB and another function to delete that item using its ID as selector
class DeleteWindow(ttk.Frame):
    def __init__(self, parent, win_title, win_size, header_title, search_controller, delete_controller, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.root.title(win_title)
        self.root.geometry(win_size)
        self.header = PhotoImage(file=header_title)
        self.search_controller = search_controller
        self.delete_controller = delete_controller
        self.init_gui()

    def clear_frames(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def search_item(self):
      like_pattern = ('%{}%'.format(self.search_term.get()),)
      self.list_items = self.search_controller(like_pattern)
      for item in self.list_items:
        self.listbox.insert(END, item)

    def delete_item(self):
      self.delete_controller(self.delete_byid.get())

    def init_gui(self):
        # Grid config
        self.grid(column=0, row=0, sticky=("nswe"))
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        #self.root.grid_columnconfigure(2, weight=1)

        # WIDGETS
        # Header image widget
        self.header_label = ttk.Label(self)
        self.header_label['image'] = self.header
        #self.items = StringVar(value=self.items_listbox)
        self.label_search = ttk.Label(self.root, text="Buscar por nombre")
        self.search_term = ttk.Entry(self.root, width=50)

        self.btn_search = ttk.Button(
            self.root, text='Buscar', width=15, command=self.search_item)

        self.label_delete = ttk.Label(self.root, text="Introduzca el id para eliminar")
        self.delete_byid = ttk.Entry(self.root, width=50)

        self.btn_delete= ttk.Button(
            self.root, text='Eliminar', width=15, command=self.delete_item)

        self.listbox = Listbox(self.root, font='consolas', width=75, height=5)
        
        # Buttons
        # Widgets LAYOUT
        self.header_label.grid(row=0, column=0, columnspan=3, sticky=("we"))
        self.listbox.grid(row=1, column=0, sticky=("we"))
        self.label_search.grid(row=2, column=0)
        self.search_term.grid(row=3, column=0) 
        self.btn_search.grid(row=4, column=0)

        # DELETE
        self.label_delete.grid(row=5, column=0)
        self.delete_byid.grid(row=6, column=0) 
        self.btn_delete.grid(row=7, column=0)
        
        # Padding
        for child in self.winfo_children():
            child.grid_configure(padx=8, pady=2)


