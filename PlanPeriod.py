"""
This class creates an interface for user to input the period for planning meal
"""
import tkinter as tk
from tkinter import ttk
import UserDefinedMeal
TITLEFONT = ("Time New Roman", 15)

class PlanPeriod(tk.Frame):
    def __init__(self, parent, main_view):
        tk.Frame.__init__(self, parent)
        parent = tk.Frame(self, bg = "white")

        # the title of the frame
        title = tk.Label(parent,text = "Set plan period", font = TITLEFONT, 
        bg = "white")

        # the combobox
        valuelist = ["Weekly"]
        plan_period = tk.StringVar()
        combo_box = ttk.Combobox(parent, width = 15, values = valuelist, 
        textvariable = plan_period)
        combo_box.current(0)

        #the back & next buttons
        back_but = tk.Button(parent, text = "Back", bg = "Green", relief = "flat", 
        command = lambda : main_view.show_frame(UserDefinedMeal))
        save_but = tk.Button(parent, text ="Save", bg = "Green", relief = "flat")
        
        # make all elements visible by using grid
        parent.grid(column = 0, row = 0)
        title.grid(column = 0, row = 0, columnspan = 3, pady = 10)
        combo_box.grid (column = 1, row = 2, pady = 30)
        back_but.grid(column = 0, row = 3, padx = 15, pady = 10)
        save_but.grid(column = 2, row = 3, padx = 15, pady = 10)
    
    def save_database(self, main_view):
        main_view.controller.save_user_info(main_view.user_info)
        main_view.controller.save_user_defined_meal(main_view.user_defined_meal)
