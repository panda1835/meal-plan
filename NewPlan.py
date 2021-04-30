import tkinter as tk
from tkinter import ttk
TITLEFONT = ("Time New Roman", 15)

class NewPlan(tk.Frame):
    def __init__(self, content, option, main_view):
        tk.Frame.__init__(self, option)
        option = tk.Frame(self, bg = 'white')