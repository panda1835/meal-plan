"""
This class creates an Interface for user to input their own recipes
"""
import tkinter as tk
from tkinter import ttk
TITLEFONT = ("Time New Roman", 15)

class CreateRecipes(tk.Frame):
    def __init__(self, parent, main_view):
        tk.Frame.__init__(self, parent)
        parent = tk.Frame(self, bg = "white")

        recipe_label = tk.Label(parent, text = "Name of dish", padyx=5, pady=5, justify ="left")
        recipe = tk.StringVar()
        recipe_entry = ttk.Entry(parent, textvariable = recipe)

        serving_size_label = tk.Label(parent, text = "Serving size", bg ="white", anchor = "w", justify="left", pady=5, padx=5)
        serving_size = tk.IntVar()
        serving_size_entry = ttk.Entry(parent, textvariable = serving_size)

        cooking_time_label = tk.Label(parent, text = "Cooking time", bg ="white", anchor = "w", justify="left", pady=5, padx=5)
        cooking_time = tk.IntVar()
        cooking_time_entry = ttk.Entry(parent, textvariable = cooking_time)

        tag_label = tk.Label(parent, text = "Tag", bg ="white", anchor = "w", justify="left", pady=5, padx=5)
        #valuelist = [CreateSubUserDefinedMeal(name)]
        tag = tk.StringVar()
        valuelist = [1,2,3]
        tag_combo = ttk.Combobox(parent, width = 5, values = valuelist, textvariable = tag)

        ingredient_label = tk.Label(parent, text = "Ingredients", bg ="white", anchor = "w", justify="left", pady=5, padx=5)
        # add
        # name_entry = ttk.Entry(parent)

        steps_taken_label = tk.Label(parent, text = "Ingredients", bg ="white", anchor = "w", justify="left", pady=5, padx=5)
        steps_taken = tk.StringVar()
        steps_taken_entry = ttk.Entry(parent, textvariable = steps_taken)

        parent.grid(column = 0, row = 0)
        recipe_label.grid(column=0, row=0)
        recipe_entry.grid(column=1, row=0)
        serving_size_label.grid(column=0, row=1)
        serving_size_entry.grid(column=1, row=1)
        cooking_time_label.grid(column=0, row=2)
        cooking_time_entry.grid(column=1, row=2)
        tag_label.grid(column=0, row=3)
        tag_combo.grid(column=1, row=3)
        ingredient_label.grid(column=0, row=4)
        steps_taken_label.grid(column=0, row=5)
        steps_taken_entry.grid(column=1, row=5)

        