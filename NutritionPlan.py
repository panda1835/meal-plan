"""
This class creates an Interface for user to input nutrion plan and retrieve inputted value
"""
import tkinter as tk
from tkinter import ttk
TITLEFONT = ("Time New Roman", 15)

class NutritionPlan(tk.Frame):
    def __init__(self, parent, main_view):
        tk.Frame.__init__(self, parent)
        parent = tk.Frame(self, bg = "white")

        # title of the frame
        title = tk.Label(parent, text = "Nutrition Plan Standard ", 
        font = TITLEFONT, bg = "white")

        # the combobox
        valuelist = [1,2,3]
        self.nutrition_plan = tk.StringVar()
        combo_box = ttk.Combobox(parent, width = 15, values = valuelist, textvariable = self.nutrition_plan)
        
        
        # the back & next buttons
        next_but = tk.Button(parent, text ="Next", bg = "Green", relief = "flat", 
        command = lambda: main_view.show_frame(main_view.frame_BodyCondition))
            
        # make all elements visible by using grid
        parent.grid(column = 0, row = 0)
        title.grid(column = 0, row = 0, columnspan = 3, pady = 10, ipadx = 0)
        combo_box.grid (column = 1, row = 2, pady = 30)
        next_but.grid(column = 2, row = 3, padx = 15, pady = 10)