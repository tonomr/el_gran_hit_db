from tkinter import *
from tkinter import ttk
from views.menubar import Menubar
# This class will show all columns from all rows ot its model
class IndexWindow(ttk.Frame):
    def __init__(self, parent, win_title, win_size, sidebar, header_title, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.root.title(win_title)
        self.root.geometry(win_size)
        self.imgobj = PhotoImage(file=sidebar)
        self.header = PhotoImage(file=header_title)
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
        # Image/Logo widget
        self.label = ttk.Label(self)
        self.label['image'] = self.imgobj

        # Header image widget
        self.header_label = ttk.Label(self)
        self.header_label['image'] = self.header

        # Buttons
               # Widgets LAYOUT
        self.label.grid(row=0, column=0, rowspan=26, sticky=("we"))
        self.header_label.grid(row=1, column=1, rowspan=19, columnspan=2, sticky=("e"))
        
        # Padding
        for child in self.winfo_children():
            child.grid_configure(padx=8, pady=2)


