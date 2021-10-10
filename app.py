import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
from pattern import *

# Create the frame for the app
class InStitches(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidgets()

    # Create the widgets in the app window
    def createWidgets(self):
        root.geometry(str(root.winfo_screenwidth())+"x"+str(root.winfo_screenheight()))
        ttk.Button(text="Submit", style='success.TButton').pack(side='left', padx=5, pady=10)
        ttk.Button(text="Submit", style='success.Outline.TButton').pack(side='left', padx=5, pady=10)

# Color window pane class
class ColorPane(tk.Frame):
    def __init__(self, master=None):
        pass

# Instatitate the app and its classes
root = tk.Tk(className=' In Stitches ')
style = Style(theme='minty')
app = InStitches(master=root)
app.mainloop()
