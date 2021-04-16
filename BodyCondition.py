"""
This class creates an interface for user to input physical conditions of height, weight, age
"""
import tkinter as tk
from tkinter import ttk
TITLEFONT = ("Time New Roman", 15)

class BodyCondition(tk.Frame):
    def __init__(self, parent, main_view):
        tk.Frame.__init__(self, parent)
        parent = tk.Frame(self, bg = "white")
        

        #title of the frame
        title = tk.Label(parent,text = "Your body condition", font = TITLEFONT, 
        bg = "white")


        self.height_info = tk.IntVar()
        self.weight_info = tk.IntVar()
        self.age_info = tk.IntVar()

        # the height-weight-age titles and entries
        height = tk.Label(parent, text = "Height", bg = "white")
        height_entry = ttk.Entry(parent, width = 10, textvariable = self.height_info)
        weight = tk.Label(parent, text = "Weight", bg = "white")
        weight_entry = ttk.Entry(parent, width = 10, textvariable = self.weight_info)
        age = tk.Label(parent, text = "Age", bg = "white")
        age_entry = ttk.Entry(parent, width = 10, textvariable = self.age_info)

        #the back & next buttons
        backbtn = tk.Button(parent, text = "Back", bg = "Green", relief = "flat", 
        command = lambda : main_view.show_frame(main_view.frame_NutritionPlan))
        nextbtn = tk.Button(parent, text ="Next", bg = "Green", relief = "flat", 
        command = lambda: main_view.show_frame(main_view.frame_UserDefinedMeal))

        # make all elements visible by using grid
        parent.grid(column = 0, row = 0)
        title.grid(column = 0, row = 0, columnspan = 3, pady = 10)
        height.grid(column = 0, row = 1, padx = 5, pady = 5)
        height_entry.grid(column = 0, row = 2, padx = 10, pady = 10)
        age.grid(column = 1, row = 1, padx = 10, pady = 10)
        age_entry.grid(column = 1, row = 2, padx = 10, pady = 10)
        weight.grid(column = 2, row = 1, padx = 10, pady = 10)
        weight_entry.grid(column = 2, row = 2, padx = 10, pady = 10)
        backbtn.grid(column = 0, row = 3, padx = 10, pady = 10)
        nextbtn.grid(column = 2, row = 3, padx = 10, pady = 10)
