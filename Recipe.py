import tkinter as tk
from tkinter import ttk
import tkinter.scrolledtext as tkst

TITLEFONT = ("Time New Roman", 15)

class Recipe(tk.Frame):
    def __init__(self, content, parent, main_view, controller):
        tk.Frame.__init__(self, parent)
        parent = tk.Frame(self, bg = 'white')
        parent.grid(column = 0, row = 0)

        self.frame_Ours = FrameOurRecipeForYou(content, main_view, controller)
        self.frame_Ours.grid(row = 0, column = 0, sticky ="nsew")
        self.frame_Yours = FrameYourRecipe(content, main_view, controller)
        self.frame_Yours.grid(row = 0, column = 0, sticky ="nsew")
        self.frame_Create = FrameCreateYourRecipe(content, main_view, controller)
        self.frame_Create.grid(row = 0, column = 0, sticky ="nsew")

        self.show_frame(self.frame_Ours)

        ours_btn = tk.Button(parent, text = "Our Recipe for you", bg = "white", relief = "solid", borderwidth = 2,
        command = lambda:self.show_frame(self.frame_Ours))
        ours_btn.pack(side  = "left")
        
        yours_btn = tk.Button(parent, text = "Your Recipe", bg = "white",  relief = "solid", borderwidth = 2,
        command = lambda:self.show_frame(self.frame_Yours))
        yours_btn.pack(side  = "left")
        
        create_btn = tk.Button(parent, text = "Create your own Recipe", bg = "white",  relief = "solid", borderwidth = 2,
        command = lambda:self.show_frame(self.frame_Create))
        create_btn.pack(side  = "left")

    def show_frame(self, current_frame):
        current_frame.tkraise()

class FrameOurRecipeForYou(tk.Frame):
    def __init__(self, parent, main_view, controller):
        tk.Frame.__init__(self, parent)
        parent = tk.Frame(self, bg = 'white')
        parent.grid(column = 0, row = 0)
        
        title = tk.Label(parent, text = "Our recipe for you")  
        title.grid(column = 0, row = 1)      


class FrameYourRecipe(tk.Frame):
    def __init__(self, parent, main_view, controller):

        tk.Frame.__init__(self, parent)
        parent = tk.Frame(self, bg = 'white')
        parent.grid(column = 0, row = 0)
        
        title = tk.Label(parent, text = "Our recipe for you")  
        title.pack()    

class FrameCreateYourRecipe(tk.Frame):
    def __init__(self, parent, main_view, controller):

        tk.Frame.__init__(self, parent)
        parent = tk.Frame(self, bg = 'white')
        parent.grid(column = 0, row = 0) 
        button = tk.Frame(self, bg = "white")
        button.grid(column = 0, row = 1) 


        self.recipe_name = tk.StringVar()
        self.serving_size = tk.IntVar()
        self.cooking_time = tk.IntVar()
        self.tag = tk.StringVar()
        self.ingredients = tk.StringVar()
        self.nutritions = tk.StringVar()
        self.steps_taken = tk.StringVar()

        recipe_label = tk.Label(parent, text = "Name of dish", bg ="white", padx=5, pady=5, justify ="left")
        recipe_entry = ttk.Entry(parent, textvariable = self.recipe_name)

        serving_size_label = tk.Label(parent, text = "Serving size", bg ="white", anchor = "w", justify="left")
        serving_size_entry = ttk.Entry(parent, textvariable = self.serving_size)

        cooking_time_label = tk.Label(parent, text = "Cooking time", bg ="white", anchor = "w", justify="left", pady=5, padx=5)
        cooking_time_entry = ttk.Entry(parent, textvariable = self.cooking_time)

        tag_label = tk.Label(parent, text = "Tag", bg ="white", anchor = "w", justify="left", pady=5, padx=5)
        valuelist = [1,2,3]
        tag_combo = ttk.Combobox(parent, width = 5, values = valuelist, textvariable = self.tag)

        ingredient_label = tk.Label(parent, text = "Ingredients", bg ="white", anchor = "w", justify="left", pady=5, padx=5)
        ingredient_entry = ttk.Entry(parent, textvariable = self.ingredients)
        
        nutrition_label = tk.Label(parent, text = "Nutrition", bg ="white", anchor = "w", justify="left", pady=5, padx=5)
        nutrition_entry = ttk.Entry(parent, textvariable = self.nutritions)

        steps_taken_label = tk.Label(parent, text = "Steps Taken", bg ="white", anchor = "w", justify="left", pady=5, padx=5, height = 10)
        # steps_taken_entry = ttk.Entry(parent, textvariable = self.steps_taken)
        steps_taken_entry = tkst.ScrolledText(parent, wrap=tk.WORD, width = 20, height = 10)

        save_btn = ttk.Button(button, text = "Save",
        command = lambda : controller.save_recipe(self))

        recipe_label.grid(column=0, row=0, sticky = 'w')
        recipe_entry.grid(column=1, row=0)
        serving_size_label.grid(column=0, row=1)
        serving_size_entry.grid(column=1, row=1)
        cooking_time_label.grid(column=0, row=2)
        cooking_time_entry.grid(column=1, row=2)
        tag_label.grid(column=0, row=3)
        tag_combo.grid(column=1, row=3)
        ingredient_label.grid(column=0, row=4)
        ingredient_entry.grid(column=1, row=4)
        nutrition_label.grid(column=0, row=5)
        nutrition_entry.grid(column=1, row=5)
        steps_taken_label.grid(column=0, row=6)
        steps_taken_entry.grid(column=1, row=6) 
        save_btn.grid(column = 0, row = 0)