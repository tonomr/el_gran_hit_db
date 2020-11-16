from tkinter import *
from tkinter import ttk
from views.menubar import Menubar
# This class will show all columns from all rows ot its model
class IndexWindow(ttk.Frame):
    def __init__(self, parent, win_title, win_size, header_title, listbox, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.root.title(win_title)
        self.root.geometry(win_size)
        self.header = PhotoImage(file=header_title)
        self.items_listbox = listbox 
        self.init_gui()

    def clear_frames(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def show_all(self):
    
        pass

    def init_gui(self):
        # Grid config
        self.grid(column=0, row=0, sticky=("nswe"))

        # WIDGETS
        # Header image widget
        self.header_label = ttk.Label(self)
        self.header_label['image'] = self.header
        self.items = StringVar(value=self.items_listbox)
        self.listbox = Listbox(self.root, font='consolas', listvariable=self.items, width=80)
        
        # Buttons
        # Widgets LAYOUT
        self.header_label.grid(row=0, column=0, rowspan=19, columnspan=2, sticky=("we"))
        self.listbox.grid(row=1, column=0, sticky=("we"))
        
        # Padding
        for child in self.winfo_children():
            child.grid_configure(padx=8, pady=2)


