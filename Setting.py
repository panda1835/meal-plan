import tkinter as tk
from tkinter import ttk
TITLEFONT = ("Time New Roman", 15)

class Setting(tk.Frame):
    def __init__(self, content, option, main_view):
        tk.Frame.__init__(self, option)
        option = tk.Frame(self, bg = 'white')
        option.grid(column = 0, row = 0)

        personal_btn = tk.Button(option, text = "Personal info", bg = "white", relief = "flat")
        personal_btn.pack(side  = "left")
        
        nut_btn = tk.Button(option, text = "Nutritional info", bg = "white", relief = "flat")
        nut_btn.pack(side  = "left")
        
        meal_btn = tk.Button(option, text = "Meal info", bg = "white", relief = "flat")
        meal_btn.pack(side  = "left")